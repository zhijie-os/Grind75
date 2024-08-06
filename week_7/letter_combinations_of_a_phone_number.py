class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {'2':['a', 'b','c'], '3':['d','e','f'],'4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        return self.helper_function(table, digits, 0)
    
    def helper_function(self, table, digits, index):
        if index == len(digits):
            return []
        elif index == len(digits) - 1:
            return table[digits[index]]

        result = []
        current_combination = table[digits[index]]
        next_combination = self.helper_function(table, digits, index + 1)

        for i in range(len(current_combination)):
            for j in range(len(next_combination)):
                elem = current_combination[i] + next_combination[j]
                result.append(elem)

        return result 