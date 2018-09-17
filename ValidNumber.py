class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i,c in enumerate(s):
            if i == 0:
                if c== ' ':
                    continue
                elif c == '+' or c == '-' or c == 'e' or c == '.' or c.isdigit():
                    if '+' in s[i:]:
                        return False
                    else:
                        continue
                else:
                    return False
            if c != 'e' or c != '+' or c != '-' or c != '.' or c.isalpha():
                return False
            if c == 'e':
                print(s[i+1])
                if s[i+1] == '-' or s[i+1].isdigit():
                    if '+' in s[i:] or '-' in s[i:] or '.' in s[i:]:
                        return False
                    else:
                        continue
                else:
                    print(s[i+1])
        return True
            
