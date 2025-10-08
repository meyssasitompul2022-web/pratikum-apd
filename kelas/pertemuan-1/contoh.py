users = {
        "mey": "2501",
        "mel": "2222"
}

username = input("masukan username: ")
password = input("masukan password: ")

if username in users and users[username] == password:
    print("selamat datang di program kami")
else:
    print("username atau password salah! silahkan coba lagi")