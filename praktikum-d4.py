a=[2,3,1,0,3,1,1,2,3]
# akses item
print(a)
print(f'itemindeks-0 {a[0]}')
print(f'itemindeks-3 {a[3]}')
print(f'itemindeks:terakhir{a[len(a)-1]}')
# akses item indeks negatif
print(f'itemindeks:terakhir (-1) {a[-1]}')
print(f'itemindeks:pertama (-9) {a[-len(a)]}')
print(f'itemindeks:1 (-8) {a[-8]}')
print(f'itemindeks:5 (-4) {a[-4]}')
# akses indeks batas
print (f'item indeks:1,2,3 {a[1:4]}')
print (f'item indeks:1,2,... {a[1:]}')
print (f'item indeks:3,4,... {a[3:]}')
print (f'item indeks:0,1,2 {a[:3]}')
print (f'item indeks:0,1,2,3,4 {a[:5]}')
print(f'itemindeks:semua {a[:]}')
#pengirisan indeks
print(f'itemindeks:1,2,3 {a[1:4]}')
print(f'itemindeks:2,3,4 {a[2:5]}')
print(f'itemindeks:[1:8] {a[1:-1]}')

#nested list
kelas = [('pancasila',2),
         ('agama islam',2),
         ('pemrograman',3),
         ]
print(F'data kelas {kelas}')
kelas.append (('bahasa indonesia',2))
print (f'data kelas {kelas}')
kelas.append (('cinta',3))
print (f'data kelas {kelas}')


# nama mata kuliah 1 : matkul1 dengan jumlah sks : 2
print('nama mata  kuliah 1;',kelas [0][0],
      'dengan jumlah sks;',kelas [0][1])
# nama mata kuliah 2 : matkul2 dengan jumlah sks : 2
print('nama mata  kuliah 2;',kelas [1][0],
      'dengan jumlah sks;',kelas [1][1])
# nama mata kuliah 3 : matkul3 dengan jumlah sks : 3
print('nama mata  kuliah 3;',kelas [2][0],
      'dengan jumlah sks;',kelas [2][1])
# nama mata kuliah 4 : matkul4 dengan jumlah sks : 2
print('nama mata  kuliah 4;',kelas [3][0],
      'dengan jumlah sks;',kelas [3][1])
# nama mata kuliah 5 : matkul5 dengan jumlah sks : 3
print('nama mata  kuliah 4;',kelas [4][0],
      'dengan jumlah sks;',kelas [4][1])

data = [('Safa Ibrahim Satria',2023,'aktif'),
        (90,89,93,97,99),
        (20,22),
        ('SI-Reguler','Sistem Informasi D','ganjil')]

# nama mahasiswa : Safa Ibrahim satria 
print ('nama mahasiswa:', data [0][0])
# NIM Mahasiswa : 231031123
print('NIM Mahasiswa :',a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8])
#Program pendidikan Safa Ibrahim Satria: Sistem Informasi D S1-Reguler
print('Program Pendidikan',data [0][0],'adalah :',data [3][1],data[3][0])
#Angkatan : 2023-Ganjil
print('Angkatan :',data [0][1],'-',data[3][2])
#Jumlah nilai Safa Ibrahim Satria adalah: 5
print('Jumlah nilai',data [0][0],'adalah :',len(data[1]))
#Data terkecil Safa Ibrahim Satria adalah: 89
print('Data terkecil',data [0][0],'adalah :',min(data[1]))
#Data terbesar Safa Ibrahim Satria  adalah: 99
print('Data terbesar',data [0][0],'adalah :',max(data[1]))
#Rata-rata nilai Safa Ibrahim Satria adalah: 92.25
rata = sum(data[1])/len(data[1])
print('Rata-rata nilai',data [0][0],'adalah :',rata)
