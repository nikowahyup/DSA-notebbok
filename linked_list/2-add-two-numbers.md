
# [#2] - [Add two Numbers]

## 1. Problem Overview
- Platform: LeetCode
- Difficulty: Medium
- Topic: Linked List
- Algorithm: Linked List Traversal,Elementary Addition with Carry
- Problem Link: https://leetcode.com/problems/add-two-numbers

## 2. Problem Summary
Diberikan dua Singly Linked List, yaitu l1 dan l2 yang masing-masing merepresentasikan sebuah bilangan bulat non-negatif.

Setiap node menyimpan satu digit angka, dengan urutan digit terbalik (reverse order). Tugas kita adalah menjumlahkan kedua bilangan tersebut dan menyimpan hasilnya dalam sebuah Linked List baru dengan format yang sama.

Setiap node pada Linked List hasil menyimpan satu digit dari hasil penjumlahan.

## 3. Input & Output

- Input: l1 = [2,4,3], l2 = [5,6,4]
- Output: [7,0,8]
Penjelasan: 342 + 465 = 807.

## Constraints:
- Jumlah node di masing-masing linked list di rentang [1, 100]
- 0 <= Node.val <= 9

## 4. Example
    l1 = 3 --> 4 --> 5
    l2 = 1 --> 2 --> 6
    hasil = 4 --> 6 --> 1 --> 1

Penjelasan:
Tiap nilai dari node dijumlahkan dan hasilnya digunakan untuk value node hasil,contoh 3 + 1 = 4.


## 5. Approach & Reasoning
- Apa pola masalahnya?
Soal ini merupakan simulasi penjumlahan dua bilangan yang direpresentasikan menggunakan linked list.

Setiap node menyimpan satu digit dalam urutan terbalik, sehingga kita dapat melakukan penjumlahan langsung dari head ke tail tanpa perlu mengubah linked list menjadi integer.

Proses penjumlahan dilakukan digit demi digit dengan memperhitungkan carry, kemudian setiap hasil digit digunakan untuk membentuk linked list baru.

- Mengapa memilih algoritma ini?
Penjumlahan dilakukan dari digit paling kanan (satuan) menuju digit paling kiri karena linked list yang diberikan menyimpan digit dalam urutan terbalik.

Urutan ini sesuai dengan karakteristik singly linked list yang hanya memungkinkan traversal maju dari head menuju tail.

Dengan demikian, kita dapat melakukan penjumlahan digit demi digit sekaligus meneruskan carry ke node berikutnya tanpa perlu membalik linked list atau menggunakan struktur data tambahan.

- Bagaimana algoritma bekerja?
1. Inisialisasi dummy node sebagai titik awal untuk membangun linked list hasil.
2. Inisialisasi pointer `current` untuk menyambungkan node hasil dan `carry` untuk menyimpan nilai puluhan dari penjumlahan sebelumnya.
3. Gunakan `while` untuk melakukan traversal selama salah satu linked list masih memiliki node atau carry belum bernilai 0.
4. Ambil value dari masing-masing node. Jika salah satu linked list sudah habis, gunakan nilai 0.
5. Jumlahkan kedua value beserta carry sebelumnya.
6. Gunakan modulo 10 untuk mendapatkan digit hasil dan floor division untuk mendapatkan carry berikutnya.
7. Buat node baru berdasarkan digit hasil, kemudian sambungkan ke linked list menggunakan `current`.
8. Pindahkan pointer `l1` dan `l2` jika masih memiliki node.
9. Kembalikan `dummy.next` sebagai linked list hasil

- Mengapa pendekatan ini benar?
Pendekatan ini sesuai dengan kebutuhan soal karena:

Penjumlahan dilakukan langsung pada value setiap node tanpa mengubah representasi linked list menjadi integer.

Traversal dari head ke tail sesuai dengan urutan digit terbalik yang diberikan soal.

Penggunaan carry memastikan hasil penjumlahan setiap digit tetap akurat.

Dummy node dan pointer current memungkinkan kita membangun linked list hasil secara berurutan.

Kondisi loop memastikan seluruh digit dan carry terakhir tetap diproses, termasuk ketika kedua linked list memiliki panjang berbeda.

Dengan demikian, pendekatan ini memenuhi kebutuhan soal untuk menghasilkan linked list baru yang merepresentasikan hasil penjumlahan kedua bilangan.

## 6. Implementation
Referensi file Python:
`[2-add-two-numbers].py`

## 7. Complexity Analysis
- Time Complexity:
Kompleksitas waktu adalah O(max(n, m)), dengan n dan m merupakan jumlah node pada masing-masing linked list.

Kedua linked list diproses secara bersamaan dalam satu loop. Jumlah iterasi mengikuti panjang linked list yang lebih besar.


- Space Complexity:
- Auxiliary Space: O(1)
- Output Space: O(max(n, m))
- Total Space: O(max(n, m))

Memori tambahan untuk variabel hanya konstan, sedangkan linked list hasil membutuhkan ruang sesuai jumlah digit hasil penjumlahan.

## 8. Edge Cases
Tuliskan kondCarry terakhir

Carry terakhir

Ketika kedua linked list sudah habis, masih mungkin terdapat carry dari penjumlahan sebelumnya. Algoritma harus tetap berjalan untuk membuat node baru yang menyimpan nilai carry tersebut agar tidak ada digit hasil yang terlewat.

Panjang linked list berbeda

Kedua linked list tidak selalu memiliki jumlah node yang sama. Karena itu, proses penjumlahan tidak boleh berhenti ketika salah satunya habis. Node yang tidak tersedia dianggap memiliki nilai 0, sehingga linked list yang lebih panjang tetap dapat diproses sampai selesai.

Carry berulang

Carry selalu disertakan dalam proses penjumlahan pada setiap iterasi. Dengan demikian, jika carry terus muncul pada beberapa digit berturut-turut, nilainya tetap diteruskan hingga seluruh proses penjumlahan selesai.

## 9. Lessons Learned

Memahami penggunaan modulo (%) dan floor division (//) untuk memisahkan digit hasil penjumlahan dan carry.
Memahami bagaimana menentukan value setiap node berdasarkan hasil penjumlahan digit.
Memahami penggunaan dummy node dan pointer current untuk membangun linked list baru secara berurutan.
Memahami cara menggeser pointer untuk melakukan traversal pada dua linked list secara bersamaan.
Memahami cara menangani linked list dengan panjang berbeda dan carry yang masih tersisa.
