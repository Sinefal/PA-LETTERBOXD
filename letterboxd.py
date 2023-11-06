import os
User = {
    "Admin" : "admin"
}
Pass = {
    "Admin" : "admin"
}

def menu():
    print("""
SELAMAT DATANG DI LETTERBOXD
[1] Sign In
[2] Register
[3] Exit""")
    pilih1=int(input("Pilih opsi(1/2/3): "))
    os.system('cls')
    if pilih1 == 1 :
        sign_in()
    elif pilih1 == 2 :
        regist()

def regist():
    regist_username=input("Buat Username : ")
    regist_password=input("Buat Password : ")
    User.update({"User1":regist_username})
    Pass.update({"User1":regist_password})
    os.system('cls')
    sign_in()
    
def sign_in():
    username=input("Masukkan Username : ")
    password=input("Masukkan Password : ")
    os.system('cls')
    if username == User.get("Admin") and password == Pass.get("Admin") :
        admin()

def admin():
    print("""[1] Lihat Review Film
[2] Beri Review Film""")
    
menu()
