class Solution:
    def reorderSpaces(self, text: str) -> str:
        c = text.count(" ")
        li = text.strip().split()
        if len(li) == 1:
            return li[0] + " " * c
        s, s1 = divmod(c, len(li) - 1) 
        return (" " * s).join(li)  + " " * s1