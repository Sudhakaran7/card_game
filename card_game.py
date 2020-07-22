import collections
class Solution(object):
    def card_rearrangement(self, hand, W):
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in range(m, m+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1
        return True

val=Solution()
cards=list(map(int,input().split()))
w=int(input())
print(val.card_rearrangement(cards,w))
