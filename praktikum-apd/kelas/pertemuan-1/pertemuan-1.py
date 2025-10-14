print("Hello World")
nama = str(input("nama mu"))
nim = int(input("nim kamu"))

biayalangganan = 1500000

paket = {
    "1": {
        "nama": "Bronze",
        "admin": 0.01,
        "keuntungan": "Akses dasar ke lagu-lagu populer." },
    "2": {"nama": "Silver",
        "admin": 0.03,
        "keuntungan": "Akses lagu premium dan playlist kustom."},
    "3": {"nama": "Gold",
        "admin": 0.05,
        "keuntungan": "Akses lagu premium, playlist kustom, dan mode offline."},
    "4": {"nama": "Platinum",
         "admin" : 0.07,
        "keuntungan": "Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis." }
}

totalbayar = biayalangganan + (biayalangganan * paket)