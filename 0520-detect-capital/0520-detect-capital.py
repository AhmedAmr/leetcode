class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n<=1:
            return True
        uppercase = word[0].isupper() and word[1].isupper()
        lowercase = word[0].islower() and word[1].islower()
        camelcase = word[0].isupper() and word[1].islower()

        if uppercase:
            return all(map(str.isupper, list(word)))
        if lowercase:
            return all(map(str.islower, list(word)))
        if camelcase:
            return all(map(str.islower, list(word[1:])))
        return False