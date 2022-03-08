asect 0x00
jsr func
inc r3
halt


# some really far code
asect 0xf123
func:
ldi r0, 0xde
ldi r1, 0xad
ldi r2, 0xbe
ldi r3, 0xee
rts

end