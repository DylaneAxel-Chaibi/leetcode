class Solution:
    def isPalindrome(self, s: str) -> bool:
        # re.sub(r'[^A-Za-z0-9]', '', text)
        return re.sub(r'[^A-Za-z0-9]', '', s).lower() == re.sub(r'[^A-Za-z0-9]', '', s[::-1]).lower()