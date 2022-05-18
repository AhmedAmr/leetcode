class Solution:
    def reverseWords(self, s: str) -> str:
        #Pythonic way..
        words = s.split(' ')
        words_as_chars_list = list(map(list, words))
        reversed_words_as_chars_list = list(map(reversed, words_as_chars_list))
        reversed_words_list = list(map(''.join, reversed_words_as_chars_list))
        return ' '.join(reversed_words_list)
        