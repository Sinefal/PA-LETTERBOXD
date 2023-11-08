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
                'rating': 8,
                'comment': "Tidurrrrrrrrrrrrrrrrr"
            }
        ]
    },
    'Avengers: Infinity War': {
        'review': [
            {
                'username': "user",
                'rating': 2,
                'comment': "3487 pilem opo iki"
            }
        ]
    }
}

akun_admin = {
    "admin" : "123"
}

akun_user = {
    "user" : "321",
    "Ryan Gosling" : "me"
}

def sign_in():
    coba = 0
    while coba < 3 :
        username=input("Masukkan Username : ")
        password=input("Masukkan Password : ")
        os.system('cls')
        if username in akun_admin.keys() and password in akun_admin.values() :
            while True :
                lanjut=input("Ingin melanjutkan sign in(y/n)?")
                os.system('cls')
                if lanjut.lower() == "n":
                    return main()
                elif lanjut.lower() == "y":
                    return menu_admin()
                else:
                    print("input tidak valid")
        elif username in  akun_user.keys() and password in akun_user.values() :
            while True :
                lanjut=input("Ingin melanjutkan sign in? Lanjut(y) / Cancel(n) : ")
                os.system('cls')
                if lanjut.lower() == "n":
                    return main()
                elif lanjut.lower() == "y":
                    return menu_user(username)
                else:
                    print("Input tidak valid!")
        else :
            coba+=1
            print("Sign In gagal!")
        if coba==3:
            print("Upaya masuk terlalu sering. Coba lagi nanti.")

# Fungsi register akun
def regist():
    while True :
        new_username = input("Username baru : ")
        if new_username in akun_user.keys() or new_username in akun_admin.keys() :
            print("Username sudah digunakan!")
        else :
            break
    new_password=input("Password baru : ")
    akun_user.update({new_username : new_password})
    
    while True :
        konfirmasi = input("Konfirmasi(y) / Cancel(n) : ")
        os.system('cls')
        if konfirmasi.lower() == "y" :
            print("Akun berhasil dibuat!")
            return
        elif konfirmasi.lower() == 'n':
            akun_user.pop(new_username)
            return
        else :
            print("Input tidak sesuai!")

def showList():
    if not cinema:
        print("Tidak ada film.")
        return

    for i, film in enumerate(cinema):
        print(f"{i + 1}. {film}")

# Fungsi untuk menampilkan review film
def lihat_review_film():
    showList()
    try:
        nomor_film = int(input("Pilih nomor film (0 untuk kembali): ")) - 1
        os.system('cls')
        if nomor_film == -1 :
            return
        elif 0 <= nomor_film < len(cinema):
            judul_film = list(cinema.keys())[nomor_film]
            ulasan = cinema[judul_film]['review']
            if ulasan:
                print(f"Review untuk {judul_film}:")
                print("--------------------------------------------------------")
                for review in ulasan:
                    print(f"From: {review['username']}")
                    print(f"Rating: {review['rating']}")
                    print(f"Comment: {review['comment']}")
                    print()
            else:
                print("Tidak ada review untuk film ini.")
        else:
            print("Film tidak ditemukan.")
            return lihat_review_film()
    except ValueError:
        os.system("cls")
        print("Input tidak valid.")
        return lihat_review_film()
    
# Fungsi untuk menampilkan review film
def lihat_review_film_user(username):
    showList()
    try:
        nomor_film = int(input("Pilih nomor film (0 untuk kembali): ")) - 1
        os.system('cls')
        if nomor_film == -1 :
            return menu_user(username)
        elif 0 <= nomor_film < len(cinema):
            judul_film = list(cinema.keys())[nomor_film]
            ulasan = cinema[judul_film]['review']
            if ulasan:
                print(f"Review untuk {judul_film}:")
                print("--------------------------------------------------------")
                for review in ulasan:
                    print(f"From: {review['username']}")
                    print(f"Rating: {review['rating']}")
                    print(f"Comment: {review['comment']}")
                    print()
                    return menu_user(username)
            else:
                print("Tidak ada review untuk film ini.")
                return menu_user(username)
        else:
            print("Film tidak ditemukan.")
            return lihat_review_film_user(username)
    except ValueError:
        os.system("cls")
        print("Input tidak valid.")
        return lihat_review_film_user(username)      
        
# Fungsi untuk menghapus review film
def admin_hapus_review():
    showList()
    try:
        nomor_film = int(input("Pilih nomor film (0 untuk kembali): ")) -1
        os.system('cls')
        if nomor_film == -1 :
            return
        elif 0 <= nomor_film < len(cinema):
            judul_film = list(cinema.keys())[nomor_film]
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
                            del ulasan[nomor_ulasan]
                            print("Ulasan film berhasil dihapus!")
                            return admin_hapus_review()
                        else:
                            print("Nomor ulasan tidak valid.")
                    except ValueError:
                        os.system('cls')
                        print("Input tidak valid.")
        else:
            print("Nomor film tidak valid.")
            return admin_hapus_review()
    except ValueError:
        os.system('cls')
        print("Input tidak valid.")
        return admin_hapus_review()
    
def tambah_judul_film():
    judul_film = input("Masukkan judul film yang akan ditambahkan (0 untuk kembali): ")
    os.system('cls')
    while True:
        if judul_film == '0':
            return
        elif judul_film not in cinema:
            while True:
                konfirmasi = input("Konfirmasi(y) / Cancel(n) : ")
                os.system('cls')
                if konfirmasi.lower() == 'y':
                    cinema[judul_film] = {'review': []}
                    print("Judul film telah ditambahkan!")
                    return
                elif konfirmasi.lower() == 'n':
                    return tambah_judul_film()
                else:
                    print("Input tidak valid")
        else:
            print("Judul film sudah ada dalam daftar.")
            return tambah_judul_film()

def ubah_judul_film():
    showList()
    try:
        nomor_film = int(input("Pilih nomor film yang akan diubah (0 untuk kembali): ")) - 1
        os.system('cls')
        while True:
            if nomor_film == -1:
                return
            elif 0 <= nomor_film < len(cinema):
                judul_film = list(cinema.keys())[nomor_film]
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
                        print("Judul film telah diubah!")
                        return menu_admin()
                    elif konfirmasi.lower() == 'n':
                        return ubah_judul_film()
                    else:
                        print("Input tidak valid")
            else:
                print("Nomor film tidak valid.")
                return ubah_judul_film()
    except ValueError:
        os.system('cls')
        print("Input tidak valid.")
        return ubah_judul_film()

def hapus_judul_film():
    showList()
    try:
        nomor_film = int(input("Pilih nomor film yang akan dihapus (0 untuk kembali): ")) - 1
        os.system('cls')
        while True:
            if nomor_film == -1:
                return
            elif 0 <= nomor_film < len(cinema):
                judul_film = list(cinema.keys())[nomor_film]
                while True:
                    konfirmasi = input("Konfirmasi(y) / Cancel(n) : ")
                    os.system('cls')
                    if konfirmasi.lower() == 'y':
                        del cinema[judul_film]
                        print("Judul film telah dihapus!")
                        return menu_admin()
                    elif konfirmasi.lower() == 'n':
                        return hapus_judul_film()
                    else:
                        print("Input tidak valid")
            else:
                print("Nomor film tidak valid.")
    except ValueError:
        os.system('cls')
        print("Input tidak valid.")
        return ubah_judul_film()

def beri_review(username):
    showList()
    try:
        while True:
            nomor_film = int(input("Masukkan nomor film yang ingin direview (0 untuk kembali): ")) - 1
            os.system('cls')
            if nomor_film == -1:
                return menu_user(username)
            elif 0 <= nomor_film <= len(cinema):
                judul = list(cinema.keys())[nomor_film]
                review = cinema[judul]['review']
                for ulasan in review:
                    if ulasan['username'] == username:
                        print("Anda sudah memberi rating untuk film ini.")
                        return beri_review(username)
                while True:
                    rating = int(input("Berikan rating (1-10) untuk film ini: "))
                    if rating > 0 and rating <= 10:
                        comment = input("Tambahkan komentar Anda: ")
                        cinema[judul]['review'].append({
                            'username': username,
                            'rating': rating,
                            'comment': comment
                        })
                        os.system('cls')
                        print(f"Review untuk film '{judul}' telah ditambahkan.")
                        return menu_user(username)
                    else:
                        print("Rating harus berada dalam rentang 1 hingga 10.")
            else:
                print("Film tidak ditemukan.")
    except ValueError:
        print("Input tidak valid!")
        return beri_review(username)

def ubah_review(username):
    showList()
    try:
        while True:
            nomor_film = int(input("Masukkan nomor film (0 untuk kembali): ")) -1
            os.system('cls')
            if nomor_film == -1:
                return ubah_review(username)
            elif 0 <= nomor_film <= len(cinema):
                judul = list(cinema.keys())[nomor_film]
                while True:
                    try:
                        new_rating = int(input("Masukkan rating baru: "))
                        if new_rating > 0 and new_rating <= 10:
                            new_comment = input("Masukkan komentar baru: ")
                            while True:
                                konfirmasi = input("Konfirmasi(y) / Cancel(n) : ")
                                os.system('cls')
                                if konfirmasi.lower() == 'y':
                                    for review in cinema[judul]['review']:
                                        if review['username'] == username:
                                            review['rating'] = new_rating
                                            review['comment'] = new_comment
                                            print(f"Review untuk film '{judul}' telah diubah.")
                                            return menu_user(username)
                                elif konfirmasi.lower() == 'n':
                                    return ubah_review(username)
                                else:
                                    print("Input tidak valid")
                        else:
                            print("Rating harus berada dalam rentang 1 hingga 10.")
                    except ValueError:
                        print("Input tidak valid!")
            else:
                print("Film tidak tersedia!")
    except ValueError:
        os.system('cls')
        print("Input tidak valid!")
        return ubah_review(username)

def hapus_review(username):
    showList()
    try:
        while True:
            nomor_film = int(input("Masukkan kode film yang ingin dihapus review-nya (0 untuk kembali): ")) -1
            if nomor_film == -1:
                return menu_user(username)
            elif 0 <= nomor_film <= len(cinema):
                film = list(cinema.keys())[nomor_film]
                ulasan = cinema[film]['review']
                for review in ulasan:
                    if review['username'] == username:
                        print(f"Review saat ini:")
                        print(f"Rating: {review['rating']}")
                        print(f"Komentar: {review['comment']}")
                        while True:
                            konfirmasi = input("Konfirmasi(y) / Cancel(n) : ")
                            os.system('cls')
                            if konfirmasi.lower() == 'y':
                                ulasan.remove(review)
                                print(f"Review untuk film '{film}' telah dihapus.")
                                return menu_user(username)
                            elif konfirmasi.lower() == 'n':
                                return hapus_review(username)
                            else:
                                print("Input tidak valid!")
                    else:
                        print(f"Anda belum memberikan review untuk film '{film}'.")
            else:
                print("Film tidak tersedia.")
    except ValueError:
        print("Input tidak valid.")
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
            lihat_review_film()
        elif pilihan == "2":
            admin_hapus_review()
        elif pilihan == "3":
            tambah_judul_film()
        elif pilihan == "4":
            ubah_judul_film()
        elif pilihan == "5":
            hapus_judul_film()
        elif pilihan == "0":
            print("Anda berhasil keluar.")
            return None
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Fungsi Menu User
def menu_user(username):
    print("""Menu
[1] Lihat Review Film
[2] Beri Review Film
[3] Ubah Review Film
[4] Hapus Review Film
[0] Sign Out""")
    try:
        pilih_user=int(input("Pilih menu : "))
        os.system('cls')
        if pilih_user == 1 :
            lihat_review_film_user(username)
        elif pilih_user == 2 :
            beri_review(username)
        elif pilih_user == 3 :
            ubah_review(username)
        elif pilih_user == 4 :
            hapus_review(username)
        elif pilih_user == 0 :
            main()
        else :
            print("Input tidak valid")
    except ValueError:
        print("Input tidak valid")

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
            break
        else:
            print("Pilihan tidak valid.")
            
if __name__ == "__main__":
    main()