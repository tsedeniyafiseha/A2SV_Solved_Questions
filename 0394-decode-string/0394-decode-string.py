class Solution(object):
    def decodeString(self, s):

        stack = []

        for c in s:

            if c != ']':
                stack.append(c)

            else:
                
                substr = ""
                while stack[-1] != '[':
                    substr = stack.pop() + substr

                stack.pop()  

                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                repeat = int(num)

                
                stack.append(substr * repeat)

        return "".join(stack)