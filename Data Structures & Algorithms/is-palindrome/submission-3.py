class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.strip()
        final_word = ''.join([char.lower() for char in word if char.isalnum()])
        print(final_word)
        if final_word == final_word[::-1]:
            return True
        return False
        