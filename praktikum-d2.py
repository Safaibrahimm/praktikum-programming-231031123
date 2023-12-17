print('praktikum-d2')
print()
print('nama lengkap : Safa Ibrahim Satria')
print('nim          : 231031123')
print('prodi        : Sistem Informasi')
print('angkatan     : 2023\n\n')

print('praktikum-2')
print('=========================IN AND =========================')
print()
a=True
b=False
hasil=a and a
print('Nilai',a,'and',a,'adalah',hasil)

hasil=a and b
print('Nilai',a,'and',b,'adalah',hasil)

hasil=b and b
print('Nilai',b,'and',b,'adalah',hasil)

hasil=b and a
print('Nilai',b,'and',a,'adalah',hasil)
print('=========================IN OR =========================')
hasil=a or a
print('Nilai',a,'or',a,'adalah',hasil)

hasil=a or b
print('Nilai',a,'or adalah',hasil)

hasil=b or b
print('Nilai',b,'or',b,'adalah',hasil)

hasil=b or a
print('Nilai',b,'or',a,'adalah',hasil)
print('=========================IN NOT =========================')
hasil= not a
print('Nilai not',a,'adalah',hasil)
hasil= not b
print('Nilai not',b,'adalah',hasil)
print('=========================IN XOR =========================')
hasil=a ^ a
print('Nilai',a,'XOR',a,'adalah',hasil)

hasil=a ^ b
print('Nilai',a,'XOR adalah',hasil)

hasil=b ^ b
print('Nilai',b,'XOR',b,'adalah',hasil)

hasil=b ^ a
print('Nilai',b,'XOR',a,'adalah',hasil)
print('=========================IN Nand =========================')
hasil=not (a and a)
print('Nilai',a,'nand',a,'adalah',hasil)

hasil=not (a and b)
print('Nilai',a,'nand',b,'adalah',hasil)

hasil=not (b and b)
print('Nilai',b,'nand',b,'adalah',hasil)

hasil=not (b and a)
print('Nilai',b,'nand',a,'adalah',hasil)
print('=========================IN nor =========================')
hasil=not (a and a)
print('Nilai',a,'nor',a,'adalah',hasil)

hasil=not (a and b)
print('Nilai',a,'nor',b,'adalah',hasil)

hasil=not (b and b)
print('Nilai',b,'nor',b,'adalah',hasil)

hasil=not (b and a)
print('Nilai',b,'nor',a,'adalah',hasil)

print('=========================IN nxor =========================')
hasil=not (a and a)
print('Nilai',a,'nxor',a,'adalah',not hasil)

hasil=not (a and b)
print('Nilai',a,'nxor',b,'adalah',not hasil)

hasil=not (b and b)
print('Nilai',b,'nxor',b,'adalah',not hasil)

hasil=not (b and a)
print('Nilai',b,'nxor',a,'adalah',not hasil)

print('========================= Is')
a= 5
b= 6
print('nilai',a,'memilki identitas=',hex(id(a)))
print('nilai',b,'memilki identitas=',hex(id(b)))
hasil = a is b
print('a is b=',hasil)
a=6
b=6
print('nilai',a,'memilki identitas=',hex(id(a)))
print('nilai',b,'memilki identitas=',hex(id(b)))
hasil = a is b
print('a is b=',hasil)

print('========================= IS NOT')
a= 5
b= 6
print('nilai',a,'memilki identitas=',hex(id(a)))
print('nilai',b,'memilki identitas=',hex(id(b)))
hasil = a is b
print('a is not b=',hasil)
a=6
b=6
print('nilai',a,'memilki identitas=',hex(id(a)))
print('nilai',b,'memilki identitas=',hex(id(b)))
hasil = a is b
print('a is not b=',hasil)

print('\n========================= IN')
nama = 'Baharuddin jusuf habibie'
test = 'rud'
cek = test in nama 
print(test,'terdapat di',nama, 'adalah '+str (cek))

test = 'bach'
cek = test in nama 
print(test,'terdapat di',nama, 'adalah '+str (cek))

test = 'ib'
cek = test in nama 
print(test,'terdapat di',nama, 'adalah '+str (cek))

test = 'a'
cek = test in nama 
print(test,'terdapat di',nama, 'adalah '+str (cek))

test = 'i'
cek = test in nama 
print(test,'terdapat di',nama, 'adalah '+str (cek))

test = 'u'
cek = test in nama 
print(test,'terdapat di',nama, 'adalah '+str (cek))

test = 'e'
cek = test in nama 
print(test,'terdapat di',nama, 'adalah '+str (cek))

test = 'o'
cek = test in nama 
print(test,'terdapat di',nama, 'adalah '+str (cek))


print('\n========================= IN')
data = ['institut',
        'teknologi',
        'Bacharudding',
        'yusuf',
        'habibie']
print('data adalah' , data)
test1 = 'habibie'
test2 = 'parepare'
test3 = 'kampus' 
test4 = 'institut'

cek = test1 in data 
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 in data 
print(test2,'terdapat di data adalah '+str(cek))
cek = test3 in data 
print(test3,'terdapat di data adalah '+str(cek))
cek = test4 in data 
print(test4,'terdapat di data adalah '+str(cek))

print('\n========================= not in')
# tugas buat nama menjadi nama lengkap masing2
#tugas dengan cara yang sama buat operator untuk not in

# Ini operator bitwise 
a = 5 # tanggal lahir 
b = 10 # bulan lahir
b += 80
print('\n========================= AND')
print('nilai',a ,'dalam biner    = ',format(a,'08b'))
print('nilai',b ,'dalam biner   = ',format(b,'08b'))
print('===========================================AND')
c = a & b
print ('nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))

print('\n========================= OR')
print('nilai',a ,'dalam biner    = ',format(a,'08b'))
print('nilai',b ,'dalam biner   = ',format(b,'08b'))
print('===========================================AND')
c = a | b
print ('nilai',a,'|',b,'dalam biner adalah',format(c,'08b'))

# tugas untuk operator xor c= a^b
# tugas untuk operator not c = ~a
# tugas untuk operator not c = ~b
# tugas untuk operator geser kanan  c =a >> 2
# tugas untuk operator geser kiri  c =a << 2
# tugas untuk operator not and c = ~(a&B)
# tugas untuk operator not or c = ~(a|B)
# tugas untuk operator 
