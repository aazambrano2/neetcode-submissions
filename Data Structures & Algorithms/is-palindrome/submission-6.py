class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char.lower() for char in s if char.isalnum())
        print(cleaned_text)
        return cleaned_text == cleaned_text[::-1]
        