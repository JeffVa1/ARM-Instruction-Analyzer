import baseconvert as bc

def arm_bin_analysis(binary_str):

    opcode_dict = {"0000":"and", "0001":"eor", "0010":"sub", "0011":"rsb",
                   "0100":"add", "0101":"adc", "0110":"sbc", "0111":"rsc",
                   "1000":"tst", "1001":"teq", "1010":"cmp", "1011":"cmn",
                   "1100":"orr", "1101":"mov", "1110":"bic", "1111":"mvn", }

    leading = binary_str[0:6]
    i_bit = binary_str[6]
    opcode = binary_str[7:11]
    s_bit = binary_str[11]
    rn = binary_str[12:16]
    rd = binary_str[16:20]
    immediate_val = binary_str[24:32]
    rm = binary_str[28:32]

    instr = opcode_dict[opcode]
    rn_val = bc.base(rn, 2, 10, string=True)
    rd_val = bc.base(rd, 2, 10, string=True)
    im_val = bc.base(immediate_val, 2, 10, string=True)
    rm_val = bc.base(rm, 2, 10, string=True)

    rm_val = "r" + rm_val
    rn_val = "r" + rn_val
    rd_val = "r" + rd_val

    i_info = ""
    if i_bit == "1":
        i_info = "im val"
    if i_bit == "0":
        i_info = "rm val"

    s_info = ""
    if s_bit == "1":
        s_info = "set NZCV"

    print()
    bin_instr = "BINARY INSTRUCTION"
    print(f"{bin_instr:^40}")
    print(f"{binary_str:^40}")

    print()
    bit_analy = "BIT ANALYSIS"
    print(f"{bit_analy:^40}")
    print(f"Leading Bits: {leading:>12}")
    print(f"I Bit: {i_bit:>14}{i_info:>18}")
    print(f"Opcode: {opcode:>16}{instr:>15}")
    print(f"S Bit: {s_bit:>14}{s_info:>18}")
    print(f"RN Bits: {rn:>15}{rn_val:>15}")
    print(f"RD Bits: {rd:>15}{rd_val:>15}")
    print(f"Immediate Value: {immediate_val:>11}{im_val:>11}")
    print(f"RM Bits: {rm:>15}{rm_val:>15}")


def char_to_hex_num(hex_str):
    final_str = []
    hex_dict = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
    hex_str = [char for char in hex_str]

    input_hx_str = "INPUT HEX VALUE"
    print(f"{input_hx_str:^40}")
    print(hex_str)
    for char in hex_str:
        if char in hex_dict:
            final_str.append(str(hex_dict[char]))
        else:
            final_str.append(char)

    return [int(i) for i in final_str]


def main():

    quit = False

    while not quit:
        print()
        print("========================================")
        print()

        print("Input base (2-16): ")
        in_base = int(input())
        while in_base > 16 or in_base < 2:
            print("INVALID BASE... TRY AGAIN: ")
            in_base = int(input())

        print("Output base (2-16):")
        out_base = int(input())
        while out_base > 16 or out_base < 2:
            print("INVALID BASE... TRY AGAIN: ")
            out_base = int(input())

        print("Input Value: ")
        base_val = input()

        #char_to_num converts each char in the hex_val string into its decimal representation and stores as array
        input_array = char_to_hex_num(base_val)

        #final_str is a list of numbers that make up the hex code.
        #bc.base(input value, input base, output base)
        conv = bc.base(input_array, in_base, out_base, string=True)

        if len(conv) < 32:
            print("CONVERTED VALUE")
            print(conv)
            print()
            print("CONVERSION NOT LONG ENOUGH FOR ARM INSTRUCTION - ", len(conv))
        else:
            if len(conv) > 32:
                print("CONVERSION TOO LONG FOR ARM INSTRUCTION")
            else:
                #funtion that isolates and prints the bit analysis
                arm_bin_analysis(conv)

        print("Continue? (y/n)")
        to_continue = input()
        if to_continue == "n":
            quit = True

main()