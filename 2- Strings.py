print("Melek\nMemiş")
print("Melek\"Memiş")
phrase = "sorma ne haldeyim "
print(phrase + "sorma kederdeyim")
print(phrase.isupper())  # upper lower tüm harflere etki ediyor.
print(phrase.upper())
print(phrase.upper().isupper())  # önce değiştirip sonra sorgulatabilirsin
print(len(phrase))  # string'in kaç karakterden oluştuğunu öğrenmek için
print(phrase[0])  # istediğin karakteri çekmek için
print(phrase.index("yim"))  # index karakterin konumunu tespit etmek için, birden fazla karakter yazınca ilk karakterin başladığı konumu veriyor
print(phrase.replace("sorma", "sor bak"))  # string içinde istediğimiz karakterleri değiştiriyor
