biodata = {'nama'  : 'Safa Ibrahim satria', 
       'nim'   : '231031123',
       'asal'  : 'parepare',
       'umur': '19 tahun',
       'Alamat':'Btn lapadde Mas Blok H No 1',
       'universitas': 'institut teknologi Bj habibie',
       'prodi' : 'Sistem Informasi' }
       

print ('\n')
print((biodata['nama']),biodata['nim'],biodata['asal'])
print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:3])
print(selected_biodata)
