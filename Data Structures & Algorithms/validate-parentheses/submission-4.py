class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = { ")" : "(", "]" : "[", "}" : "{"}

        for character in s:
            if character in closetoopen:
                if stack and stack[-1] == closetoopen[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)

        return True if not stack else False