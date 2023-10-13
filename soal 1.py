# Definisikan tampilan angka
digit_0 = [
    "  #####  ",
    " #     # ",
    "#       #",
    "#       #",
    "#       #",
    " #     # ",
    "  #####  "
]

digit_1 = [
    "    #    ",
    "   ##    ",
    "    #    ",
    "    #    ",
    "    #    ",
    "    #    ",
    "  #####  "
]

digit_6 = [
    "  ####   ",
    " #       ",
    "#        ",
    "#  ####  ",
    "#      # ",
    " #     # ",
    "  ####   "
]

# Definisikan fungsi untuk mencetak NIM
def print_nim(nim):
    # Pisahkan NIM menjadi angka-angka
    nim_digits = [int(digit) for digit in str(nim)]

    # Tampilkan NIM 
    for row in range(7):
        for digit in nim_digits:
            if digit == 0:
                print(digit_0[row], end="")
            elif digit == 1:
                print(digit_1[row], end="  ")
            elif digit == 6:
                print(digit_6[row], end="  ")
            else:
                print("   ", end="  ")
        print()  # Pindah ke baris berikutnya

# NIM terakhir Anda adalah 160
nim_terakhir = 160

# Tampilkan NIM 
print_nim(nim_terakhir)
