def awal():
    print(" === Selamat Datang di ATM Bersama === ")
    print("   ===   Silahkan Pilih Bahasa   === ")


# Saldo Awal 2,5jt
saldo = 2500000

# main
awal()

bahasa = input(" [Indonesia / English] : ")

# JIKA PILIH  BAHASA INDONESIA
if bahasa == "Indonesia" or bahasa == "indonesia" or bahasa == "INDONESIA":
    # Validasi PIN
    cekPin = 0
    while cekPin == 0:
        pin = int(input("Masukkan PIN Anda : "))
        if pin == 190322:
            cekPin = 1
        else:
            print("PIN Anda Salah ! Coba Lagi \n")

    print(" \t == Menu == ")
    print(" 1. Tarik Tunai ")
    print(" 2. Cek Saldo ")
    print(" 3. Transfer Uang ")
    print(" 4. Setor Tunai")
    print(" 5. Keluar ")
    pilih_menu = 0
    while pilih_menu != 5:
        pilih_menu = int(input("Masukkan Pilihan Anda : "))
        # Pilihan 1
        if pilih_menu == 1:
            jumlah_tarik = int(input("\nMasukkan Nominal yang ingin ditarik : "))
            if jumlah_tarik < saldo:
                saldo -= jumlah_tarik
                print(f"Berhasil Tarik Tunai Sejumlah Rp {jumlah_tarik} \n")
            elif jumlah_tarik > saldo:
                print("Maaf Uang Anda Kurang! \n")
        # pilihan 2
        if pilih_menu == 2:
            print(f"\nSisa Saldo Anda Rp {saldo} \n")

        #pilihan 3
        if pilih_menu == 3:
            rek_tujuan = int(input(" \nNo. Rekening Tujuan : "))
            nominal = int(input("Nominal Transfer : "))
            if nominal < saldo:
                saldo -= nominal
                print(f"\nBerhasil Transfer Sebesar Rp {nominal} ke No. Rekening : {rek_tujuan}\n")
            elif nominal > saldo:
                print(f"\nGagal Transfer, Saldo Anda Kurang! \n")

        #pilihan 4
        if pilih_menu == 4:
            setor = int(input("\nJumlah Setoran : "))
            saldo += setor
            print(f"Berhasil Setor Tunai Sejumlah Rp {setor}\n")

    print("Terimakasih telah bertransaksi di ATM ini :) ")


# JIKA PILIH  BAHASA INGGRIS
elif bahasa == "English" or bahasa == "english" or bahasa == "ENGLISH":
    # Validasi PIN
    cekPin = 0
    while cekPin == 0:
        pin = int(input("Entry Your PIN : "))
        if pin == 190322:
            cekPin = 1
        else:
            print("Your PIN is wrong! Try Again \n")

    print(" \t == Menu == ")
    print(" 1. Cash Withdrawal ")
    print(" 2. Balance Check ")
    print(" 3. Money Transfer ")
    print(" 4. Cash Deposit ")
    print(" 5. Exit ")
    pilih_menu = 0
    while pilih_menu != 5:
        pilih_menu = int(input("Enter Your Options : "))
        # Pilihan 1
        if pilih_menu == 1:
            jumlah_tarik = int(input("\nEnter the Nominal you want to Withdraw : "))
            if jumlah_tarik < saldo:
                saldo -= jumlah_tarik
                print(f"Successfully Withdraw Cash a Certain Amount Rp {jumlah_tarik} \n")
            elif jumlah_tarik > saldo:
                print("Sorry you're less money! \n")
        # pilihan 2
        if pilih_menu == 2:
            print(f" \nRest of Your Balance Rp {saldo} \n")

        #pilihan 3
        if pilih_menu == 3:
            rek_tujuan = int(input(" \nDestination Account Number : "))
            nominal = int(input("Nominal Transfer : "))
            if nominal < saldo:
                saldo -= nominal
                print(f"\nSuccessful Transfer Amount Rp {nominal} to Account Number : {rek_tujuan}\n")
            elif nominal > saldo:
                print(f"\nFailed Transfer, Your Balance Is Less! \n")

        # pilihan 4
        if pilih_menu == 4:
            setor = int(input("\nDeposit Amount : "))
            saldo += setor
            print(f"Successfully Deposit Cash a Certain Amount Rp {setor}\n")
    print("Thank you for transacting at this ATM. :) ")

else:
    print("Hanya ada bahasa Indonesia dan Englsih!")