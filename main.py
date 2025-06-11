


print("Hello User")

users = {
    "Uğur": "123456",
    "Ahmet": "987654",
    "Mehmet": "142536",
    "Şükrü": "172839"
}

    
attempts = 3 # giriş hakkı

while attempts > 0:
    username = input("Kullanıcı adınızı giriniz : ")
    password = input("Şifrenizi giriniz : ")
    
    if username in users and users[username] == password:
        print(f"Hoş geldiniz, {username}!")
        break # giriş başarılıysa göngüden çık
    else:
        attempts -= 1
        print(f"Hatalı giriş kalan deneme sayısı {attempts}")
        
        if attempts == 0:
            print("3 kez hatalı giriş yaptınız. Hesabınız kilitlendi.")
