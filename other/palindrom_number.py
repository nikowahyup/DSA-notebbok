"""LeetCode Solution [#9 Palindrome Number]
   Link : https://leetcode.com/problems/palindrome-number/
   Difficulty : Easy"""


class Solution:
    def solusi(self, x : int) -> bool:

        """#1 Inti Masalah
        Soal ini meminta kita untuk mengecek apakah sebuah angka termasuk bilangan palindrom atau bukan.
        Bilangan palindrom adalah bilangan yang jika dibalik nilainya tetap sama, contoh 121, 1331"""

        """#2 Mengapa Memilih Desain Ini
        Ingin mencoba pendekatan matematika untuk menyelesaikan soal ini,
        tidak hanya dengan mengonversi ke string dan melakukan pembalikan"""


        """#3 Analisis Kompleksitas
        Time Complexity : O(n log n) --> Setiap perulangan membagi x dengan 10,itu artinya 
        jumlah perulangan bergantung pada jumlah digit pada x.
         Space Complexity : O(1) --> Tidak ada alokasi untuk list atau dictionary 
         yang menyimpan hasil setiap perulangan dan akan membesar jika x semakin besar """

        if x < 0:
            return False

        if x != 0 and x % 10 == 0:
            return False


        angka_dibalik = 0
        angka_asli = x


        while x > 0:
            digit = x % 10
            angka_dibalik = (angka_dibalik * 10) + digit
            x //= 10

        return angka_asli == angka_dibalik






if __name__=="__main__":
    sol = Solution()
