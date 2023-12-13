print('praktikum-d1')
print()
print('nama lengkap : Safa Ibrahim Satria')
print('nim          : 231031123')
print('prodi        : Sistem Informasi')

angkatan = 2023
print('angkatan adalah',angkatan)

print()
a= 20
print('Data adalah =',a)
print('Tipenya adalah =',type(a))

print()
b = 20.0
print('Data adalah =',b)
print('Tipenya adalah =',type(b))

print()
kampus = 'institut teknologi Bj Habibie'
print('Data adalah =',kampus)
print('Tipenya adalah =',type(kampus))

print()
log = True
print('Data adalah =',log)
print('Tipenya adalah =',type(log))

print()
c = complex(5,8)
print('Data adalah =',c)
print('Tipenya adalah =',type(c))

print()
p = 20
q = 5
hasil = p+q
print('hasil',p,'+',q,'adalah',hasil)

print()
p = 20
q = 5
hasil = p-q
print('hasil',p,'-',q,'adalah',hasil)

print()
p = 20
q = 5
hasil = p*q
print('hasil',p,'*',q,'adalah',hasil)

print()
p = 20
q = 5
hasil = p/q
print('hasil',p,'/',q,'adalah',hasil)

print()
p =3
q =2
hasil = p ** q
print('hasil',p,'^',q,'=',hasil)

print()
p =37
q =31
hasil = p % q
print('hasil',p,'%',q,'=',hasil)

print()
p =37
q =31
hasil = p // q
print('hasil',p,'//',q,'=',hasil)

print()
p =30
q =31
hasil = p // q
print('hasil',p,'//',q,'=',hasil)

print()
p = 20
q = 3
hasil = p/q
print('hasil',p,'/',q,'adalah',hasil)

print()
a = 20
print('Nilai a adalah', a)
a = a + 1   #ini perintah a = a + 1
print('Nilai a+=1 menjadi', a)

print()
a = 25
print('Nilai a adalah', a)
a -= 2 #ini perintah a = a - 2
print('Nilai a-=2 menjadi', a)

print()
a = 20
print('Nilai a adalah', a)
a *=2 #ini perintah a = a * 2
print('Nilai a*=2 menjadi', a)

print()
a = 20
print('Nilai a adalah', a)
a /= 5 #ini perintah a = a / 5
print('Nilai a/=2 menjadi', a)

print()
a = 20
print('Nilai a adalah', a)
a **=2 #ini perintah a = a ** 2
print('Nilai a**=2 menjadi', a)

print()
a = 20
print('Nilai a adalah', a)
a %=7 #ini perintah a = a % 7
print('Nilai a%=7 menjadi', a)

print()
a = 20
print('Nilai a adalah', a)
a //=7 #ini perintah a = a // 7
print('Nilai a//=7 menjadi', a)

print() #ini operasi OR
log =  True
print('Nilai log adalah',log)
log |= False  #ini perintah log= false log
print('Nilai log|= False menjadi', log)

print() #ini operasi AND
log =  True
print('Nilai log adalah',log )
log &= True  #ini perintah log= log & False
print('Nilai log&= true menjadi', log)

print() #ini operasi XOR
log =  True
print('Nilai log adalah',log )
log ^= True  #ini perintah log= log ^ False
print('Nilai log ^= true menjadi', log)

print() #ini operasi shifting
bi = 0b0100
print('Nilai bi =',format(bi,'04b'))
bi >>= 1 #menggeser digit ke kanan 1 kali
print('nilai bi >>=1 menjadi',format(bi,'04b'))

print() #ini operasi shifting
bi = 0b0100
print('Nilai bi =',format(bi,'04b'))
bi <<= 1 #menggeser digit ke kanan 1 kali
print('nilai bi <<=1 menjadi',format(bi,'04b'))

print()
a = 20 
hasil = a>15
print('hasil', a, '>15 adalah', hasil)

print()
a = 20 
hasil = a==15
print('hasil', a, '==15 adalah', hasil)

print()
print('\t\tTugas')
print('\tOperator Koperasi')

print()
a=9
b=8
c=14
d=7
print('Diketahui Bilangan\n a =',a,'\n b =',b,'\n c =',c,'\n d =',d)
print()

hasil=a<b
print('Perbadingan antara a<b adalah',hasil)

hasil=a>b
print('Perbadingan antara a>b adalah',hasil)

hasil=a<b>c
print('Perbadingan antara a<b>c adalah',hasil)

hasil=a>b<c
print('Perbadingan antara a<b>c adalah',hasil)

hasil=a>b<c
print('Perbadingan antara a<b>c adalah',hasil)

hasil=a>b<c
print('Perbadingan antara a<b>c adalah',hasil)

print()
a='apakah'
b='dia'
c='punya'
d='saya'
hasil=a is 'dia'

print('a adalah "aku"',hasil)

print('a tidak "aku"', a is not "aku" )

print(a,b,c,d,'ternyata', a is c)