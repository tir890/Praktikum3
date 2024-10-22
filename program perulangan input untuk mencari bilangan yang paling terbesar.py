maxBilangan = float('-inf')  
count = 0

while True:
    print("Masukkan bilangan (0 untuk berhenti):")
    bilangan = int(input())  

    if bilangan == 0:
        break  

    if bilangan > maxBilangan:
        maxBilangan = bilangan  

    count += 1 


if count > 0:
    print("Bilangan terbesar adalah:", maxBilangan)
else:
    print("Tidak ada bilangan yang dimasukkan.")
