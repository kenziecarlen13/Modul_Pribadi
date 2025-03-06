# buatlah variabel  dengan nama:
# iniString := berjeniskan string(), diisi dengan namamu
#  iniInt := berjeniskan int(), diisi dengan umurmu
# iniFloat := berjeniskan float(), diisi dengan tinggi satuan meter


# kerjaain di sini brok 





#ini jangan di rubah rubah!!
if __name__=="__main__":
# lalu uncomment kodeline di bawah ini untuk menjalankan progam! Happy coding...
    # print(f"halo nama saya {iniString} berumur {iniInt}, dengan tinggi badan, {iniFloat} meter.\nsalam kenal!")




# gausa peduliin line code ini
    import cek
    import subprocess
    result = subprocess.run(["python", "cek.py"], capture_output=True, text=True)
    print(result.stdout)