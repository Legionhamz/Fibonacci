# Fibonacci

# sayac = int(input("bir sayi giriniz: "))

# a, b = 0,1

# toplam = a + b

# print(a)                # ilk olarak 0 1 1 yazdırıyor.
# print(b)
# print(toplam)

# for i in range(sayac-3):         # buradaki dögü ile kaç sayı yazdırıcağını belirtiyor
#     a = b
#     b = toplam
#     toplam = a+b
#     print(toplam)


# ==============  VEYA ===>

# def fibonacci(x):
#     if x <= 1:                          # burası'da aynı ama işlemleri fonksiyonun içerisinde yapıyor
#         return x

#     else:
#         return fibonacci(x-1) + fibonacci(x-2)

# tekrar = int(input("kaç defa tekrar etsin: "))

# for j in range(tekrar):
#     print(fibonacci(j))

