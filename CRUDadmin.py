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
    'Admin':{
        'password': 'admin',
        'role': 'admin'},
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
def lihat_review_film():
    showList()
    nomor_film = int(input("Pilih nomor film: ")) - 1
    if 0 <= nomor_film < len(cinema):
        judul_film = list(cinema.keys())[nomor_film]
        ulasan = cinema[judul_film]['review']
        for judul, data_film in cinema.items():
            print(f"Judul: {judul}")
            for ulasan in data_film['review']:
                print(f"Rating: {ulasan['rating']}")
                print(f"Komentar: {ulasan['comment']}")
                print(f"Username: {ulasan['username']}")
                print("---------------")

# Fungsi untuk memberi review film
def beri_review_film(username):
    judul_film = int(input("Masukkan judul film yang akan direview: "))
    film = list(cinema.keys)[judul_film]
    if judul_film in cinema:
        rating = int(input("Masukkan rating (1-10): "))
        comment = input("Masukkan komentar: ")
        cinema[judul_film]['review'].append({'username': username, 'rating': rating, 'comment': comment})
        print("Review film telah ditambahkan!")
    else:
        print("Judul film tidak ditemukan.")

# Fungsi untuk mengubah review film
def ubah_review_film(username):
    film = list(cinema.keys)
    judul_film = int(input("Masukkan nomor urut film yang reviewnya akan diubah: "))
    if judul_film in cinema:
        for review in cinema[judul_film]['review']:
            if review['username'] == username:
                new_rating = int(input("Masukkan rating baru (1-10): "))
                new_comment = input("Masukkan komentar baru: ")
                review['rating'] = new_rating
                review['comment'] = new_comment
                print("Review film telah diubah!")
                break
        else:
            print("Anda belum memberikan review untuk film ini.")
    else:
        print("Judul film tidak ditemukan.")

# Fungsi untuk menghapus review film
def hapus_review_film(username):
    judul_film = input("Masukkan judul film yang reviewnya akan dihapus: ")
    if judul_film in cinema:
        for review in cinema[judul_film]['review']:
            if review['username'] == username:
                cinema[judul_film]['review'].remove(review)
                print("Review film telah dihapus!")
                break
        else:
            print("Anda belum memberikan review untuk film ini.")
    else:
        print("Judul film tidak ditemukan.")

# Fungsi untuk menambahkan judul film
def tambah_judul_film():
    judul_film = input("Masukkan judul film yang akan ditambahkan: ")
    if judul_film not in cinema:
        cinema[judul_film] = {'review': []}
        print("Judul film telah ditambahkan!")
    else:
        print("Judul film sudah ada dalam daftar.")

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
                print("(2) Beri Review Film")
                print("(3) Ubah Review Film")
                print("(4) Hapus Review Film")
                print("(5) Tambah Judul Film")
                print("(0) Sign Out")

                pilihan = input("Masukkan pilihan: ")
                os.system('cls')
                if pilihan == "1":
                    lihat_review_film()
                elif pilihan == "2":
                    beri_review_film(username)
                elif pilihan == "3":
                    ubah_review_film(username)
                elif pilihan == "4":
                    hapus_review_film(username)
                elif pilihan == "5":
                    tambah_judul_film()
                elif pilihan == "0":
                    print("Anda telah keluar.")
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.")
        else:
            print("Anda bukan admin. Anda tidak memiliki akses ke Menu Admin.")
    else:
        print("Username atau password salah. Silakan coba lagi.")
