class Solution:
    def removeComments(self, source):
        res = []
        inBlock = False
        new_line = []

        for line in source:
            i = 0
            if not inBlock:
                new_line = []

            while i < len(line):
                
                if not inBlock and i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                    inBlock = True
                    i += 2
                
                elif inBlock and i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                    inBlock = False
                    i += 2
                
                elif not inBlock and i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                    break
               
                elif not inBlock:
                    new_line.append(line[i])
                    i += 1
                else:
                    i += 1

            if not inBlock and new_line:
                res.append("".join(new_line))

        return res
