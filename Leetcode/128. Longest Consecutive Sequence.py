class Solution(object):
    #v1
    """def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums = list(set(nums))  # gets rid of duplicates
        numObjects = len(nums)
        maxConsecutive = 1
        currConsecutive = 1
        removedSet = set([])

        currNum = min(nums)  # initialising
        for i in range(numObjects):
            nextNum = currNum+1
            if nextNum in nums:  # if something after exists
                nums.remove(currNum)
                removedSet.add(currNum)
                currNum = nextNum
                currConsecutive += 1
            elif currConsecutive >= 1: # if last in seq
                nums.remove(currNum)
                removedSet.add(currNum)
                #currConsecutive += 1
                if currConsecutive > maxConsecutive:
                    maxConsecutive = currConsecutive
                    currConsecutive = 0
                    if i != numObjects-1: # if not final thingy
                        currNum = min(nums)

        print(nums, maxConsecutive, removedSet)
        return maxConsecutive"""

    # v2 -- works
    def longestConsecutive(self, nums):
        maxConsecutive = 0
        newSet = set(nums)  # removes duplicates
        newSetTEST = set(nums) # test

        # Empty List
        if not nums:
            return 0

        currNum = min(newSet)
        currConsecutive = 1  # bc if there is one digit, it is one consec already, and that's a given bc set isnt empty
        numValues = len(newSet)
        for i in range(numValues):
            #print(f"CurrentNum: {currNum}")
            newSet.remove(currNum)
            #print(f"\t{currNum+1} in set: {currNum+1 in newSet}")
            if currNum+1 in newSet:
                currNum = currNum+1
                currConsecutive += 1
            else:
                #print("\tELSE")
                #print(f"\t\tcurrNum+1 {currNum+1} not in set")
                #print(f"\t\tcurrConsecutive: {currConsecutive}, maxConsecutive: {maxConsecutive}, curr>max: {currConsecutive>maxConsecutive}")
                if currConsecutive > maxConsecutive:
                    maxConsecutive = currConsecutive
                currConsecutive = 1
                if newSet:  # not end of set
                    currNum = min(newSet)

        #print(f"nums: {nums}, {newSetTEST}")
        #print(f"consecutive: {maxConsecutive}")

        return maxConsecutive

    #v3
    def longestConsecutive(self, nums):
        maxConsecutive = 0
        nums = set(nums)  # removes duplicates

        # Empty List
        if not nums:
            return 0

        currNum = min(nums)
        currConsecutive = 1  # bc if there is one digit, it is one consec already, and that's a given bc set isnt empty
        numValues = len(nums)
        for i in range(numValues):
            nums.remove(currNum)
            if currNum+1 in nums:
                currNum = currNum+1
                currConsecutive += 1
            else:
                if currConsecutive > maxConsecutive:
                    maxConsecutive = currConsecutive
                currConsecutive = 1
                if nums:  # not end of set
                    currNum = min(nums)

        return maxConsecutive

if __name__ == "__main__":
    nums = [[100, 4, 200, 1, 3, 2], [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], [1,2,3,4,11,12,13,14,15], [9,1,4,7,3,-1,0,5,8,-1,6], [9,1,-3,2,4,8,3,-1,6,-2,-4,7], {1, 2, 3, 4, 6, 7, 8, 9}]  #removing duplicates could help efficiency

    test = Solution()
    print(test.longestConsecutive(nums[5]))
