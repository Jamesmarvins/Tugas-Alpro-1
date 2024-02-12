from decimal import Decimal

emas_1 = 25
harga_beli_1 = Decimal('650000')
harga_jual_1 = Decimal('685000')

laba1_rp = int(emas_1 * harga_jual_1 - emas_1 * harga_beli_1)
laba1_persen = float((laba1_rp * 100) / (emas_1 * harga_beli_1))
print(f"Berat Emas: {emas_1} gram")
print(f"Keuntungan dalam Rupiah: {laba1_rp} Rupiah")
print(f"Keuntungan dalam persen: {laba1_persen}%")
print()

beli_tambah = 15
emas_2 = emas_1 + beli_tambah
harga_beli_2 = Decimal('685000')
harga_jual_2 = Decimal('715000')

laba2_rp = int((emas_2 * harga_jual_2) - (emas_1 * harga_beli_1) - (beli_tambah * harga_beli_2))
laba2_persen = float((laba2_rp * 100) / ((emas_1 * harga_beli_1) + (beli_tambah * harga_beli_2)))
print(f"Berat Emas: {emas_2} gram")
print(f"Keuntungan dalam Rupiah: {laba2_rp} Rupiah")
print(f"Keuntungan dalam persen: {laba2_persen}%")