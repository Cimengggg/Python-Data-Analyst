# tuple
INFO_KELAS = ("SMA Merdeka", "2026/2027")

# Set
MATA_PELAJARAN = {"Matematika", "Fisika", "Kimia"}

# list
DAFTAR_HADIR = ["Andi", "Budi", "Citra"]

# dictionary
DATA_SISWA = {
    "Andi" : {
        "Matematika" : 85,
        "Fisika" : 90,
        "Kimia" : 78
    },
    "Budi" : {
        "Matematika" : 80,
        "Fisika" : 85,
        "Kimia" : 88
    },
    "Citra" : {
        "Matematika" : 95,
        "Fisika" : 92,
        "Kimia" : 90
    }
}

print("========================================")
print("        LAPORAN AKADEMIK SEKOLAH"        )
print("========================================")

print(f"Sekolah : {INFO_KELAS[0]}")
print(f"Tahun Ajaran: {INFO_KELAS[1]}\n")

print("[ MATA PELAJARAN TERSEDIA ]")
print(f"{MATA_PELAJARAN}\n")

print(" [ URUTAN KEHADIRAN SISWA ] ");
for nomor, nama_siswa in enumerate(DAFTAR_HADIR, 1):
    print(f"{nomor}. {nama_siswa} ")

print("\n[ REKAP NILAI SISWA ]")
for DAFTAR_HADIR, nilai in DATA_SISWA.items():
    print(f"- {DAFTAR_HADIR} | Matematika: {nilai['Matematika']}, Fisika: {nilai['Fisika']}, Kimia: {nilai['Kimia']} ")

    print("========================================")