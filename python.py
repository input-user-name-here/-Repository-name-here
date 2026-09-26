import random
num = int(input("Podaj długość hasła."))
znaki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
haslo = ""

for i in range(num):
    random_num = random.randint(0,len(znaki)-1)
    haslo = haslo + znaki[random_num]
print(haslo)
