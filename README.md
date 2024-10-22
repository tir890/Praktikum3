# Pratikum 1 | Tipe data, Variable, dan Operator

Nama : Tiara Hayatul Khoir

Kelas : TI.24.A.5

NIM : 321410474

Mata Kuliah : Bahasa Pemrograman

## Mencari Bilangan Terbesar Dari Bilangan yang Diinputkan
Program ini menentukan bilangan terbesar dari serangkaian bilangan yang diinputkan hingga input 0. Program ini menggunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar yang ditemukan

## Flowchart 
![foto](https://github.com/tir890/foto/blob/be8bd72f0833d80a2f7fb17fc203c5f60e8c6199/code2flow_PCTQl5%20(1).png)

## Kode Program
```Python
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
```
## Penjelasan Kode Program

```Python
maxBilangan = float('-inf') 
count = 0
```
maxBilangan, diinisialisasi dengan nilai terkecil dalam representasi float, yaitu -inf, (negatif tak hingga). Ini dilakukan agar setiap bilangan yang dimasukkan pengguna nantinya pasti lebih besar dari maxBilangan, pada saat pertama kali dibandingkan.
count, diinisialisasi dengan 0, digunakan untuk menghitung berapa kali pengguna memasukkan bilangan (selain 0).
```Python
while True:
    print("Masukkan bilangan (0 untuk berhenti):")
    bilangan = int(input())
```
Loop ini berjalan terus menerus hingga pengguna memasukkan bilangan 0.
Pada setiap iterasi, pengguna diminta untuk memasukkan bilangan. Bilangan ini dibaca dengan input(), dan dikonversi menjadi tipe integer menggunakan int().
```Python
if bilangan == 0:
    break
```
Jika bilangan yang dimasukkan adalah 0, maka perulangan **berhenti** dengan perintah break. Ini digunakan sebagai tanda dari pengguna bahwa dia tidak ingin memasukkan bilangan lagi.
```Python
if bilangan > maxBilangan:
    maxBilangan = bilangan
```
Jika bilangan yang dimasukkan lebih besar daripada nilai maxBilangan, saat ini, maka nilai maxBilangan, diupdate dengan bilangan tersebut. Dengan cara ini, maxBilangan, selalu menyimpan bilangan terbesar yang telah dimasukkan.
```Python
count += 1
```
Setiap kali pengguna memasukkan bilangan (selain 0), nilai count, bertambah 1. Ini digunakan untuk melacak berapa banyak bilangan yang dimasukkan.
```Python
if count > 0:
    print("Bilangan terbesar adalah:", maxBilangan)
else:
    print("Tidak ada bilangan yang dimasukkan.")
```
Jika count > 0, artinya pengguna telah memasukkan setidaknya satu bilangan, dan program akan mencetak nilai bilangan terbesar yang telah ditemukan (maxBilangan).
Jika tidak ada bilangan yang dimasukkan (yaitu count == 0), maka program akan menampilkan pesan bahwa **tidak ada** bilangan yang dimasukkan.

## Hasil Kode Program
![foto](https://github.com/tir890/foto/blob/fd78231d4e00794d8830fe5cace89bf03a0614be/Screenshot%202024-10-22%20144622.png)
