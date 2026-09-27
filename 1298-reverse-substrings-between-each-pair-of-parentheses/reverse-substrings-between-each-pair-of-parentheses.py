class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[""]
        for c in s:
            if c=="(":
                stack.append("")
            elif c==")":
                inner=stack.pop()
                stack[-1]+=inner[::-1]
            else:
                stack[-1]+=c
        return stack[0]
        