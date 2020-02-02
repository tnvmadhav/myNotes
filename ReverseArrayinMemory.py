def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, (int(len(s)/2) + (len(s)%2))):
            s[len(s)-1-i], s[i]  = s[i], s[len(s)-1-i]
