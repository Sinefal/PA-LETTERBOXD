cinema = {
    'Interstellar': {
        'review': [
            {
                'username': 'Ardian',
                'rating': 10,
                'comment': 'Mahakarya dari Christopher Nolan'
            },
            {
                'username': 'Andrei',
                'rating': 9,
                'comment': 'Spektakuler! Sutradara Christopher Nolan luar biasa.'
            },
            {
                'username': 'Maulana',
                'rating': 8,
                'comment': 'Konsep ilmiah yang menarik.'
            }
        ]
    },
    'Blade Runner': {
        'review': [
            {
                'username': 'Ardian',
                'rating': 8,
                'comment': 'Tidurrrrrrrrrrrrrrrrr'
            },
            {
                'username': 'Andrei',
                'rating': 7,
                'comment': 'Atmosfir yang menakjubkan.'
            },
            {
                'username': 'Maulana',
                'rating': 6,
                'comment': 'Atmosfir futuristik yang kuat.'
            }
        ]
    },
    'Avengers: Infinity War': {
        'review': [
            {
                'username': 'Maulana',
                'rating': 2,
                'comment': "3487 pilem '.'.] opo iki"
            },
            {
                'username': 'Ardian',
                'rating': 7,
                'comment': 'Spektakuler! Begitu banyak superhero.'
            },
            {
                'username': 'Andrei',
                'rating': 6,
                'comment': 'Aksi yang hebat, tapi jalan cerita agak rumit.'
            }
        ]
    }
}

cinephile = {
    'Andrei': {
        'password': 'Tarkovsky',
        'role': 'admin'
    },
    'Ardian': {
        'password': 'ganteng',
        'role': 'user'
    },
    'Maulana': {
        'password': 'hari',
        'role': 'user'
    }
}

# Fungsi untuk menambahkan (CREATE) judul film
def addFilm():
    title = input("Masukkan judul film: ")
    if not title:
        print("Judul film tidak boleh kosong.")
        return

    if title in cinema:
        print("Film sudah ada di dalam daftar.")
    else:
        cinema[title] = {
            'review': []
        }
        print("Film berhasil ditambahkan.")

# Fungsi untuk menampilkan (READ) daftar film
def showList():
    if not cinema:
        print("Tidak ada film di dalam daftar.")
        return

    for i, film in enumerate(cinema):
        print(f"{i + 1}. {film}")

# Fungsi untuk memberi (CREATE) rating film
def rateFilm(username):
    
    showList()
    
    try:
        filmNumber = int(input("Pilih film yang akan di rating (masukkan nomor film): ")) - 1
        if filmNumber == -1:
            return
        elif 0 <= filmNumber < len(cinema):
            title = list(cinema.keys())[filmNumber]
            review = cinema[title]['review']
            for rating in review:
                if rating['username'] == username:
                    print("Anda sudah memberi rating untuk film ini.")
                    return
            rating = int(input("Beri rating (1-10): "))
            if 1 <= rating <= 10:
                cinema[title]['review'].append({
                    'username': username,
                    'rating': rating
                })
                print("Rating berhasil diberikan.")
            else:
                print("Rating harus antara 1-10.")
        else:
            print("Film tidak ditemukan.")
    except ValueError:
        print("Masukkan nomor film yang valid.")

# Fungsi untuk menampilkan (READ) rating film
def showRating():
    if not cinema:
        print("Tidak ada film di dalam daftar.")
        return

    showList()

    try:
        filmNumber = int(input("Pilih film untuk melihat rating (masukkan nomor film): ")) - 1
        if 0 <= filmNumber < len(cinema):
            title = list(cinema.keys())[filmNumber]
            review = cinema[title]['review']
            if review:
                print(f"Rating untuk film '{title}':")
                for rating in review:
                    print(f"From: {rating['username']}")
                    print(f"Rating: {rating['rating']}")
                    print(f"Comment: {rating['comment']}")
                    print()
            else:
                print("Belum ada rating untuk film ini.")
        else:
            print("Film tidak ditemukan.")
    except ValueError:
        print("Masukkan nomor film yang valid.")

# Fungsi untuk mengubah (UPDATE) rating film
def editRating(username):
    if not cinema:
        print("Tidak ada film di dalam daftar.")
        return

    showList()

    try:
        filmNumber = int(input("Pilih film yang akan diubah ratingnya (masukkan nomor film): ")) - 1
        if 0 <= filmNumber < len(cinema):
            title = list(cinema.keys())[filmNumber]
            for rating in cinema[title]['review']:
                if rating['username'] == username:
                    try:
                        newRating = int(input("Masukkan rating baru (1-10): "))
                        if 1 <= newRating <= 10:
                            rating['rating'] = newRating
                            print("Rating berhasil diubah.")
                            break
                        else:
                            print("Rating harus antara 1-10.")
                    except ValueError:
                        print("Masukkan rating yang valid.")
            else:
                print("Anda belum memberikan rating untuk film ini.")
        else:
            print("Film tidak ditemukan.")
    except ValueError:
        print("Masukkan nomor film yang valid.")

# Fungsi untuk menghapus (DELETE) rating film
def deleteRating(username):
    if not cinema:
        print("Tidak ada film di dalam daftar.")
        return

    showList()

    try:
        filmNumber = int(input("Pilih film yang akan dihapus ratingnya (masukkan nomor film): ")) - 1
        if 0 <= filmNumber < len(cinema):
            title = list(cinema.keys())[filmNumber]
            review = cinema[title]['review']
            for rating in review:
                if rating['username'] == username:
                    cinema[title]['review'].remove(rating)
                    print("Rating berhasil dihapus.")
                    break
            else:
                print("Anda belum memberikan rating untuk film ini.")
        else:
            print("Film tidak ditemukan.")
    except ValueError:
        print("Masukkan nomor film yang valid.")


# Fungsi untuk role admin
def is_admin(username):
    if username in cinephile:
        return cinephile[username]['role'] == 'admin'
    return False

# Fungsi sign in akun
def sign_in():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in cinephile and cinephile[username]['password'] == password:
        print("Sign in berhasil.")
        return username
    print("Username atau password salah.")
    return None

# Fungsi register akun
def register():
    while True:
        username = input("Masukkan username baru: ")
        if username in cinephile:
            print("Username sudah digunakan. Coba lagi.")
        else:
            break

    password = input("Masukkan password baru: ")

    while True:
        user_role = input("Pilih role sebagai admin (A) atau user (U): ")
        if user_role.lower() == 'a':
            role = 'admin'
            break
        elif user_role.lower() == 'u':
            role = 'user'
            break
        else:
            print("Pilihan tidak valid. Harap pilih 'A' untuk admin atau 'U' untuk user.")

    print("Akun berhasil dibuat.")
    cinephile[username] = {
        'password': password,
        'role': role
    }
    return username

# Fungsi menu Rateboxd
def main():
    while True:
        print("\nSelamat datang di Rateboxd")
        print("(1) Sign in")
        print("(2) Register")
        print("(0) Keluar")

        choice = input("Pilihan Anda: ")

        if choice == '1':
            username = sign_in()
        elif choice == '2':
            username = register()
        elif choice == '0':
            print("Terima kasih sudah menggunakan Rateboxd! May the Force be with you!")
            break
        else:
            print("Pilihan tidak valid.")

        if username is not None:
            while True:
                print("\nMENU:")
                print("(1) Tambahkan Film")
                print("(2) Beri Rating")
                print("(3) Lihat Rating Film")
                print("(4) Ubah Rating")
                print("(5) Hapus Rating")
                print("(0) Sign out")

                choice = input("Pilihan Anda: ")

                if choice == '1':
                    if is_admin(username):
                        addFilm()
                    else:
                        print("Anda tidak memiliki izin untuk menambahkan film.")
                elif choice == '2':
                    rateFilm(username)
                elif choice == '3':
                    showRating()
                elif choice == '4':
                    editRating(username)
                elif choice == '5':
                    deleteRating(username)
                elif choice == '0':
                    break
                else:
                    print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()