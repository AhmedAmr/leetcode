class Solution:
    def reverseWords(self, s: str) -> str:
        # this should handle multiple spaces in between words
        def reverse_string(string: str) -> None:
            s = list(string)
            n = len(s)
            i = 0
            j = n-1
            while(i<j):
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            return ''.join(s)
        
        n = len(s)
        current_token = ''
        output = ''
        for i, char in enumerate(s):
            if char != ' ':
                current_token+=char
            elif char == ' ' and current_token == '':
                output+=' '
            else:
                reversed_token = reverse_string(current_token)
                output+=reversed_token
                output+=' '
                current_token=''
        if current_token:
            reversed_token = reverse_string(current_token)
            output+=reversed_token
        return output
        