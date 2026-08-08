class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]: # Recebo Lista e o target
        _range = len(nums) # Leio o range 
        resultado = None 

        for i in range(_range): # Percorre todos os itens na lista "nums"
            indice = 1
            if i + 1 >= _range: # Se o índice estiver "out of range" ele para aqui
                return []
            
            while indice != _range: # Enquanto não percorrer todos os itens de "nums" 
                resultado = nums[i] + nums[indice]

                if resultado == target and i != indice:
                    return [i, indice]
                indice += 1

lista = [2, 7, 11, 15]

solucao = Solution()

solucao.twoSum(lista, 9)