asect 0x00
stv r1, 127

macro tes/0
xor r0, r0
xor r3, r3
mend

macro tes2/0

xor r1, r1
tes
xor r2, r2
mend


ldi r1, 228
tes2
stv r1, 128
halt
end













