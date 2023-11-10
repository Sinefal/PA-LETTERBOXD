import os

cinema = {
    'Interstellar': {
        'review': [
            {
                'username': "user",
                'rating': 10,
                'comment': "Mahakarya dari Christopher Nolan"
            }
        ]
    },
    'Blade Runner 2049': {
        'review': [
            {
                'username': "Ryan Gosling",
                'rating': 10,
                'comment': "He's literally me fr"
            },
            {
                'username': "user",
                'rating': 2,
                'comment': "Ngantuk coy"
            }
        ]
    },
    'Avengers: Infinity War': {
        'review': [
            {
                'username': "user",
                'rating': 2,
                'comment': "Pilem opo iki"
            },
            {
                'username': "Ryan Gosling",
                'rating': 2,
                'comment': "I drive"
            }
        ]
    }
}

akun_admin = {
    "admin" : "admin"
}

akun_user = {
    "user" : "user",
    "Ryan Gosling" : "me"
}

def sign_in():
    gagal = 0
    while gagal < 3 :
        username=input("Masukkan Username : ")
        password=input("Masukkan Password : ")
        os.system('cls')
        if username in akun_admin.keys() and password in akun_admin.values() :
            print("Sign in berhasil!")
            while True :
                konfirmasi=input("Masuk ke Letterboxd? Konfirmasi(y) / Cancel(n) : ")
                os.system('cls')
                if konfirmasi.lower() == "n":
                    return main()
                elif konfirmasi.lower() == "y":
                    return menu_admin()
                else:
                    print("input tidak valid!")
        elif username in  akun_user.keys() and password in akun_user.values() :
            print("Sign in berhasil!")
            while True :
                konfirmasi=input("Masuk ke Letterboxd? Konfirmasi(y) / Cancel(n) : ")
                os.system('cls')
                if konfirmasi.lower() == "n":
                    return main()
                elif konfirmasi.lower() == "y":
                    return menu_user(username)
                else:
                    print("Input tidak valid!")
        else :
            gagal += 1
            print("Username atau password salah!")
        if gagal == 3:
            print("Upaya masuk terlalu sering. Coba lagi nanti!")

# Fungsi register akun
def regist():
    while True :
        new_username = input("Username baru : ")
        if new_username in akun_user.keys() or new_username in akun_admin.keys() :
            print("Username sudah digunakan!")
        else :
            break
    new_password=input("Password baru : ")
    while True :
        konfirmasi = input("Buat akun? Konfirmasi(y) / Cancel(n) : ")
        os.system('cls')
        if konfirmasi.lower() == "y" :
            akun_user.update({new_username : new_password})
            print("Akun berhasil dibuat!")
            return main()
        elif konfirmasi.lower() == 'n':
            return main()
        else :
            print("Input tidak valid!")

def showList():
    if not cinema:
        print("---Tidak ada film tersedia---")
        return

    for i, film in enumerate(cinema):
        print(f"{i + 1}. {film}")

# Fungsi untuk menampilkan review film
def admin_lihat_review():
    try:
        showList()
        tunjuk = int(input("Pilih nomor film (0 untuk kembali): "))
        tunjuk -= 1
        os.system('cls')
        if tunjuk == -1 :
            return menu_admin()
        elif 0 <= tunjuk < len(cinema):
            judul = list(cinema.keys())[tunjuk]
            review = cinema[judul]['review']
            if review:
                print(f"Review untuk {judul}:")
                print("--------------------------------------------------------")
                for ulasan in review:
                    print(f"From    : {ulasan['username']}")
                    print(f"Rating  : {ulasan['rating']}")
                    print(f"Comment : {ulasan['comment']}")
                    print()
                return admin_lihat_review()
            else:
                print("Tidak ada review untuk film ini")
                return admin_lihat_review()
        else:
            print("Film tidak ditemukan")
            return admin_lihat_review()
    except ValueError:
        os.system("cls")
        print("Input tidak valid!")
        return admin_lihat_review()
    
        
# Fungsi untuk menghapus review film
def admin_hapus_review():
    try:
        showList()
        tunjuk = int(input("Pilih nomor film (0 untuk kembali) : "))
        tunjuk -= 1
        os.system('cls')
        if tunjuk == -1 :
            return menu_admin()
        elif 0 <= tunjuk < len(cinema):
            judul = list(cinema.keys())[tunjuk]
            review = cinema[judul]['review']
            if not review:
                print("Tidak ada review untuk film ini")
                return admin_hapus_review()
            else:
                while True:
                    try:
                        print(f"Review untuk {judul} :")
                        for i, ulasan in enumerate(review):
                            print(f"{i + 1}.  From    : {ulasan['username']}")
                            print(f"    Rating  : {ulasan['rating']}")
                            print(f"    Comment : {ulasan['comment']}")
                            print()
                        nomor_review = int(input("Pilih nomor review yang akan dihapus (0 untuk kembali) : "))
                        os.system('cls')
                        nomor_review -= 1
                        if nomor_review == -1:
                            return admin_hapus_review()
                        elif 0 <= nomor_review < len(review):
                            while True:
                                konfirmasi = input("Hapus review? Konfirmasi(y) / Cancel(n) : ")
                                os.system('cls')
                                if konfirmasi.lower() == 'y':
                                    del review[nomor_review]
                                    print("Review berhasil dihapus!")
                                    return admin_hapus_review()
                                elif konfirmasi.lower() == 'n':
                                    return admin_hapus_review()
                                else:
                                    print("Input tidak valid!")
                        else:
                            print("Review tidak ditemukan!")
                    except ValueError:
                        os.system('cls')
                        print("Input tidak valid!")
        else:
            print("Film tidak ditemukan!")
            return admin_hapus_review()
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return admin_hapus_review()
    
def tambah_judul_film():
    judul = input("Masukkan judul film yang ingin ditambahkan (0 untuk kembali) : ")
    os.system('cls')
    if judul == '0':
        return menu_admin()
    elif judul not in cinema:
        while True:
            konfirmasi = input("Tambah film? Konfirmasi(y) / Cancel(n) : ")
            os.system('cls')
            if konfirmasi.lower() == 'y':
                cinema[judul] = {'review': []}
                print("Film berhasil ditambahkan!")
                return menu_admin()
            elif konfirmasi.lower() == 'n':
                return tambah_judul_film()
            else:
                print("Input tidak valid!")
    else:
        print("Judul film sudah ada")
        return tambah_judul_film()

def ubah_judul_film():
    try:
        showList()
        tunjuk = int(input("Pilih nomor film yang ingin diubah judulnya (0 untuk kembali) : "))
        tunjuk -= 1
        os.system('cls')
        if tunjuk == -1:
            return menu_admin()
        elif 0 <= tunjuk < len(cinema):
            judul = list(cinema.keys())[tunjuk]
            while True:
                judul_baru = input("Masukkan judul film baru : ")
                if judul_baru in cinema.keys():
                    print("Judul film sudah ada")
                else:
                    break
            while True:
                konfirmasi = input("Ubah judul film? Konfirmasi(y) / Cancel(n) : ")
                os.system('cls')
                if konfirmasi.lower() == 'y':
                    cinema[judul_baru] = cinema.pop(judul)
                    print("Judul film berhasil diubah!")
                    return menu_admin()
                elif konfirmasi.lower() == 'n':
                    return ubah_judul_film()
                else:
                    print("Input tidak valid!")
        else:
            print("Film tidak ditemukan!")
            return ubah_judul_film()
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return ubah_judul_film()

def hapus_judul_film():
    try:
        showList()
        tunjuk = int(input("Pilih nomor film yang akan dihapus (0 untuk kembali) : "))
        tunjuk -= 1
        os.system('cls')
        if tunjuk == -1:
            return menu_admin()
        elif 0 <= tunjuk < len(cinema):
            judul = list(cinema.keys())[tunjuk]
            while True:
                konfirmasi = input("Hapus film? Konfirmasi(y) / Cancel(n) : ")
                os.system('cls')
                if konfirmasi.lower() == 'y':
                    del cinema[judul]
                    print("Film berhasil dihapus!")
                    return menu_admin()
                elif konfirmasi.lower() == 'n':
                    return hapus_judul_film()
                else:
                    print("Input tidak valid!")
        else:
            print("Film tidak ditemukan!")
            return hapus_judul_film()
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return ubah_judul_film()

# Fungsi untuk menampilkan review film
def user_lihat_review(username):
    try:
        showList()
        tunjuk = int(input("Pilih nomor film (0 untuk kembali) : "))
        tunjuk -= 1
        os.system('cls')
        if tunjuk == -1:
            return menu_user(username)
        elif 0 <= tunjuk < len(cinema):
            judul = list(cinema.keys())[tunjuk]
            review = cinema[judul]['review']
            if review:
                print(f"Review untuk {judul}:")
                print("--------------------------------------------------------")
                for ulasan in review:
                    print(f"From    : {ulasan['username']}")
                    print(f"Rating  : {ulasan['rating']}")
                    print(f"Comment : {ulasan['comment']}")
                    print()
                return user_lihat_review(username)
            else:
                print("Tidak ada review untuk film ini")
                return user_lihat_review(username)
        else:
            print("Film tidak ditemukan!")
            return user_lihat_review(username)
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return user_lihat_review(username)  

def beri_review(username):
    try:
        showList()
        tunjuk = int(input("Masukkan nomor film yang ingin direview (0 untuk kembali) : "))
        tunjuk -= 1
        os.system('cls')
        if tunjuk == -1:
            return menu_user(username)
        elif 0 <= tunjuk < len(cinema):
            judul = list(cinema.keys())[tunjuk]
            review = cinema[judul]['review']
            for ulasan in review:
                if ulasan['username'] == username:
                    print("Anda sudah memberi rating untuk film ini")
                    return beri_review(username)
            while True:
                rating = int(input("Beri rating (1-10) untuk film ini : "))
                os.system('cls')
                if rating > 0 and rating <= 10:
                    comment = input("Beri komentar : ")
                    cinema[judul]['review'].append({
                        'username': username,
                        'rating': rating,
                        'comment': comment
                    })
                    os.system('cls')
                    print(f"Review untuk {judul} berhasil ditambahkan!")
                    return menu_user(username)
                else:
                    print("Rating harus berada dalam rentang 1 hingga 10!")
        else:
            print("Film tidak ditemukan!")
            return beri_review(username)
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return beri_review(username)

def ubah_review(username):
    try:
        showList()
        tunjuk = int(input("Masukkan nomor film (0 untuk kembali) : "))
        os.system('cls')
        tunjuk -= 1
        if tunjuk == -1:
            return menu_user(username)
        elif 0 <= tunjuk < len(cinema):
            judul = list(cinema.keys())[tunjuk]
            review = cinema[judul]['review']
            for ulasan in review:
                if ulasan['username'] == username:
                    while True:
                        try:
                            print(f"---Current Review---")
                            print()
                            print(f"Rating  : {ulasan['rating']}")
                            print(f"Comment : {ulasan['comment']}")
                            print("----------------------------------------------------------------")
                            new_rating = int(input("Masukkan rating baru : "))
                            if new_rating > 0 and new_rating <= 10:
                                new_comment = input("Masukkan komentar baru : ")
                                while True:
                                    konfirmasi = input("Ubah review? Konfirmasi(y) / Cancel(n) : ")
                                    os.system('cls')
                                    if konfirmasi.lower() == 'y':
                                        for review in cinema[judul]['review']:
                                            if review['username'] == username:
                                                review['rating'] = new_rating
                                                review['comment'] = new_comment
                                                print(f"Review untuk {judul} berhasil diubah!")
                                                return menu_user(username)
                                    elif konfirmasi.lower() == 'n':
                                        return ubah_review(username)
                                    else:
                                        print("Input tidak valid!")
                            else:
                                os.system('cls')
                                print("Rating harus berada dalam rentang 1 hingga 10!")
                        except ValueError:
                            os.system('cls')
                            print("Input tidak valid!")
            print(f"Anda belum memberikan review untuk {judul} !")
            return ubah_review(username)
        else:
            print("Film tidak ditemukan!")
            return ubah_review(username)
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return ubah_review(username)

def hapus_review(username):
    try:
        showList()
        tunjuk = int(input("Pilih nomor film (0 untuk kembali) : "))
        tunjuk -= 1
        os.system('cls')
        if tunjuk == -1:
            os.system('cls')
            return menu_user(username)
        elif 0 <= tunjuk < len(cinema):
            judul = list(cinema.keys())[tunjuk]
            review = cinema[judul]['review']
            for ulasan in review:
                if ulasan['username'] == username:
                    print(f"---Current Review---")
                    print()
                    print(f"Rating  : {ulasan['rating']}")
                    print(f"Comment : {ulasan['comment']}")
                    print()
                    while True:
                        konfirmasi = input("Hapus review? Konfirmasi(y) / Cancel(n) : ")
                        os.system('cls')
                        if konfirmasi.lower() == 'y':
                            review.remove(ulasan)
                            print(f"Review untuk {judul} berhasil dihapus!")
                            return menu_user(username)
                        elif konfirmasi.lower() == 'n':
                            return hapus_review(username)
                        else:
                            print("Input tidak valid!")
            print(f"Anda belum memberikan review untuk {judul} !")
            return hapus_review(username)
        else:
            print("Film tidak ditemukan")
            return hapus_review(username)
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return hapus_review(username)

# Fungsi Menu Admin
def menu_admin():
    try:
        print("Menu Admin")
        print("[1] Lihat Review Film")
        print("[2] Hapus Review Film")
        print("[3] Tambah Judul Film")
        print("[4] Ubah Judul Film")
        print("[5] Hapus Judul Film")
        print("[0] Sign Out")
        pilihan = int(input("Pilih menu : "))
        os.system('cls')
        if pilihan == 1:
            admin_lihat_review()
        elif pilihan == 2:
            admin_hapus_review()
        elif pilihan == 3:
            tambah_judul_film()
        elif pilihan == 4:
            ubah_judul_film()
        elif pilihan == 5:
            hapus_judul_film()
        elif pilihan == 0:
            print("Sign out berhasil!")
            return main()
        else:
            print("Pilihan menu tidak valid!")
            return menu_admin()
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return menu_admin()

# Fungsi Menu User
def menu_user(username):
    try:
        print("Menu")
        print("[1] Lihat Review Film")
        print("[2] Beri Review Film")
        print("[3] Ubah Review Film")
        print("[4] Hapus Review Film")
        print("[0] Sign Out")
        pilihan = int(input("Pilih menu : "))
        os.system('cls')
        if pilihan == 1 :
            user_lihat_review(username)
        elif pilihan == 2 :
            beri_review(username)
        elif pilihan == 3 :
            ubah_review(username)
        elif pilihan == 4 :
            hapus_review(username)
        elif pilihan == 0 :
            print("Sign out berhasil!")
            return main()
        else:
            print("Pilihan menu tidak valid!")
            return menu_user(username)
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return menu_user(username)

# Fungsi menu masuk
def main():
    while True:
        try:
            print("Wellcome to Letterboxd")

            print("[1] Sign in")
            print("[2] Register")
            print("[0] Exit")
            print()
            pilihan = int(input("Pilih menu : "))
            os.system('cls')
            if pilihan == 1:
                username = sign_in()
            elif pilihan == 2:
                username = regist()
            elif pilihan == 0:
                print("Terima kasih sudah menggunakan Letterboxd! May the Force be with You!")
                exit()
            else:
                print("Pilihan menu tidak valid!")
        except ValueError:
            os.system('cls')
            print("Input tidak valid!")
            
if __name__ == "__main__":
    main()