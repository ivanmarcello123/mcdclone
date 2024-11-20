def hitung_3_variabel(p=None, l=None, t=None):
    # Mengecek apakah ketiga variabel ada
    if p is not None and l is not None and t is not None:
        # Menghitung Volume Balok
        volume = p * l * t
        # Menghitung Luas Permukaan Balok
        luas_permukaan = 2 * (p * l + p * t + l * t)
        return volume, luas_permukaan
    else:
        return None, None

def hitung_2_variabel(p=None, l=None):
    # Mengecek apakah panjang dan lebar diberikan
    if p is not None and l is not None:
        # Menghitung Keliling
        keliling = 2 * (p + l)
        # Menghitung Luas
        luas = p * l
        return keliling, luas
    else:
        return None, None

def hitung(p=None, l=None, t=None):
    if p is not None and l is not None and t is not None:
        # Memanggil fungsi untuk 3 variabel (volume dan luas permukaan)
        volume, luas_permukaan = hitung_3_variabel(p, l, t)
        if volume is not None:
            print(f"Volume Balok: {volume} cubic units")
            print(f"Luas Permukaan Balok: {luas_permukaan} square units")
    elif p is not None and l is not None:
        # Memanggil fungsi untuk 2 variabel (keliling dan luas)
        keliling, luas = hitung_2_variabel(p, l)
        if keliling is not None:
            print(f"Keliling: {keliling} units")
            print(f"Luas: {luas} square units")
    else:
        print("Variabel yang dimasukkan tidak lengkap!")

# Fungsi untuk input manual
def input_data():
    print("Masukkan data untuk perhitungan:")

    # Input panjang dan lebar, dan tinggi (jika ada)
    p = float(input("Masukkan panjang (p): "))
    l = float(input("Masukkan lebar (l): "))

    # Tanyakan apakah pengguna ingin menginput tinggi
    t_input = input("Apakah Anda ingin memasukkan tinggi (t)? (y/n): ").strip().lower()

    if t_input == 'y':
        t = float(input("Masukkan tinggi (t): "))
        hitung(p, l, t)
    else:
        hitung(p, l)

# Menjalankan fungsi input dan perhitungan
input_data()
