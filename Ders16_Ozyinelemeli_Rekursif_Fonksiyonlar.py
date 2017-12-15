print(">>>| Faktoriyel Hesaplama |<<<")
sayi=input(">>> Sayi giriniz! :")
sayi=int(sayi)
def faktoriyel(n):
    if(n==1):
        return 1
    else:
        return n*faktoriyel(n-1)

print(faktoriyel(sayi))
