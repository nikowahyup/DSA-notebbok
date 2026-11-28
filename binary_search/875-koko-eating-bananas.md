
# [Problem Number] - [Problem Title]

## 1. Problem Overview
- Platform: LeetCode
- Difficulty: Medium
- Topic: Binary Search
- Algorithm: Binary Search on Answer
- Problem Link: https://leetcode.com/problems/koko-eating-bananas/

## 2. Problem Summary
Diberikan sebuah list piles yang berisi angka integer positif. Setiap elemen merepresentasikan jumlah pisang dalam satu tumpukan.

Koko dapat memilih satu tumpukan pisang dan memakannya dengan kecepatan k pisang per jam. Jika pisang dalam tumpukan tersebut belum habis dalam satu jam, Koko dapat melanjutkan memakan sisanya pada jam berikutnya. Koko hanya boleh memakan satu tumpukan dalam satu jam.

Diberikan batas waktu h jam, tugas kita adalah mencari kecepatan minimum k yang memungkinkan Koko menghabiskan seluruh tumpukan pisang tepat pada atau sebelum batas waktu tersebut.

## 3. Input & Output
- Input: piles = [3,6,7,11], h = 8. piles -> list, h -> int
- Output: k = 4, k -> int


## Constraints:
    1 <= piles.length <= 104
    piles.length <= h <= 109

## 4. Example
- Input: piles = [3,6,7,11], h = 8
- Output: k = 4
    Jika Koko memakan 4 pisang per jam, dia membutuhkan waktu 1 jam untuk menghabiskan tumpukan pertama (3 pisang), 2 jam untuk tumpukan kedua (6 pisang), 2 jam untuk tumpukan ketiga (7 pisang), dan 3 jam untuk tumpukan keempat (11 pisang).

    Total waktu yang dibutuhkan adalah 1 + 2 + 2 + 3 = 8 jam. Dengan demikian, k = 4 merupakan kecepatan minimum yang memungkinkan Koko menghabiskan seluruh pisang dalam batas waktu yang diberikan.

## 5. Approach & Reasoning
- Apa pola masalahnya?
    Permasalahan ini memiliki hubungan monotonik antara kecepatan makan (k) dan total waktu yang dibutuhkan untuk menghabiskan seluruh pisang.

    Semakin kecil nilai k, semakin besar atau sama total waktu yang dibutuhkan.

    Semakin besar nilai k, semakin kecil atau sama total waktu yang dibutuhkan.

- Mengapa memilih algoritma ini?

    Kita memiliki rentang kecepatan makan dari 1 hingga jumlah maksimal pisang dalam satu tumpukan. Setiap kecepatan k dapat diuji satu per satu untuk menghitung total waktu yang dibutuhkan Koko dalam menghabiskan seluruh pisang. Namun, pendekatan tersebut membutuhkan pengujian sebanyak jumlah pilihan kecepatan yang tersedia.

    Dengan Binary Search, kita dapat mempersempit ruang pencarian berdasarkan hasil pengujian kecepatan tengah dari rentang yang tersedia. Jika total waktu melebihi batas yang ditentukan, kita mencari kecepatan yang lebih tinggi. Sebaliknya, jika total waktu memenuhi batas tersebut, kita mencari kemungkinan kecepatan yang lebih rendah.

    Pendekatan ini memungkinkan kita menemukan kecepatan minimum tanpa harus menguji seluruh kemungkinan kecepatan satu per satu.
- Bagaimana algoritma bekerja?
    - Kita perlu menyiapkan batas bawah dan atas kecepatan makan koko.
    - Buat variabel kiri untuk menyimpan batas bawah kecepatan makan koko. Untuk nilai awalnya 1.
    - Buat variabel kanan untuk menyimpan batas atas kecepatan makan koko. Untuk nilai awalnya sesuai dengan jumlah maksimal pisang dalam satu tumpukan,konsepnya max(piles).

    - buat variabel tengah untuk menyimpan kecepatan yang akan diuji pada setiap iterasi. Kecepatan ini didapat dari penjumlahan batas bawah dan atas yang kemudian dibagi menggunakan pembagian bilangan bulat.

    - Siapkan variabel penyimpan total waktu yang diperlukan jika koko makan dengan kecepatan tengah tersebut,sebut saja total_jam.

    - Mulai iterasi yang menghitung waktu koko memakan setiap tumpukan pisang dan simpan ke variabel total_jam.
    - Bandingkan total_jam dengan h.
    - Jika total_jam masih lebih besar dari h,geser batas bawah.
    - Jika total jam lebih kecil atau sama dengan h,geser batas atas.
    - Iterasi ini akan terus berjalan selama kiri lebih kecil atau sama dengan kanan, kiri <= kanan.

catatan:Untuk menghitung waktu setiap tumpukan, kita menggunakan pembagian yang dibulatkan ke atas (ceiling division). Hal ini diperlukan karena Koko tetap membutuhkan satu jam penuh untuk menghabiskan sisa pisang pada jam terakhir.

- Mengapa pendekatan ini benar?
    Sifat monotonik pada kecepatan makan
        Semakin cepat kecepatan makannya semakin sedikit total waktu yang dibutuhkan koko untuk menghabiskan pisang.

    Cara binary search memanfaatkan konsep monotonik
        ketika kecepatan tengah tidak memenuhi batas waktu,artinya seluruh kecepatan di bagian kiri juga tidak akan memenuhi,kita bisa persempit dengan mengeliminasi seluruh kemungkinan di sebelah kiri.
        Jika kecepatan tengah memenuhi batas waktu, kecepatan tersebut valid, tetapi kita masih perlu memeriksa apakah ada kecepatan lebih rendah yang juga valid.


## 6. Implementation
Referensi file Python:
`[875-koko-eating-bananas].py`

## 7. Complexity Analysis
- Time Complexity: O(n log m)
    n adalah jumlah tumpukan pisang dalam piles.
    m adalah jumlah pisang terbanyak dalam satu tumpukan, yaitu max(piles).

- Space Complexity: O(1)
    Tidak ada struktur data tambahan,kita hanya menggunakan beberapa variabel konstan.


## 8. Edge Cases
     - Hanya ada satu tumpukan
     - Kecepatan minimum 1
     - Kecepatan maksimum 
     - Ukuran tumpukan sama

## 9. Lessons Learned
    Mempelajari variasi penerapan Binary Search on Answer. Berbeda dengan binary seach pada array terurut,kita menggunakan rentang kemungkinan untuk mendapatkan jawaban.
