
# [#26] - [Remove Duplicated From Sorted Array]

## 1. Problem Overview
- Platform: LeetCode
- Difficulty: Easy
- Topic: Array
- Algorithm: Two Pointers
- Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array

## 2. Problem Summary
Diberikan sebuah array integer yang sudah terurut secara ascending. Tugas kita adalah menghapus elemen duplikat secara in-place, mempertahankan urutan elemen unik, dan mengembalikan jumlah elemen unik yang tersisa.


## 3. Input & Output
- Input: nums = [1,1,2]

- Output: 2 , nums = [1,2,___]
Penjelasan: Angka diurutkan dari terkecil ke terbesar. Elemen duplikat harus dihilangkan dari bagian awal array yang berisi elemen unik. Elemen setelah indeks k - 1 tidak perlu diperhatikan.
## Constraints:
- 1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100

## 4. Example
Tuliskan contoh input, output, dan penjelasannya.
 input : nums = [1,1,2,3,3,4,4,5]
 output : k = 5 nums = [1,2,3,4,5,....]
 Penjelasan: k bernilai berapa banyak nilai unik yang terdapat di dalam list yang dihitung dari index pertama hingga index terakhir yang menampung elemen unik dari index sebelumnya.
 Setiap elemen harus diurutkan secara ascending dan jika ada duplikat harus dibuang atau digeser ke index akhiran. Tanda titik mengindikasikan kita tidak peduli pada nilai setelah elemen unik habis.

## 5. Approach & Reasoning
- Apa pola masalahnya?
In-place Array Modification menggunakan Two Pointers.
Kita mempertahankan elemen unik di bagian depan array, sambil memeriksa elemen berikutnya.

- Mengapa memilih algoritma ini?
Kita membutuhkan satu pointer untuk menunjuk elemen yang sekarang dicek dan pointer kedua untuk menyimpan index 
elemen terakhir yang unik. Selain itu,pointer kedua berguna untuk menyiapkan index jika pointer pertama menemukan elemen unik lainnya.

- Bagaimana algoritma bekerja?
 - Buat satu pointer untuk mengecek seluruh elemen list menggunakan index satu-persatu,bisa menggunakan perulangan for loop,anggap bernama fast.
 - Buat satu pointer untuk menyimpan index elemen unik pertama untuk dibandingkan dengan elemen yang ditunjuk pointer pertama,anggap bernama slow.
 - Buat variabel untuk menyimpan berapa banyak elemen unik yang sudah ditemukan.
 - Jika menemukan elemen unik,artinya ketika nilai pada indeks yang ditunjuk fast berbeda dari nilai pada indeks yang ditunjuk slow, berarti ditemukan elemen unik baru. geser index pointer penyimpan elemen unik,overwrite posisi elemennya dengan elemen yang sedang ditunjuk pointer sekarang dan tambah nilai variabel penyimpan jumlah elemen unik.

 - Ulangi sampai semua elemen list dicek.

- Mengapa pendekatan ini benar?

Array sudah terurut, sehingga nilai yang sama selalu berdekatan.

Kita cukup membandingkan nilai saat ini dengan nilai unik terakhir yang disimpan untuk mengetahui apakah ditemukan elemen unik baru.

Setiap elemen unik ditempatkan pada posisi berikutnya di bagian depan array, sehingga urutan elemen tetap terjaga dan tidak ada duplikasi dalam bagian tersebut.

Karena posisi pointer sebelum hanya bertambah ketika ditemukan elemen unik, bagian depan array akan selalu berisi elemen unik tanpa duplikasi dan tetap mempertahankan urutan aslinya.

## 6. Implementation
Referensi file Python:
`[26-remove-duplicated-from-sorted-array].py`

## 7. Complexity Analysis
- Time Complexity: O(n)
    Setiap elemen diperiksa sehingga time bergantung pada seberapa banyak elemen di dalam list.
- Space Complexity:
    - Auxiliary space: O(1)
    - Output Space: O(1)
    - Total Space: O(1)

Kita tidak membuat array baru.
Kita memodifikasi array input secara langsung.
Pointer dan variabel tambahan jumlahnya tetap, tidak bertambah mengikuti ukuran input.


## 8. Edge Cases
 Kondisi semua elemen list unik

 Ketika semua elemen list unik,setiap perulangan akan selalu menambah nilai variabel penyimpan jumlah elemen unik sehingga nilainya sama dengan panjang dari list itu sendiri, k = len(nums)

 Kondisi ketika semua elemen duplikat

 Ketika semua elemen duplikat,kondisi if tidak akan berjalan sehingga variabel penyimpan jumlah elemen unik tidak akan berubah sampai pengecekan berakhir. k = 1.

 Kondisi hanya ada satu elemen
Ketika list hanya memiliki satu elemen, perulangan tidak akan dijalankan karena tidak ada elemen berikutnya yang perlu diperiksa. Elemen pertama sudah dianggap unik sejak awal sehingga k = 1.

## 9. Lessons Learned

Memahami penggunaan Two Pointers untuk memeriksa dan memodifikasi array secara in-place.
Memahami bagaimana mempertahankan elemen unik di bagian depan array menggunakan overwrite.
Memahami bagaimana memanfaatkan sifat sorted array untuk mendeteksi duplikasi tanpa menggunakan struktur data tambahan seperti set.

\
