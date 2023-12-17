import os
os.system('cls')

pwd_benar = 'si23d'
a = True
limit = 3
i = 0 

while a:
    i +=1
    pwd = input ('masukkan password: ')
    if pwd == pwd_benar:
        print('password benar! selamat anda login')
        a = False
    else:
        print('password salah')
        if i == limit:
             print('kesempatan anda habis!!')
             a= False
        else:
             print('kesempatan anda habis',limit-i)
             a = True



#tugas : buat password berlapis 3
#jika salah: pasword salah, anda gagal pada halaman 1
#jika salah: pasword salah, anda gagal pada halaman 2
#jika salah: pasword salah, anda gagal pada halaman 3
#jika benar : pasword benar, selamat datang di halaman 1
#jika benar : pasword benar, selamat datang di halaman 2
#jika benar : pasword benar, selamat berhasil login 

# tiap halaman memiliki kesempatan 3 kali memasukkan password 
