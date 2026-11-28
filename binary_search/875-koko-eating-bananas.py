
class ListNode:
    def __init(self, value):
        self.val = value
        self.nnext = None

def KokoEating(piles : list, jam : int) -> int:
        kiri = 1
        kanan = max(piles)

        while kiri <= kanan:
            total_jam = 0
            k = (kiri + kanan) // 2
            for pisang in piles:
                total_jam += (pisang + k - 1) // k



            if total_jam > jam:
                kiri = k + 1

            else:
                kanan = k -1


        return kiri



angka = [1,1,100]

print(KokoEating(angka, 3))