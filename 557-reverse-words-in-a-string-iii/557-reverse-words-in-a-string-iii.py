from multiprocessing import Pool
class Solution:
    def reverseWords(self, s: str) -> str:
        #Pythonic way..
        words = s.split(' ')
        with Pool(10) as p:
            words_as_chars_list = list(p.map(list, words))
            reversed_words_as_chars_list = list(p.map(reversed, words_as_chars_list))
            reversed_words_list = list(p.map(''.join, reversed_words_as_chars_list))
        return ' '.join(reversed_words_list)
        