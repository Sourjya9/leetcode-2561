class Solution:
    def partition(self, s):
        result = []
        path = []
        
        def backtrack(start):
            if start == len(s):
                result.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(end)
                    path.pop()
        
        backtrack(0)
        return result