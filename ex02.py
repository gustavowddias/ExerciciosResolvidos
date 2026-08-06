class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)

        reverse_text = text[::-1]

        if reverse_text == text:
            return True
        
        return False

solucao = Solution()

solucao.isPalindrome(121)