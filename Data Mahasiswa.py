#   Program Input Variabel  #

print("""
|---------------------------------------------------|                                                   
|           Program Input Data Mahasiswa            |
|      ======================================       |                                          
|---------------------------------------------------|                                                   
""")

import json
x = 1
DataInputMahasiswa = {}
while x > 0:
        print("\n================================================================================")
        print("\nSelamat datang di program sederhana ini. \nSilahkan masukkan data diri anda")
        answer = input("Lanjut untuk memasukkan data anda? (Yes/No) ")
        print("\n================================================================================")

        if answer == "yes" or answer == "Yes":
            print("\n================================================================================")
            Nama = input("Masukkan Nama = ")
            NIM = int(input("Masukkan NIM = "))
            SMT = int(input("Masukkan Tahun Semester Mahasiswa = "))
            TinggiBadan = float(input("Masukkan Tinggi Badan dalam cm = "))
            BeratBadan = float(input("Masukkan Berat Badan Mahasiswa = "))
            Umur = int(input("Masukkan Umur = "))
            Hobi = input("Masukkan Hobi Mahasiswa = ")
            print("\n================================================================================")
            
            Data = {"Nama Mahasiswa": Nama,
                    "NIM Mahasiswa": NIM,
                    "Tahun Semester Mahasiswa": SMT,
                    "Tinggi Badan Mahasiswa": TinggiBadan,
                    "Berat Badan Mahasiswa": BeratBadan,
                    "Umur Mahasiswa": Umur,
                    "Hobi Mahasiswa": Hobi}

            print("\nDiperoleh data Mahasiswa sebagai berikut : ")
            print(json.dumps(Data, indent=7))

        else:
            print("\n================================================================================")
            print("\nProgram telah selesai berjalan. Terima kasih telah mencoba :D")
            print("\n================================================================================")
            break