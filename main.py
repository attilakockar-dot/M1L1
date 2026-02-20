meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "BRUH": "Ciddi misin ya, of ya gibi bir tepki.",
            "BASED":"Birinin fikrini özgüvenli ve umursamadan söylemesini övmek için kullanılır."
            }

word = input("Anlamadığınız bir kelime yazın").upper()

if word in meme_dict:
    print(meme_dict[word])
else:
    print("Hatalı girdi")
