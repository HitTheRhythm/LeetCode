class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cur = 0
        count = float('inf')
        for i in range(len(blocks)):
            if blocks[i] == "W":
                cur += 1
            if i < k - 1:
                continue
            count = min(cur,count)
            if blocks[i - k + 1] == "W":
                cur -= 1 
        return count