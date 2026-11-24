
# [#206] - [Reverse Linked List]

## 1. Problem Overview
- Platform: LeetCode
- Difficulty: Easy
- Topic: Linked List
- Algorithm: Iterative Linked List Reversal
- Problem Link: https://leetcode.com/problems/reverse-linked-list

## 2. Problem Summary
Diberikan sebuah singly linked list dan head,referensi dari node pertama linked list tersebut. Tugas kita mengubah hubungan antar-node sehingga node yang awalnya merupakan node pertama menjadi node terakhir,begitu pun sebaliknya.

## 3. Input & Output
- Input: linked list :  1--> 2 --> 3 --> 4 --> None
- Output: linked list : 4 --> 3 --> 2 --> 1 --> None
## Constraints:
    - Jumlah node pada linked list di rentang [0, 5000]
    - -5000 <= Node.val => 5000

## 4. Example
Linked list : 1 --> 2 --> 3 --> 4 --> None
jawaban : 4 --> 3 --> 2 --> 1 --> None

Penjelasan: Setiap node mengubah referensi next-nya agar menunjuk ke node yang sebelumnya berada di sebelah kirinya. Contohnya, hubungan dari node 1 menuju node 2 diubah menjadi hubungan dari node 2 menuju node 1.

## 5. Approach & Reasoning
- Apa pola masalahnya?
In-place Linked List Reversal menggunakan Iterative Traversal.

- Mengapa memilih algoritma ini?

Pendekatan iterative dipilih karena singly linked list hanya memiliki referensi ke node berikutnya, sehingga kita perlu mengelola referensi node sebelumnya secara manual. Dengan menggunakan tiga variabel tambahan, kita dapat membalik hubungan antar-node secara langsung tanpa membuat struktur data baru.

- Bagaimana algoritma bekerja?
    - Buat variabel previous untuk menyimpan referensi node terakhir yang sudah diproses. Variabel ini menjadi tujuan referensi next dari node yang sedang diproses.

    - Buat variabel current untuk menyimpan referensi node yang sedang diproses.

    - Buat variabel next_node untuk menyimpan referensi asli node berikutnya. Variabel ini penting agar kita tidak kehilangan akses ke node yang belum diproses.

    - Simpan referensi asli node berikutnya melalui next_node = current.next.

    - Ubah referensi node sekarang agar menunjuk ke node sebelumnya melalui current.next = previous.

    - Perbarui previous agar menunjuk ke node yang sekarang diproses.

    - Perbarui current agar menunjuk ke node berikutnya melalui next_node.
    Ulangi proses tersebut sampai current mencapai None.
    Setelah seluruh node selesai diproses, previous akan menunjuk ke node pertama dari linked list yang sudah dibalik.

- Mengapa pendekatan ini benar?
   - Setiap iterasi membalik referensi next dari satu node ke node sebelumnya.
   - Setelah selesai diproses, referensi node tersebut tidak akan diubah lagi oleh iterasi berikutnya.
   - Node yang belum diproses tetap dapat diakses melalui current, sehingga tidak ada node yang terlewat.
   - Ketika current mencapai None, seluruh node sudah diproses dan dibalik referensinya. Pada saat itu,        previous menunjuk ke head baru

## 6. Implementation
Referensi file Python:
`[206-reverse-linked-list].py`

## 7. Complexity Analysis
- Time Complexity: O(n)
    Setiap node dikunjungi tepat satu kali untuk mengubah arah referensi next-nya. Karena jumlah iterasi mengikuti jumlah node dalam linked list, kompleksitas waktunya adalah O(n).

- Space Complexity:
 - Auxiliary space: O(1)
 - Output space: O(1)
Algoritma hanya menggunakan tiga variabel tambahan untuk menyimpan referensi node. Jumlah variabel tersebut tetap dan tidak bergantung pada jumlah node dalam linked list.

## 8. Edge Cases

Empty Linked List: head = None. Loop tidak dijalankan dan fungsi mengembalikan None

Single Node: Linked list hanya memiliki satu node. Referensinya tetap None dan node tersebut menjadi head sekaligus tail.

Multiple Nodes: Semua node diproses satu kali dan urutan referensinya berhasil dibalik tanpa kehilangan node.


## 9. Lessons Learned

Pointer Manipulation: Memahami cara membalik arah referensi next tanpa membuat linked list baru.

Three-Pointer Technique: Memahami peran previous, current, dan next_node dalam proses pembalikan.

In-place Algorithm: Memodifikasi struktur data yang sudah ada tanpa alokasi node tambahan.


Loop Termination: Memahami bahwa ketika current mencapai None, seluruh node sudah diproses dan previous menjadi head baru.

Complexity Analysis: Memahami mengapa algoritma ini memiliki time O(n) dan auxiliary space O(1).
