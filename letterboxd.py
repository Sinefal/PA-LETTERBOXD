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
                'username': "yanto",
                'rating': 2,
                'comment': "lmaooooooooooooooooo"
            },
            {
                'username': "user",
                'rating': 2,
                'comment': "fiefjeuhf"
            }
        ]
    },
    'Avengers: Infinity War': {
        'review': [
            {
                'username': "user",
                'rating': 2,
                'comment': "3487 pilem opo iki"
            },
            {
                'username': "Ryan Gosling",
                'rating': 2,
                'comment': "lmaooooooooooooooooo"
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
                konfirmasi=input("Masuk ke menu utama? Konfirmasi(y) / Cancel(n) : ")
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
                konfirmasi=input("Masuk ke menu utama? Konfirmasi(y) / Cancel(n) : ")
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
    showList()
    try:
        tunjuk = int(input("Pilih nomor film (0 untuk kembali): "))
        os.system('cls')
        tunjuk -= 1
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
    showList()
    try:
        tunjuk = int(input("Pilih nomor film (0 untuk kembali): ")) -1
        os.system('cls')
        if tunjuk == -1 :
            return menu_admin()
        elif 0 <= tunjuk < len(cinema):
            judul_film = list(cinema.keys())[tunjuk]
            ulasan = cinema[judul_film]['review']
            if not ulasan:
                print("Tidak ada review untuk film ini")
                return admin_hapus_review()
            else:
                while True:
                    try:
                        print(f"Review untuk {judul_film} :")
                        for i, review in enumerate(ulasan):
                            print(f"{i + 1}.  From    : {review['username']}")
                            print(f"    Rating  : {review['rating']}")
                            print(f"    Comment : {review['comment']}")
                            print()
                        nomor_ulasan = int(input("Pilih nomor ulasan yang akan dihapus (0 untuk kembali): ")) - 1
                        os.system('cls')
                        if nomor_ulasan == -1:
                            return admin_hapus_review()
                        elif 0 <= nomor_ulasan < len(ulasan):
                            while True:
                                konfirmasi = input("Konfirmasi(y) / Cancel(n) : ")
                                os.system('cls')
                                if konfirmasi.lower() == 'y':
                                    del ulasan[nomor_ulasan]
                                    print("Ulasan film berhasil dihapus!")
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
            print("Film tidak ditemukan")
            return admin_hapus_review()
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return admin_hapus_review()
    
def tambah_judul_film():
    judul_film = input("Masukkan judul film yang akan ditambahkan (0 untuk kembali): ")
    os.system('cls')
    while True:
        if judul_film == '0':
            return menu_admin()
        elif judul_film not in cinema:
            while True:
                konfirmasi = input("Konfirmasi(y) / Cancel(n) : ")
                os.system('cls')
                if konfirmasi.lower() == 'y':
                    cinema[judul_film] = {'review': []}
                    print("Judul film berhasil ditambahkan!")
                    return menu_admin()
                elif konfirmasi.lower() == 'n':
                    return tambah_judul_film()
                else:
                    print("Input tidak valid!")
        else:
            print("Judul film sudah ada")
            return tambah_judul_film()

def ubah_judul_film():
    showList()
    try:
        tunjuk = int(input("Pilih nomor film yang ingin diubah judulnya (0 untuk kembali): ")) - 1
        os.system('cls')
        while True:
            if tunjuk == -1:
                return menu_admin()
            elif 0 <= tunjuk < len(cinema):
                judul_film = list(cinema.keys())[tunjuk]
                while True:
                    new_judul_film = input("Masukkan judul film baru: ")
                    if new_judul_film in cinema.keys():
                        print("Judul film sudah ada")
                    else:
                        break
                while True:
                    konfirmasi = input("Konfirmasi(y) / Cancel(n) : ")
                    os.system('cls')
                    if konfirmasi.lower() == 'y':
                        cinema[new_judul_film] = cinema.pop(judul_film)
                        print("Judul film berhasil diubah!")
                        return menu_admin()
                    elif konfirmasi.lower() == 'n':
                        return ubah_judul_film()
                    else:
                        print("Input tidak valid!")
            else:
                print("Film tidak ditemukan")
                return ubah_judul_film()
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return ubah_judul_film()

def hapus_judul_film():
    showList()
    try:
        tunjuk = int(input("Pilih nomor film yang akan dihapus (0 untuk kembali): ")) - 1
        os.system('cls')
        while True:
            if tunjuk == -1:
                return menu_admin()
            elif 0 <= tunjuk < len(cinema):
                judul_film = list(cinema.keys())[tunjuk]
                while True:
                    konfirmasi = input("Konfirmasi(y) / Cancel(n) : ")
                    os.system('cls')
                    if konfirmasi.lower() == 'y':
                        del cinema[judul_film]
                        print("Judul film berhasil dihapus!")
                        return menu_admin()
                    elif konfirmasi.lower() == 'n':
                        return hapus_judul_film()
                    else:
                        print("Input tidak valid!")
            else:
                print("Film tidak ditemukan")
                return hapus_judul_film()
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return ubah_judul_film()

# Fungsi untuk menampilkan review film
def user_lihat_review(username):
    showList()
    try:
        tunjuk = int(input("Pilih nomor film (0 untuk kembali): "))
        os.system('cls')
        tunjuk -= 1
        if tunjuk == -1:
            return menu_user(username)
        elif 0 <= tunjuk < len(cinema):
            film = list(cinema.keys())[tunjuk]
            review = cinema[film]['review']
            if review:
                print(f"\nReview untuk film '{film}':")
                print("-------------------------------------")
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
            print("Film tidak ditemukan.")
            return user_lihat_review(username)
    except ValueError:
        os.system('cls')
        print("Input tidak valid")
        return user_lihat_review(username)  

def beri_review(username):
    try:
        while True:
            showList()
            tunjuk = int(input("Masukkan nomor film yang ingin direview (0 untuk kembali): ")) - 1
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
                    rating = int(input("Berikan rating (1-10) untuk film ini: "))
                    os.system('cls')
                    if rating > 0 and rating <= 10:
                        comment = input("Tambahkan komentar Anda: ")
                        cinema[judul]['review'].append({
                            'username': username,
                            'rating': rating,
                            'comment': comment
                        })
                        os.system('cls')
                        print(f"Review untuk film '{judul}' berhasil ditambahkan!")
                        return menu_user(username)
                    else:
                        print("Rating harus berada dalam rentang 1 hingga 10!")
            else:
                print("Film tidak ditemukan")
                return beri_review(username)
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return beri_review(username)

def ubah_review(username):
    try:
        while True:
            showList()
            tunjuk = int(input("Masukkan nomor film (0 untuk kembali): "))
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
                                new_rating = int(input("Masukkan rating baru: "))
                                if new_rating > 0 and new_rating <= 10:
                                    new_comment = input("Masukkan komentar baru: ")
                                    while True:
                                        konfirmasi = input("Ubah review? Konfirmasi(y) / Cancel(n) : ")
                                        os.system('cls')
                                        if konfirmasi.lower() == 'y':
                                            for review in cinema[judul]['review']:
                                                if review['username'] == username:
                                                    review['rating'] = new_rating
                                                    review['comment'] = new_comment
                                                    print(f"Review untuk film '{judul}' berhasil diubah!")
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
                print("Tidak ada review untuk film ini")
                return ubah_review(username)
            else:
                print("Film tidak ditemukan!")
                return ubah_review(username)
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return ubah_review(username)

def hapus_review(username):
    showList()
    try:
        while True:
            tunjuk = int(input("Masukkan kode film yang ingin dihapus review-nya (0 untuk kembali): ")) -1
            os.system('cls')
            if tunjuk == -1:
                os.system('cls')
                return menu_user(username)
            elif 0 <= tunjuk < len(cinema):
                film = list(cinema.keys())[tunjuk]
                ulasan = cinema[film]['review']
                for review in ulasan:
                    if review['username'] == username:
                        print(f"---Your Review---")
                        print()
                        print(f"Rating  : {review['rating']}")
                        print(f"Comment : {review['comment']}")
                        print()
                        while True:
                            konfirmasi = input("Hapus review? Konfirmasi(y) / Cancel(n) : ")
                            os.system('cls')
                            if konfirmasi.lower() == 'y':
                                ulasan.remove(review)
                                print(f"Review untuk film '{film}' berhasil dihapus!")
                                return menu_user(username)
                            elif konfirmasi.lower() == 'n':
                                return hapus_review(username)
                            else:
                                print("Input tidak valid!")
                print(f"Anda belum memberikan review untuk {film} !")
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
    while True:
        print("""\nMenu Admin
[1] Lihat Review Film
[2] Hapus Review Film
[3] Tambah Judul Film
[4] Ubah Judul Film
[5] Hapus Judul Film
[0] Sign Out""")

        pilihan = input("Masukkan pilihan: ")
        os.system('cls')
        if pilihan == "1":
            admin_lihat_review()
        elif pilihan == "2":
            admin_hapus_review()
        elif pilihan == "3":
            tambah_judul_film()
        elif pilihan == "4":
            ubah_judul_film()
        elif pilihan == "5":
            hapus_judul_film()
        elif pilihan == "0":
            print("Sign out berhasil!")
            return main()
        else:
            print("Pilihan tidak valid!")

# Fungsi Menu User
def menu_user(username):
    print("""Menu
[1] Lihat Review Film
[2] Beri Review Film
[3] Ubah Review Film
[4] Hapus Review Film
[0] Sign Out""")
    while True:
        try:
            pilih_user=int(input("Pilih menu : "))
            os.system('cls')
            if pilih_user == 1 :
                user_lihat_review(username)
            elif pilih_user == 2 :
                beri_review(username)
            elif pilih_user == 3 :
                ubah_review(username)
            elif pilih_user == 4 :
                hapus_review(username)
            elif pilih_user == 0 :
                print("Sign out berhasil!")
                return main()
            else :
                print("Pilihan tidak valid!")
                return menu_user(username)
        except ValueError:
            os.system('cls')
            print("Input tidak valid!")
            return menu_user(username)

# Fungsi menu masuk
def main():
    while True:
        print("\nSelamat datang di Letterboxd")
        print("[1] Sign in")
        print("[2] Register")
        print("[0] Exit")

        pilihan = input("Pilihan Anda: ")
        os.system('cls')
        if pilihan == '1':
            username = sign_in()
        elif pilihan == '2':
            username = regist()
        elif pilihan == '0':
            print("Terima kasih sudah menggunakan Letterboxd! May the Force be with You!")
            exit()
        else:
            print("Pilihan tidak valid!")
            
if __name__ == "__main__":
    main()