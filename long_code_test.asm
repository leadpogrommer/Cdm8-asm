asect 0x00

ldi r0, 11
jsr fib
halt


# some really far code
asect 0xf123
fib:
push r3
ldi r3, 2
cmp r0, r3
blt fibend

dec r0
push r0
jsr fib
move r0, r3
pop r0

dec r0
push r0
jsr fib
add r0, r3
pop r0
move r3, r0


fibend:
pop r3
rts

end