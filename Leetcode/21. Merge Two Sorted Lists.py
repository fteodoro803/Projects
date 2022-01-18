# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList():
    # Function to initialize head
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = ListNode(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def traverse(self):
        temp = self.head
        while (temp):
            print(temp.val)
            temp = temp.next

    def traverseAsList(self):
        temp = self.head
        lst = []
        while (temp):
            lst.append(temp.val)
            temp = temp.next

        print(lst)

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sortedList = LinkedList()

        l1.




if __name__ == "__main__":
    l1 = [[1, 2, 4]]
    l2 = [[1, 3, 4]]

    linkedList1 = LinkedList()
    linkedList2 = LinkedList()
    for i in range(len(l1[0])):
        linkedList1.append(l1[0][i])
    for i in range(len(l2[0])):
        linkedList2.append(l2[0][i])

    solution = Solution()

    linkedList1.traverseAsList()
    linkedList2.traverseAsList()
    solution.mergeTwoLists(linkedList1, linkedList2)