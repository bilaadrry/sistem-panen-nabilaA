def hitung_total_panen(berat_panen):
    return sum(berat_panen)

def hitung_diskon(total_harga, persen_diskon=10):
    return total_harga - (total_harga * persen_diskon / 100)

panen_harian = [120, 100, 140, 110, 105]
harga_per_kg = 15000

total_berat = hitung_total_panen(panen_harian)
total_biaya = total_berat * harga_per_kg

print(f"Total hasil panen: {total_berat} kg")
print(f"Total setelah diskon: Rp{hitung_diskon(total_biaya):,.0f}")
