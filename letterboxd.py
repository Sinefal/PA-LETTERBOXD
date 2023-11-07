import os

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
    'Admin': {
        'password': 'admin',
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

def showList():
    if not cinema:
        print("Tidak ada film di dalam daftar.")
        return

    for i, film in enumerate(cinema):
        print(f"{i + 1}. {film}")

# Fungsi untuk menampilkan review film
def lihat_review_film(username):
    showList()
    nomor_film = float(input("Pilih nomor film: ") - 1)
    if 0 <= nomor_film < len(cinema):
        judul_film = list(cinema.keys())[nomor_film]
        ulasan = cinema[judul_film]['review']
        for ulasan in ulasan:
            print(f"Judul: {judul_film}")
            print(f"Rating: {ulasan['rating']}")
            print(f"Komentar: {ulasan['comment']}")
            print(f"Username: {ulasan['username']}")
            print("---------------")

# Fungsi untuk menghapus review film
def hapus_review_film():
    showList()
    nomor_film = int(input("Pilih nomor film: ") - 1)
    if 0 <= nomor_film < len(cinema):
        judul_film = list(cinema.keys())[nomor_film]
        ulasan = cinema[judul_film]['review']
        print("\nUlasan untuk film", judul_film, ":")
        for i, review in enumerate(ulasan):
            print(f"{i + 1}. Username: {review['username']}, Rating: {review['rating']}, Komentar: {review['comment']}")
        nomor_ulasan = int(input("Pilih nomor ulasan yang akan dihapus: ") - 1)
        if 0 <= nomor_ulasan < len(ulasan):
            del ulasan[nomor_ulasan]
            print("Ulasan film telah dihapus!")
        else:
            print("Nomor ulasan tidak valid.")
    else:
        print("Nomor film tidak valid.")

# Fungsi untuk menambahkan judul film
def tambah_judul_film():
    judul_film = input("Masukkan judul film yang akan ditambahkan: ")
    if judul_film not in cinema:
        cinema[judul_film] = {'review': []}
        print("Judul film telah ditambahkan!")
    else:
        print("Judul film sudah ada dalam daftar.")

# Fungsi untuk mengubah judul film
def ubah_judul_film():
    showList()
    nomor_film = int(input("Pilih nomor film: ") - 1)
    if 0 <= nomor_film < len(cinema):
        judul_film = list(cinema.keys())[nomor_film]
        new_judul_film = input("Masukkan judul film baru: ")
        cinema[new_judul_film] = cinema.pop(judul_film)
        print("Judul film telah diubah!")
    else:
        print("Nomor film tidak valid.")

# Fungsi untuk menghapus judul film
def hapus_judul_film():
    showList()
    nomor_film = int(input("Pilih nomor film: ") - 1)
    if 0 <= nomor_film < len(cinema):
        judul_film = list(cinema.keys())[nomor_film]
        del cinema[judul_film]
        print("Judul film telah dihapus!")

# Menu utama
while True:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    os.system('cls')
    if username in cinephile and password == cinephile[username]['password']:
        role = cinephile[username]['role']

        if role == 'admin':
            while True:
                print("\nMenu Admin")
                print("(1) Lihat Review Film")
                print("(2) Hapus Review Film")
                print("(3) Tambah Judul Film")
                print("(4) Ubah Judul Film")
                print("(5) Hapus Judul Film")
                print("(0) Sign Out")

                pilihan = input("Masukkan pilihan: ")
                os.system('cls')
                if pilihan == "1":
                    lihat_review_film(username)
                elif pilihan == "2":
                    hapus_review_film()
                elif pilihan == "3":
                    tambah_judul_film()
                elif pilihan == "4":
                    ubah_judul_film()
                elif pilihan == "5":
                    hapus_judul_film()
                elif pilihan == "0":
                    print("Anda telah keluar.")
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.")
        else:
            print("Anda bukan admin. Anda tidak memiliki akses ke Menu Admin.")
    else:
        print("Username atau password salah. Silakan coba lagi.")
