#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CdM8 IDE and emulator
# (c) M L Walters and A Shafarenko June-July 2018

####### CDM8 Emulator
# V4.00 Update for new stack instructions (Alex)
# V4.01 Changed to show memory changes back to CocoIDE/CocoEmu for new 
#       pushall instruction (Mick)
# V4.2  Implement Harvard Architecture - two mem banks, + support for ldc)# 

# Aug 2018, M L Walters
# V1.6 Modifications to use IO Ports from CocoIDE (ld and st instructions)
# V1.7 Implement instructions ioi, osix and rti
# V1.8 Paged Memory and HW/SW Interrupts, Mick, Aug 2018


# Python3 and 2
from __future__ import absolute_import, division, print_function

import argparse
import random

random.seed()
import time
import sys


class CDM8Emu():

    def __init__(self, memory=None, arch="vn", pages=8, parent=None):
        self.parent = parent
        self.VN = "vn"
        self.HV = "hv"
        self.arch = ["vn"] * pages

        args.arch  # Default Von Neuman Architecture

        # Class variables/ attributes
        self.curPage = 0

        self.memChanged = [[0]] * pages
        self.datamem = [0] * pages
        self.memory = [[0]] * pages  # default = 8
        # print("&",self.memory)
        # print("datamem", self.datamem)
        # print("memChanged", self.memChanged)

        # Setup Memory
        # print("Memory\n", self.memory[0])#debug
        self.setArch(args.arch, page=0)
        for n in range(1, pages):
            self.setArch(self.arch, page=n)  # default is vn, page 0 to 8
            # print("$", n)
        if memory:  # load .img file if provided
            self.memory[0][0] = memory
        # print("%\n", self.memory[0])

        self.regs = [0, 0, 0, 0]
        self.PC = 0
        self.SP = [0] * pages
        self.IR = 0
        self.IP = []
        self.CVZN = 0x0
        self.BP = []
        self.HALT = False
        self.running = False
        self.adr = None  # Used for CocoIDE fetching current st address
        self.shadowSP = True
        # Trace vars
        self.traddrs = []
        # self.traceprint=False
        self.cntr = 0  # Trace control var
        self.pretend = True  # Pretend that standard.mlb macros are real machine instructions

    def setArch(self, arch="vn", page=0):
        if arch == "vn":
            self.memory[page] = [[0] * 256, [0] * 256]  # clear memory
            self.memChanged[page] = []
            self.datamem[page] = 0

        elif arch == "hv":
            self.memory[page] = [[0] * 256, [0] * 256]  # clear memory
            self.memChanged[page] = []
            self.datamem[page] = 1
            # print(arch, page, self.memory[page])
        else:
            return "Unrecognised Architecture"
        self.arch[page] = arch
        # print("^",self.memory[page])
        return

    def changePC(self, n=0):
        self.PC = (n + 256) % 256  # Wrap around to 0 if 255
        return

    def hx(self, n):
        return format((n + 256) % 256, "02x").upper()

    def convert(self, fmt, k):
        if fmt == 0:
            # hex
            return self.hx(k)
        if fmt == 1:
            if k < 128:
                # signed int
                kk = 256 + k
            else:
                # signed decimal
                kk = k
            return "{0:+04d}".format(kk - 256)
        if fmt == 2:
            # print("**"+chr(k), k)
            if k > 31 and k < 127:
                return "'" + chr(k) + "'"
            elif k == 0:
                return "NUL"
            else:
                return ""
        if fmt == 3:
            return "0b{0:08b}".format(k)

    def loadImg(self):  # Not implemented yet
        # Direct load image from file under CocoIDE
        print("Load memory imag from file not implemented yet")

    def disasm(self, adr):
        self.IR = self.memory[self.curPage][0][adr]
        if self.IR & 0x80 == 0:
            fun = self.IR >> 4
            opcode = ["move", "add", "addc", "sub", "and", "or", "xor", "cmp"][fun]
            Rs = (self.IR >> 2) & 3
            Rd = self.IR & 3

            if self.pretend and Rs == Rd:
                if opcode == "move":
                    return "tst r" + str(Rs)
                if opcode == "sub":
                    return "clr r" + str(Rs)
                if opcode == "addc":
                    return "shl r" + str(Rs)

            return opcode + ' r' + str(Rs) + ',r' + str(Rd)
        if self.IR >> 5 == 0b100:
            fun = (self.IR >> 2) & 7
            opcode = ["not", "neg", "dec", "inc", "shr", "shla", "shra", "rol"][fun]
            Rd = self.IR & 3
            return opcode + ' r' + str(Rd)
        if self.IR >> 5 == 0b101:
            fun = (self.IR >> 4) & 1
            opcode = ["st", "ld"][fun]
            Rs = (self.IR >> 2) & 3
            Rd = self.IR & 3
            return opcode + ' r' + str(Rs) + ',r' + str(Rd)
        if self.IR >> 4 == 0b1100:
            fun = (self.IR >> 2) & 3
            opcode = ["push", "pop", "stsp", "ldsp"][fun]
            Rd = self.IR & 3
            return opcode + ' r' + str(Rd)
        if self.IR >> 2 == 0b110100:
            Rd = self.IR & 3
            return "ldi r" + str(Rd) + ",0x" + hx(self.memory[self.curPage][0][adr + 1])
        if self.IR >> 4 == 0b1101:
            fun = self.IR & 15
            opcode = ["", "", "", "", "halt", "wait", "jsr", "rts", "osi", "rti", "crc", "osix"] + ["<ext0>", "<ext1>",
                                                                                                    "<ext2>", "<ext3>"]
            opcode = opcode[fun]
            if fun == 6 or fun == 11:
                return opcode + ' 0x' + hx(self.memory[self.curPage][0][adr + 1])
            else:
                return opcode
        if self.IR >> 4 == 0b1110:
            opcode = ["eq", "ne", "hs", "lo", "mi", "pl", "vs", "vc", "hi", "ls", "ge", "lt", "gt", "le", "r", "nop"]
            fun = self.IR & 15
            pref = "b"
            if fun == 15:
                pref = ""
            return pref + opcode[fun] + ' 0x' + hx(self.memory[self.curPage][0][adr + 1])
        if self.IR >> 4 == 0b1111:
            return "bbne 0x" + hx((adr - 1 - (self.IR & 15) + 256) % 256)

    def step(self, interrupt=None, intvector=0):
        # global self.PC, self.SP, self.IP, self.CVZN, self.memory[0], self.regs, self.HALT, random

        def setZN(x):  # Sets the z and N flags
            self.CVZN = self.CVZN & 0b11111100
            if x == 0:
                self.CVZN = self.CVZN | 2
            elif x >= 128:
                self.CVZN = self.CVZN | 1

        # Set current memory page
        self.curPage = (self.CVZN & 0b01110000) >> 4
        # Local Shadow stacks or page 0 stack only
        if self.shadowSP == True:
            stackPage = self.curPage
        else:
            stackPage = 0

        ## If HW/IO interupt, generate Interrupt Instruction, ioi. Mick Aug 2018
        if interrupt:
            self.IR = 0xD8  # Hardware interrupt "ioi"
        else:  # Fetch next instruction to IR
            self.IR = self.memory[self.curPage][0][self.PC]

        # print("IR_1=", self.IR)
        ##Trace
        if args.trace:
            if self.PC in self.IP or self.IR == 0xd4:
                regstr = ""
                for ind in [0, 1, 2, 3]:
                    regstr += format(self.regs[ind], "02x") + " "
                trace = format(self.cntr, "06d") + ": " + "PC=" + format(self.PC, "02x") + " Regs: " + regstr
                memstr = ""
                if self.traddrs != []:
                    tra = ""
                    for i in range(len(traddrs)):
                        tr = traddrs[i]
                        tra += format(tr, "02x") + "  "
                        trfmt = trfmts[i]
                        if trfmt == 'x':
                            memstr += "  " + convert(0, self.memory[self.curPage][0][tr])
                        elif trfmt == 'c':
                            memstr += " " + convert(2, self.memory[self.curPage][0][tr])
                        elif trfmt == "d":
                            memstr += " " + convert(1, self.memory[self.curPage][0][tr])
                        else:
                            EP("Internal error")
                        tr += 1
                    trace += memstr
                    if not self.traceprint:
                        print(34 * " " + tra)
                        self.traceprint = True
                if (self.IR == 0xd4):
                    trace = trace + " <<< halt >>>"
                print(trace)
        ## End Trace

        if self.IR & 0x80 == 0:  # binary ALU
            fun = self.IR >> 4
            Rs = (self.IR >> 2) & 3
            Rd = self.IR & 3
            X = self.regs[Rs]
            Y = self.regs[Rd]
            if fun == 0:  # move
                Res = X
                setZN(Res)
                self.CVZN = self.CVZN & 0b11110011
            elif fun == 1 or fun == 2 or fun == 3 or fun == 7:  # add/addc/sub/cmp
                C = 0
                if fun == 3 or fun == 7:  # sub or cmp
                    Y = Y ^ 0xff  # invert
                    C = 1  # add 1 - i.e twos comp negate
                if fun == 2:  # addc
                    C = (self.CVZN & 0b00001000) >> 3  # Mick Aug 2018

                Res = (X + Y + C) % 256
                self.CVZN = self.CVZN & 0b11110000  # clear CVZN
                setZN(Res)
                if X + Y + C >= 256:
                    self.CVZN = self.CVZN | 8  # Set C
                if Res >= 128 and X < 128 and Y < 128:
                    self.CVZN = self.CVZN | 4  # Set V
                if Res < 128 and X >= 128 and Y >= 128:
                    self.CVZN = self.CVZN | 4  # Set V
            elif fun == 4:  # and
                Res = X & Y
                setZN(Res)
            elif fun == 5:  # or
                Res = X | Y
                setZN(Res)
            elif fun == 6:  # xor
                Res = X ^ Y
                setZN(Res)

            if fun != 7:  # cmp
                self.regs[Rd] = Res

            self.changePC(self.PC + 1)
            return

        if self.IR >> 5 == 0b100:  # ALU unary
            fun = (self.IR >> 2) & 7
            Rd = self.IR & 3
            X = self.regs[Rd]

            if fun == 0:  # not
                Res = X ^ 255
                setZN(Res)
                self.CVZN = self.CVZN & 0b11110011  # ??

            if fun == 1:  # neg
                Res = ((X ^ 255) + 1) % 256
                self.CVZN = self.CVZN & 0b11110000  # clear CVZN
                setZN(Res)
                if Res >= 128 and X >= 128:
                    self.CVZN = self.CVZN | 4  # Set V

                if X == 0:
                    self.CVZN = self.CVZN | 8  # Set Z

            if fun == 2:  # dec
                Res = (X + 255) % 256
                if X == 0:  # Carry?
                    self.CVZN = self.CVZN | 8  # 0b1011. Set C
                else:
                    self.CVZN = self.CVZN & 0b11110111  # Clr C/ Mick, Aug 2018
                # else:
                #    self.CVZN = self.CVZN | 8 # 0b1000 C set?

                if X == 128:  # Signed overflow?
                    self.CVZN = self.CVZN | 4  # V set
                else:
                    self.CVZN = self.CVZN & 0b11111011  # V clear
                setZN(Res)

            if fun == 3:  # inc
                Res = (X + 1) % 256
                # Carry
                if X == 255:
                    self.CVZN = self.CVZN | 8  # Set C
                else:
                    self.CVZN = self.CVZN & 0b11110111  # Clear C
                # Overflow
                if X == 127:
                    self.CVZN = self.CVZN | 4  # Set V
                else:
                    self.CVZN = self.CVZN & 0b11111011  # Clear V
                setZN(Res)

            if fun == 4 or fun == 6:  # shr/shra
                Res = X >> 1
                if (fun == 6 and X >= 128) or (fun == 4 and self.CVZN & 8 != 0):
                    Res += 128
                self.CVZN = self.CVZN & 0b11110011  # Clear C abd V
                self.CVZN = self.CVZN | ((X << 3) & 8)  #
                setZN(Res)

            if fun == 5 or fun == 7:  # shla/rol
                Res = (2 * X) % 256
                self.CVZN = self.CVZN & 0b11110000
                if X >= 128:
                    self.CVZN = self.CVZN | 8
                    if fun == 7:
                        Res = Res | 1
                    if Res < 128 and fun == 5:
                        self.CVZN = self.CVZN | 4
                elif Res >= 128 and fun == 5:
                    self.CVZN = self.CVZN | 4
                setZN(Res)

            self.regs[Rd] = Res
            self.changePC(self.PC + 1)
            return

        if self.IR >> 5 == 0b101:  # memory
            load = (self.IR & 0b00010000) >> 4
            Rs = (self.IR & 12) >> 2
            Rd = self.IR & 3

            if load == 0b0001:  # ld
                # CocoIDE Hijack to test if Input address
                self.ipAdr = self.regs[Rs]

                # Generate interrupt in CocoIDE. If an Input address
                # returns the Input port value in self.ipVal,
                self.ipVal = None
                if self.parent:  # Is running under CocoIDE?
                    self.parent.event_generate("<<checkInPorts>>")
                # print("*",self.ipVal)
                if self.ipVal != None:
                    self.regs[Rd] = self.ipVal
                else:
                    self.regs[Rd] = self.memory[self.curPage][self.datamem[self.curPage]][self.regs[Rs]]

            else:  # st
                self.memory[self.curPage][self.datamem[self.curPage]][self.regs[Rs]] = self.regs[Rd]
                self.memChanged[self.curPage] += [self.regs[Rs]]

            self.changePC(self.PC + 1)
            return

        if ((self.IR & 0b11110000) >> 4) == 0b1111:  # ldc
            Rs = (self.IR & 12) >> 2
            Rd = self.IR & 3
            self.regs[Rd] = self.memory[self.curPage][0][self.regs[Rs]]
            self.changePC(self.PC + 1)
            return

        if self.IR >> 4 == 0b1100:  # stack
            ss = (self.IR & 12) >> 2
            Rd = self.IR & 3
            stsel = Rd  # selector for mark 4 architecture
            if ss == 0:  # push
                self.SP[stackPage] = (self.SP[stackPage] + 255) % 256
                self.memory[self.curPage][self.datamem[self.curPage]][self.SP[stackPage]] = self.regs[Rd]
                self.memChanged[self.curPage] += [self.SP[stackPage]]

            if ss == 1:  # pop
                self.regs[Rd] = self.memory[self.curPage][self.datamem[self.curPage]][self.SP[stackPage]]
                self.SP[stackPage] = (self.SP[stackPage] + 1) % 256

            if ss == 2:  # stsp or ldsa
                if args.v3:
                    self.SP[stackPage] = self.regs[Rd]
                else:  # mark 4 architecture, addsa
                    imop = self.memory[self.curPage][0][(self.PC + 1 + 256) % 256]
                    self.regs[Rd] = self.SP[stackPage] + imop
                    self.changePC(self.PC + 2)
                    return

            if ss == 3:
                if args.v3:  # ldsp
                    self.egs[Rd] = self.SP[stackPage]
                else:
                    if stsel == 0 or stsel == 1:
                        imop = self.memory[self.curPage][0][(self.PC + 1 + 256) % 256]
                        self.SP[stackPage] = ((1 - stsel) * self.SP[stackPage] + imop + 256) % 256
                        self.changePC(self.PC + 2)
                        return

                    if stsel == 2:  # pushall
                        chngMem = []
                        for Rd in (3, 2, 1, 0):
                            self.SP[stackPage] = (self.SP[stackPage] + 255) % 256
                            self.memory[self.curPage][self.datamem[self.curPage]][self.SP[stackPage]] = self.regs[Rd]
                            chngMem += [self.SP[stackPage]]
                        self.memChanged[self.curPage] += chngMem

                    if stsel == 3:  # popall
                        for Rd in (0, 1, 2, 3):
                            self.regs[Rd] = self.memory[self.curPage][self.datamem[self.curPage]][self.SP[stackPage]]
                            self.SP[stackPage] = (self.SP[stackPage] + 1) % 256
            self.changePC(self.PC + 1)
            return

        if self.IR >> 2 == 0b110100:  # ldi
            Rd = self.IR & 3
            imop = self.memory[self.curPage][0][(self.PC + 1 + 256) % 256]

            self.regs[Rd] = imop
            self.changePC(self.PC + 2)
            return

        if self.IR >> 4 == 0b1101:  # 0-op
            vvww = self.IR & 0b00001111

            if vvww == 4 or vvww == 5:
                self.HALT = True
                # print(format(self.cntr,"06d")+": "+"PC="+format(self.PC,"02x")+" <<< halt >>>")
                return

            if vvww == 6:  # jsr
                self.SP[stackPage] = (self.SP[stackPage] + 255) % 256
                self.memory[self.curPage][self.datamem[self.curPage]][self.SP[stackPage]] = (self.PC + 2 + 256) % 256
                self.changePC(self.memory[self.curPage][0][(self.PC + 1 + 256) % 256])
                self.memChanged[self.curPage] += [self.SP[stackPage]]
                return

            if vvww == 7:  # rts
                self.changePC(self.memory[self.curPage][self.datamem[self.curPage]][self.SP[stackPage]])
                self.SP[stackPage] = (self.SP[stackPage] + 1) % 256
                return

            if vvww == 10:  # crc
                temp = (self.PC + 1 + 256) % 256
                self.changePC(self.memory[self.curPage][self.datamem[self.curPage]][self.SP[stackPage]])
                self.memory[self.curPage][self.datamem[self.curPage]][self.SP[stackPage]] = temp
                return

            if vvww == 15:
                k = random.randint(0, 255)
                self.regs[0] = k
                self.changePC(self.PC + 1)
                return

            if vvww == 8:  # ioi = 0xD8
                ien = self.CVZN & 0b10000000
                if ien:
                    # PC onto stack
                    if not interrupt:  # If software ioi
                        self.changePC(self.PC + 1)  # Update PC to point to next instruction
                    self.SP[0] = (self.SP[0] + 255) % 256  # dec SP[0]
                    self.memory[0][self.datamem[0]][self.SP[0]] = self.PC
                    self.memChanged[0] += [self.SP[0]]
                    self.changePC(self.memory[stackPage][0][0xf0 + intvector * 2])  ## int vector = 0 -> F0, F2, F4 etc

                    # PS onto stack
                    self.SP[0] = (self.SP[0] + 255) % 256
                    self.memory[0][self.datamem[0]][self.SP[0]] = self.CVZN
                    self.memChanged[0] += [self.SP[0]]
                    self.CVZN = self.memory[stackPage][0][0xf1 + intvector * 2]  # intvector address +1
                    self.curPage = 0  # ISR for ioi always on page 0
                else:
                    self.changePC(self.PC + 1)  # just ignore!
                return

            if vvww == 11:  # osix = 0xDB
                # Interrupts enabled?
                ien = self.CVZN & 0b10000000
                if ien:
                    # Get new SR val from osix operand, and interupt enable from vector 0
                    self.changePC(self.PC + 1)  # point PC to operand
                    # store new PS value. Set Interrupt bit 7 from vector 0 (@ 0xf1)
                    newPS = self.memory[self.curPage][0][self.PC] | (self.memory[0][0][0xf1] & 0b10000000)
                    # print(format(newPS, "0b"))

                    # PC onto stack
                    self.changePC(self.PC + 1)  # Update PC to point to next instruction
                    self.SP[stackPage] = (self.SP[stackPage] + 255) % 256  # dec current SP
                    self.memory[stackPage][self.datamem[stackPage]][self.SP[stackPage]] = self.PC
                    self.memChanged[stackPage] += [self.SP[stackPage]]
                    self.changePC(self.memory[stackPage][0][0xf0])  ## int vector always 0 for osix

                    # PS onto stack
                    self.SP[stackPage] = (self.SP[stackPage] + 255) % 256
                    intEnable = self.memory[stackPage][0][0xf1] & 0b10000000  # new SP with interrupt bit from vector
                    self.memory[stackPage][self.datamem[stackPage]][self.SP[stackPage]] = self.CVZN
                    self.memChanged[stackPage] += [self.SP[stackPage]]
                    self.CVZN = newPS | intEnable  # set Int enable state
                else:
                    self.changePC(self.PC + 2)  # skip if not enabled
                return

            if vvww == 9:  # rti = 0xD9
                # PS from stack
                self.CVZN = self.memory[stackPage][self.datamem[stackPage]][self.SP[stackPage]]
                self.SP[stackPage] = (self.SP[stackPage] + 1) % 256

                # PC from stack
                self.PC = self.memory[stackPage][self.datamem[stackPage]][self.SP[stackPage]]
                self.SP[stackPage] = (self.SP[stackPage] + 1) % 256

                return

            if vvww >= 11:
                EP("Illegal opcode: " + str(self.IR), term=False)

        # print("IR=", self.IR)
        if self.IR >> 4 == 14:  # branches
            cccc = self.IR & 0b00001111
            reverse = cccc & 1
            ccc = cccc >> 1
            C = (self.CVZN & 0b00001111) >> 3
            V = ((self.CVZN & 0b00001111) >> 2) & 1
            Z = ((self.CVZN & 0b00001111) >> 1) & 1
            N = (self.CVZN & 0b00001111) & 1
            # print("CVZN=", C, V, Z, N)
            if ccc == 0:
                dcsn = Z
            elif ccc == 1:
                dcsn = C
            elif ccc == 2:
                dcsn = N
            elif ccc == 3:
                dcsn = V
            elif ccc == 4:
                dcsn = C & (~Z) & 1
            elif ccc == 5:
                dcsn = ~(N ^ V) & 1
            elif ccc == 6:
                dcsn = (~Z) & ~(N ^ V) & 1
            elif ccc == 7:
                dcsn = 1

            dcsn = reverse ^ dcsn
            if dcsn != 0:
                self.changePC(self.memory[self.curPage][0][self.PC + 1])
            else:
                self.changePC(self.PC + 2)
            return

        if ((self.IR >> 4) == 0b1111) and (self.arch == "vn"):
            if args.save:  # not ldc, we are having a restore point
                savepnt = self.IR & 0b1111
                if savepnt > len(savestat) - 1:
                    EP("Illegal opcode: " + str(self.IR), term=False)
                    self.changePC(self.PC + 1)
                    savepnt = 0
                if savestat[savepnt] != []:
                    (adr1, adr2, state) = savestat[savepnt]
                    while adr1 <= adr2:
                        self.memory[self.curPage][0][adr1] = state[0]
                        self.memChanged[self.curPage] += [adr1]
                        adr1 += 1
                        state = state[1:]
                self.changePC(self.PC + 1)
                if self.traceprint:
                    if self.PC not in self.IP:
                        self.IP += [self.PC]
            else:
                self.changePC(self.PC + 1)
                EP("Illegal opcode: " + str(self.IR), term=False)

    def run(self):
        self.regs = [0, 0, 0, 0]
        self.PC = 0
        self.SP = [0] * pages
        self.IR = 0
        self.IP = []
        self.CVZN = 0x0
        self.BP = []
        self.HALT = False
        self.running = False
        self.traceprint = False
        self.cntr = 0
        self.pretend = True  # Pretend that standard.mlb macros are real machine instructions
        self.changePC(0x00)
        self.HALT = False
        # self.cntr=0
        self.running = True
        # Run to
        while (not self.PC in self.BP) and (not self.HALT) and self.PC < 255:  # Run to next Break point
            self.step()
        # print("PC= ", self.PC)
        # self.cntr += 1  # No of steps keep count?
        # print("Run Stopped")
        self.running = False


########## End of Emulator class
def EP(s, term=True):
    sys.stderr.write(s + '\n')
    if term:
        quit(-1)


########## Command Line options
parser = argparse.ArgumentParser(description='CdM-8 Emulator v1.0')
parser.add_argument('-r', dest='run', action='store_const', const=True, default=False, help="run image and quit")
parser.add_argument('-l', dest='lst', action='store_const', const=True, default=False,
                    help="display assembler listing (FILE.lst)")
parser.add_argument('-w', dest='trace', default="",
                    help="comma-separated list of trace snapshots (format/location): [fmt:]addr[,[fmt:]addr...] with  fmt = x (hex) | d (decimal) | c (ASCII);  addr(hex) = xx (single address) | xx-xx (address range)")
parser.add_argument('-s', dest='save', default="", help="save for restore points (chk): chk:xx[-xx],chk:xx[-xx] ...")
parser.add_argument('-v3', dest='v3', action='store_const', const=True, default=False,
                    help="assume CdM-8 Mark 3 instruction set")
parser.add_argument('-i', dest='ipoints', default="",
                    help="comma-separated list of program execution addresses xx (hex) at which to display trace snapshots: xx[,xx...]")
parser.add_argument('-a', dest='arch', default="vn", help="Architecture: default vn (Von Neuman), hv (Harvard)")
if __name__ == "__main__":
    parser.add_argument('filename', type=str, const=None, default="", help='memory_image_file[.img]')
args = parser.parse_args()

if __name__ == "__main__":
    try:
        filename = args.filename
        if filename[-4:] == ".img":
            filename = filename[:-4]
        CDM8Emu().run()
    except:
        print("Bad filename or file")

