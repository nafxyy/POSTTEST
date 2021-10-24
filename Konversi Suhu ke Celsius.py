#   Program Konversi Suhu Menjadi Celsius   #

print("""
|---------------------------------------------------|                                                   
|         Selamat Datang di Konversi Suhu           |
|      ======================================       |                                          
|---------------------------------------------------|                                                   
""")

print("""
|---------------------------------------------------|
|       1. Konversi Fahrenheit ke Celsius           |
|---------------------------------------------------|
""")

x = 1
while x > 0 :
    print("===============================================================")
    opsi =  input("Fahrenheit, Reamur, Kelvin. \nSilahkan pilih suhu yang ingin di konversikan menjadi Celsius = ")
    if opsi == "Fahrenheit" or opsi == "fahrenheit":
        Fahrenheit = float(input("Masukkan suhu Fahrenheit = "))
        Celsius = (5 / 9) * (Fahrenheit - 32)
        print("Suhu Celsius yang dihasilkan = ", Celsius, "C")

        choice = input("Ingin mengulang konversi? (Yes/No) ")
        if choice == "Yes":
            continue
        else:
            print("Konversi Fahrenheit Berhenti. \nTerima Kasih")
            print("==============================================================")
            break

    elif opsi == "Reamur" or opsi == "reamur":
        print("""
            |---------------------------------------------------|     
            |       2. Konversi Reamur ke Celsius               |
            |---------------------------------------------------|
            """)
        Reamur = float(input("Masukkan Suhu Reamur = "))
        Celsius = (5 / 4) * Reamur
        print("Suhu Celsius yang dihasilkan = ", Celsius, "C")

        choice = input("Ingin mengulang konversi? (Yes/No) ")
        if choice == "Yes":
            continue
        else:
            print("Konversi Reamur Berhenti. \nTerima Kasih")
            print("============================================================")

            break

    elif opsi == "Kelvin" or opsi == "kelvin":
        print("""
            |---------------------------------------------------|
            |       3. Konversi Kelvin ke Celsius               |  
            |---------------------------------------------------|
            """)
        Kelvin = float(input("Masukkan Suhu Kelvin = "))
        Celsius = Kelvin - 273
        print("Suhu Celsius yang dihasilkan = ", Celsius, "C")
        print("===============================================================")

        choice = input("Ingin mengulang konversi? (Yes/No) ")
        if choice == "Yes":
            continue
        else:
            print("Konversi Kelvin Berhenti. \nTerima Kasih")
            print("==========================================================")
            break

    else:
        print("===============================================================")
        print("Keyword tidak ditemukan. Silahkan coba lagi")
        print("===============================================================")
        
        choice_1 = input("\nIngin mengulang konversi? (Yes/No) ")
        if choice_1 == "Yes":
            continue
        else:
            print("\n===============================================================")
            print("\nProgram Berakhir. Terima Kasih telah mampir :D")
            print("\n===============================================================")
            break

    

