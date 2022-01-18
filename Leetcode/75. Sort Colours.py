class Solution(object):
    # To heapify subtree rooted at index i.
    # n is size of heap
    def heapify(self, array, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and array[i] < array[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < n and array[largest] < array[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            array[i], array[largest] = array[largest], array[i]  # swap

            # Heapify the root.
            self.heapify(array, n, largest)

    # The main function to sort an array of given size
    def heapSort(self, array):
        n = len(array)

        # Build a maxheap.
        # Since last parent will be at ((n//2)-1) we can start at that location.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(array, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]  # swap
            self.heapify(array, i, 0)

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        print(f"Unsorted Nums: {nums}")
        self.heapSort(nums)
        print(f"  Sorted Nums: {nums}")


if __name__ == '__main__':
    test = Solution()
    numbers = [[2, 0, 2, 1, 1, 0], [2,0,1], [0], [1]]

    test.sortColors(numbers[0])