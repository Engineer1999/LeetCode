# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next

class Solution:
    def addTwoNumbers(self, l1, l2 ,c = 0):
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret
            



if __name__ == '__main__':
    llist1 = LinkedList()
    llist1.head = ListNode(3)
    second = ListNode(2)
    third = ListNode(1)

    llist1.head.next = second
    second.next = third


    llist2 = LinkedList()
    llist2.head = ListNode(3)
    second = ListNode(2)


    llist2.head.next = second
    llist = LinkedList()

    soln = Solution()
    num = soln.addTwoNumbers(llist1.head, llist2.head)
    print('-----')
    temp = num
    while(temp):
        print(temp.val)
        temp = temp.next
