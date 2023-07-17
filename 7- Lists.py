friends = ["Merve", "Melek", "Melike", "Barış"]  # sayı ve boolean da kullanabilirsin indexleri 0 1 2 3 diye gidiyor
friends[1] = "Ben"
print(friends[1:3])  # tersten de - kullanarak yazdırabiliyoruz

# List functions
lucky_numbers = [4, 8, 15, 16, 23, 43]
friends = ["sen", "ben", "o"]
friends.extend(lucky_numbers)  # listeleri birbirine ekleyebiliyoruz
friends.append("creed")  # listeye extra değer ekleyebiliyoruz
friends.insert(2, "Jack")  # araya değer ekleyebilmek için (ekleyeceğimiz sıra, "ekleyeceğimiz değer")
friends.remove("o")  # listeden eleman çıkarabiliyoruz
# friends.clear()  # listenin içindeki herşeyi siliyor
friends.pop()  # listedeki son elemanı siliyor 
print(friends)