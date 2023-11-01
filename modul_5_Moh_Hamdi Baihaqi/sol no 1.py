print("List 1 : 13 Hewan bersayap ")
List1 = [input(list()),input(list()),input(list()),input(list()),input(list()),input(list()),input(list()),input(list()),input(list()),input(list()),input(list()),input(list()),input(list())]
print("List 2 : 5 Hewan berkaki 2 ")
List2 = [input(list()),input(list()),input(list()),input(list()),input(list())]
print("List 3 : Nama teman terdekat anda ")
List3 = [input(list()),input(list()),input(list()),input(list()),input(list())]
print("List 4 : 5 Tanggal lahir teman kamu ")
List4 = [int(input(list())),int(input(list())),int(input(list())),int(input(list())),int(input(list()))]
print("List 5 : 13,31,2,19,96")
List5 =[int(input(list())),int(input(list())),int(input(list())),int(input(list())),int(input(list()))]

# Output 1
print("output 1")
print(List1)
print(List4)
print(" Gabungannya = ")
print(List1[1:6] + List4)
print()

# Output 2
print("output 2")
print(List3)
List3[4] = (input("update index 4 : "))
print(List3)
print()

# Output 3
print("Output 3")
print(List5)
del List5 [2] 
del List5 [4]
print(List5)
print()

# Output 4
print("output 4")
gabungan = List4 + List5
print(gabungan)
print(max(gabungan))
print(min(gabungan))
print()