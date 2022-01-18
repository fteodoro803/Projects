import collections

class Solution(object):
    def letterCombinations(self, digits):
        numCorrespondence = {'2': ['a', 'b', 'c'],
                             '3': ['d', 'e', 'f'],
                             '4': ['g', 'h', 'i'],
                             '5': ['j', 'k', 'l'],
                             '6': ['m', 'n', 'o'],
                             '7': ['p', 'q', 'r', 's'],
                             '8': ['t', 'u', 'v'],
                             '9': ['w', 'x', 'y', 'z']}
        outputList = []

        if not digits:  # Empty Case
            return outputList

        for num in digits:
            outputList.append(numCorrespondence[num])

        return outputList


if __name__ == '__main__':
    test = Solution()
    digits = ["23", "", "2"]

    print(test.letterCombinations(digits[2]))