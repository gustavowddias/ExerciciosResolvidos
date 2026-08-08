class Solution:
    def romanToInt(self, roman: str) -> int:
        symbols = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                   (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), 
                   (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        resultado = 0

        for valor, simbolo in symbols:
            while roman.startswith(simbolo):
                resultado += valor
                roman = roman[len(simbolo):]

        return resultado

        

solucao = Solution()
solucao.romanToInt('III')