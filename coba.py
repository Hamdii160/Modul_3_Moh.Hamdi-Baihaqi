# Definisikan tampilan angka 0-9 dalam bentuk ASCII art
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

# Angka NIM terakhir Anda adalah 160
nim_terakhir = [1, 6, 0]

# Definisikan fungsi untuk mencetak angka dalam bentuk ASCII art secara vertikal
def print_nim_digit_vertically(digit):
    for row in digit:
        print(row)

# Cetak angka NIM terakhir dalam bentuk ASCII art secara vertikal
for digit in nim_terakhir:
    if digit == 0:
        print_nim_digit_vertically(digit_0)
    elif digit == 1:
        print_nim_digit_vertically(digit_1)
    elif digit == 6:
        print_nim_digit_vertically(digit_6)
    print()  # Tambahkan baris kosong antara angka
