uangpertama = 200000000
bunga = 10
t = 0
while uangpertama <= 400000000:
    t = t + 1
    uangpertama = float (uangpertama * ((100 + bunga) / 100))
    
B1 = float(round(uangpertama))
print (f"Perlu waktu {t} tahun untuk merubah Rp.200000000 menjadi Rp {B1}")