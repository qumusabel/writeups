op_funcs   = ['mov', 'add', '_sub', '_div', 'mul', 'xor', 'ldb', 'stb', 'cmp', 'ig', 'ige', 'ile', 'jmp', 'jit', 'jif', '_int']
op_funcs16 = ['mov16', 'add16', 'sub16', 'div16', 'mul16', 'xor16', 'ldb16', 'stb16', 'cmp16', 'ig16', 'ige16', 'ile16']

# load the bytecode. in this case, only first ~50 bytes contain the code
with open('b1.file', 'rb') as f:
    bytecode = f.read()[:0x50]
rip = 0


def get_arg(count, byte):
    global rip

    # it's a register if the second bit of the arg desc.
    if (((byte >> 1) & 0b111) >> count) & 1:
        arg = bytecode[rip+1]
        rip += 1

        return 'REG %i' % arg

    # it's a constant if it's the second arg and the first bit is 1
    elif count == 1 and (byte >> 1) & 4:
        if byte & 1:
            arg = (bytecode[rip+2] << 8) + bytecode[rip+1]
            rip += 2
        else:
            arg = bytecode[rip+1]
            rip += 1

        return '%i (0x%x)' % (arg, arg)

    # it's a pointer
    else:
        arg = (bytecode[rip+2] << 8) + bytecode[rip+1]
        rip += 2

        return 'PTR 0x%04x' % arg


while True:
    byte = bytecode[rip]
    print('0x%04x | ' % rip, end='') # print address


    # two arguments
    if (byte >> 4) < 0xc:
        # if the LSB of the opcode is 1, use 16-bit cmds
        if byte & 1:
            op_set = op_funcs16
        else:
            op_set = op_funcs

        # get two arguments
        args = get_arg(0, byte), get_arg(1, byte)
        args = '{}, {}'.format(*args)

    # one argument (jmp, _int)
    else:
        op_set = op_funcs
        args = get_arg(1, byte)
        args = '{}'.format(args)

    
    # find the opcode
    try:
        cmd = op_set[byte >> 4]
    except:
        cmd = 'invalid'

    print('{} {}'.format(cmd, args)) # print disassembly


    rip += 1

