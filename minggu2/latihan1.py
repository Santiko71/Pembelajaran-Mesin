# TAUFIK NUR SANTIKO
# A11.2022.14184
# PEMBELAJARAN MESIN

print('PYTHON BASIC-1\n')
print("Hello World!@#!#!$")
print("test")

print()

print('Latihan: The print() function')
print("Hello, Python!")
print("Taufik")
print('Taufik')

print()

print('Formatting dengan Special Character')
print("Saya sudah sarapan tadi pagi\n dan nanti siang makan lagi")
print("Saya sudah sarapan tadi pagi\t dan nanti siang makan lagi")

print()

print("nama saya \"Taufik\"")
print("\"")
print("satu.","dua.","tiga.")
print("Nama saya","Taufik", end=" ")
print("Nur Santiko")
print("satu","dua","tiga", sep=", ")

print()

print('Latihan: The print function\n')
print('Programming', 'Essentials', 'in', sep='***', end='...')
print('Python')

print()

print('Latihan: Formatting the output')
print("    *    "*2)
print("   * *   "*2)
print("  *   *  "*2)
print(" *     * "*2)
print("***   ***"*2)
print("  *   *  "*2)
print("  *   *  "*2)
print("  *****  "*2)

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n"*2)

print()

print('Literal')
print("2"*2)
print(2*2)

print(type("2"))
print(type(2))

print()

print('Integers vs Floats')
print(5, "mempunyai tipe", type(5))
print(.5, "mempunyai tipe", type(.5))

print()

print('Penulisan Float dan Integer')
print('I\'m Monty Python')

print()

print('Boolean')
print(True)
print(False)

print(4>2)
print(3>4)

print()

print('Latihan: Python literals - strings')
print('"I\'m"\n""learning""\n"""Python"""')

print("""
"I'm"
""learning""
\"""Python""\"
""")

print()

print('Operator')
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3.)
print(2. ** 3)

print()
print(10 / 3)
print(10 // 3)

print()
print(6 / 3.)
print(6 // 3.)

print()
print(-4 + 4)
print(-4. + 8)

print()

2 + 3 *5

print()

print(9 % 6 % 2)
print(9 % 6)
print(3 % 2)

print()
print(2 ** 2 ** 3)
print(2 ** 2)
print(2 ** 8)

print()
print((5 * ((25 % 13)+100) / (2 * 13)) // 2)

print()

print('Variabel')
var = 1
print(var)

print()
a=2.
b=3.
c=(a**2 + b**2) ** 0.5
print("c = ", c)

print()

print('Latihan: Variables')
Darjo = 2
Darno = 5
Waginem = 6
total_apel = Darjo + Darno + Waginem
pengurangan_apel = Darjo - Darno - Waginem
perkalian_apel = Darjo * Darno * Waginem

print('Darjo memiliki ' + str(Darjo) + ' apel', 'Darno memiliki ' + str(Darno) + ' apel', 'Waginem memiliki ' + str(Waginem) + ' apel', sep=', ')
print('Apel mereka adalah ' + str(total_apel))
print('Pengurangan apel mereka adalah ' + str(pengurangan_apel))
print('Perkalian apel mereka adalah ' + str(perkalian_apel))

print()

print('Latihan: Variables: a simple converter')
kilometer = 12.25
mil = 7.38

miles_to_kilometers = mil * 1.61
kilometers_to_miles = kilometer / 1.61

print(mil, "1 mil adalah", round(miles_to_kilometers, 2), "kilometer")
print(kilometer, "1 kilometer adalah", round(kilometers_to_miles, 2), "mil")

print()

print('Latihan: Operators and Expressions')
x = input('Masukan angka = ')
x = float(x)
y = 3 * (float(x) ** 3) - 2 * (float(x) ** 2) + 3 * float(x) - 1 

print('y =', y)

print()

print('Exercise')

var = 2
var = 3
print(var) # outputnya angka 3 

print()

print("Nama variabel mana yang ilegal?: ")

print("my_var")
print("m")
print("101")
print("averylongvariablename")
print("m101")
print("m 101")
print("Del")
print("del")  

print("Jadi jawabannya adalah : ")

print("101 karena dimulai dengan angka.")
print("m 101 karena mengandung spasi.")
print("Del dan del karena merupakan kata kunci bawaan dalam Python.")

print()

print("Apa Outputnya?")
a = '1'
b = "1"
print(a + b)

print()

a = 6
b = 3
a /= 2 * b
print(a)

print()

print("Latihan Memberi baris comment") #
#test
print("Hai...") 
#test1
#test2

print()

print("How To Talk To Computer") #
print("Katakan sesuatu...")
sesuatu = input()
print("mmmmm", sesuatu, " Oke")

print()

print("Latihan Type Casting") #
angka = float(input("Masukan Angka : "))
print("Pangkat duanya adalah ", angka**2)

print()

print("Latihan Replication")#
print("+" + 10*"-" + "+")
print(("|" + 10*" " + "|\n") * 5, end="")
print("+" + 10*"-" + "+")

print()

print("Latihan Simple dan output")#
# Masukkan nilai a dalam float
a = float(input("Masukkan nilai a: "))

# Masukkan nilai b dalam float
b = float(input("Masukkan nilai b: "))

# hitung hasil penambahan disini
penambahan = a + b

# hitung hasil pengurangan disini
pengurangan = a - b

# hitung hasil perkalian disini
perkalian = a * b

# hitung hasil pembagian disini
pembagian = a / b

# Menampilkan hasil
print("Hasil penambahan:", penambahan)
print("Hasil pengurangan:", pengurangan)
print("Hasil perkalian:", perkalian)
print("Hasil pembagian:", pembagian)

print()

print("Operator dan expressions")#
import math

# Masukkan nilai x
x = float(input("Masukkan nilai x: "))

# Hitung nilai y menggunakan rumus yang diberikan
y = math.sqrt(1 / (x**2 + 1))

# Tampilkan hasil
print("x =", x)
print("y =", y)

print()

print("\"I'm\"\n \"\"learning\"\"\n \"\"\"Python\"\"\"\n")

print()