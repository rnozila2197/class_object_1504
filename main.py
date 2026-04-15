# 1
class Kitob:
    def __init__(self, n, m):
        self.nomi = n
        self.muallif = m

kitob1 = Kitob("Otkan kunlar", "Abdulla Qodiriy")
print(kitob1.nomi, kitob1.muallif)

kitob2 = Kitob("Mehrobdan chayon", "Abdulla Qodiriy")
print(kitob2.nomi, kitob2.muallif)

# 2
class Talaba:
    def __init__(self, i, y):
        self.ism = i
        self.yosh = y

talaba1 = Talaba("Jamshid", 16)
print(talaba1.ism, talaba1.yosh)

talaba2 = Talaba("Jemfur", 17)
print(talaba2.ism, talaba2.yosh)

# 3
class Telefon:
    def __init__(self, m, n):
        self.model = m
        self.narx = n

telefon1 = Telefon("iPhone 13", 1200)
print(telefon1.model, telefon1.narx)

telefon2 = Telefon("Samsung S21", 900)
print(telefon2.model, telefon2.narx)

# 4
class Shahar:
    def __int__(self, n, a):
        self.nomi = n
        self.aholisi = a

shahar1 = Shahar("Toshkent", 3000000)
print(shahar1.nomi, shahar1.aholisi)

shahar2 = Shahar("Samarqand", 600000)
print(shahar2.nomi, shahar2.aholisi)

# 5
class Mashina:
    def __init__(self, m, r):
        self.marka = m
        self.rang = r

mashina1 = Mashina("Cobalt", "oq")
print(mashina1.marka, mashina1.rang)

mashina2 = Mashina("Malibu", "qora")
print(mashina2.marka, mashina2.rang)

mashina3 = Mashina("Nexia", "Kulrang")
print(mashina3.marka, mashina3.rang)

# 6
class Talaba:
    def __init__(self, ism, yosh, kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs

talaba1 = Talaba("Ali", 20, "2-kurs")
talaba2 = Talaba("Vali", 22, "3-kurs")

print(talaba1.ism, talaba1.yosh, talaba1.kurs)
print(talaba2.ism, talaba2.yosh, talaba2.kurs)

# 7
class Kitob:
    def __init__(self, n, m, s):
        self.nomi = n
        self.muallif = m
        self.sahifa_soni = s

kitob1 = Kitob("Otkan kunlar", "Abdulla Qodiriy", 300)
kitob2 = Kitob("Alkimyogar", "Paulo Coelho", 200)

print(kitob1.nomi, kitob1.muallif, kitob1.sahifa_soni)
print(kitob2.nomi, kitob2.muallif, kitob2.sahifa_soni)

# 8
class Telefon:
    def __init__(self, model, rang, narx):
        self.model = model
        self.rang = rang
        self.narx = narx

tel1 = Telefon("iPhone 13", "qora", 1200)
tel2 = Telefon("Samsung S21", "oq", 900)

print(tel1.model, tel1.rang, tel1.narx)
print(tel2.model, tel2.rang, tel2.narx)
# 9
class Mashina:
    def __init__(self, marka, rang, yili):
        self.marka = marka
        self.rang = rang
        self.yili = yili

m1 = Mashina("Cobalt", "oq", 2022)
m2 = Mashina("Malibu", "qora", 2023)

print(m1.marka, m1.rang, m1.yili)
print(m2.marka, m2.rang, m2.yili)

# 10
class Xodim:
    def __init__(self, ism, lavozim, maosh):
        self.ism = ism
        self.lavozim = lavozim
        self.maosh = maosh

x1 = Xodim("Ali", "Dasturchi", 1000)
x2 = Xodim("Vali", "Manager", 1500)
x3 = Xodim("Hasan", "Dizayner", 1200)

print(x1.ism, x1.lavozim, x1.maosh)
print(x2.ism, x2.lavozim, x2.maosh)
print(x3.ism, x3.lavozim, x3.maosh)
