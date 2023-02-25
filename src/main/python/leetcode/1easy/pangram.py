class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        
        my_str = list(sentence)
        my_str.sort()

        index_list = self.letterToIndex(my_str)
        
        index_list_nodup = self.removeDuplicates(index_list)
        
        index_list_nodup = self.removeDuplicates(index_list_nodup)
        
        
        return index_list == nums

    def removeDuplicates(self, my_list):

        remove_list = []
        
        for index in range(len(my_list)):

            if index == len(my_list) - 1:
                return my_list

            if my_list[index] == my_list[index + 1]:
                remove_list.append(my_list[index])

        for index in range(len(remove_list)):
            my_list.remove(remove_list[index])

        return my_list

    def letterToIndex(self, sentence):
        index_list = []

        for index in range(len(sentence)):
            index_list.append(self.getValue(sentence[index]))

        return index_list
            
    def getValue(self, letter):
        if letter == "a":
            return 1
        elif letter == "b":
            return 2
        elif letter == "c":
            return 3
        elif letter == "d":
            return 4
        elif letter == "e":
            return 5
        elif letter == "f":
            return 6
        elif letter == "g":
            return 7
        elif letter == "h":
            return 8
        elif letter == "i":
            return 9
        elif letter == "j":
            return 10
        elif letter == "k":
            return 11
        elif letter == "l":
            return 12
        elif letter == "m":
            return 13
        elif letter == "n":
            return 14
        elif letter == "o":
            return 15
        elif letter == "p":
            return 16
        elif letter == "q":
            return 17
        elif letter == "r":
            return 18
        elif letter == "s":
            return 19
        elif letter == "t":
            return 20
        elif letter == "u":
            return 21
        elif letter == "v":
            return 22
        elif letter == "w":
            return 23
        elif letter == "x":
            return 24
        elif letter == "y":
            return 25
        elif letter == "z":
            return 26


    def main(self):
        print(self.checkIfPangram("abcdefghijklmnopqrstuvwxyz"))

if __name__ == "__main__":
    Solution().main()