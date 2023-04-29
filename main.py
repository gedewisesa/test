meme_dict = { 
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO": "untuk menjadi agresif/marah"
            }

for i in range(5):           
    word = input("kata gaul apa yang kamu masih bingung?(GUNAKAN HURUF KAPITAL)")
    if word in meme_dict.keys():
        # Apa yang harus kita lakukan jika kata itu ditemukan?
        print(meme_dict[word])
    else:
        print("kata yang anda masukkan tidak ada dalam dictionary")
        # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
