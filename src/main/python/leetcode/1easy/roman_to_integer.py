class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        """
        
        roman = s
        integer = 0
        
        letters = list(roman)
        
        index = 0
        
        while index < len(letters):
            
            letter = letters[index]
            
            value = self.getValue(letter)
            
            if index != len(letters) - 1:
                next_letter = letters[index + 1]
                next_value = self.getValue(next_letter)
                isBigger = self.checkBigger(value, next_value)
                
                if isBigger:
                    integer += value
                else:
                    integer -= value
                
            else:
                integer += value
                
            index += 1
            
        return integer
    
    def getValue(self, letter):
        
        if letter == "I":
            return 1
        elif letter == "V":
            return 5
        elif letter == "X":
            return 10
        elif letter == "L":
            return 50
        elif letter == "C":
            return 100
        elif letter == "D":
            return 500
        elif letter == "M":
            return 1000
        
    def checkBigger(self, letter, next_letter=None):
        return letter >= next_letter


    def main(self):
        roman = "XIV"
        print("Roman:", roman)
        print("Integer:", self.romanToInt(roman))

if __name__ == "__main__":
    Solution().main()

        
    
    
        
        
        
    
        
        
        