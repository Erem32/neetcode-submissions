class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.strip()
        word = word.lower()
        final_word = ''.join([char for char in word if char.isalnum()])
        print(final_word)
        if final_word == final_word[::-1]:
            return True
        return False
        