INFO_KELAS = ("KELAS X-A", "Kurikulum Merdeka") # This is Tuple
MATA_PELAJARAN = {"Matematika", "Fisika", "Kimia"} # This is Sets
DAFTAR_HADIR = ["Andi", "Budi", "Citra"] #this is List
DATA_SISWA = {
    "Andi" : {"Matematika": 85, "Fisika": 90, "Kimia": 78},
    "Budi" : {"Matematika": 80, "Fisika": 85, "Kimia": 88},
    "Citra" : {"Matematika": 95, "Fisika": 92, "Kimia": 90}
}


# Informasi Kelas
print("=== INFORMASI KELAS ===")
print(f"Nama Kelas: {INFO_KELAS[0]}")
print(f"Kurikulum: {INFO_KELAS[1]} \n")

# Mata Pelajaran
print("=== MATA PELAJARAN (Set) ===")
print(f"Daftar Mapel Tersedia: {MATA_PELAJARAN} \n")

# Absensi Kelas
print("=== ABSENSI KELAS (List) ===")
print(f"Urutan Kehadiran: {DAFTAR_HADIR} \n")

# Rekap Nilai Siswa
print("=== REKAP NILAI SISWA (Dictionary) ===")
for DAFTAR_HADIR, nilai in DATA_SISWA.items():
    print(f"- {DAFTAR_HADIR} | Matematika: {nilai['Matematika']}, Fisika: {nilai['Fisika']}, Kimia: {nilai['Kimia']} ")
