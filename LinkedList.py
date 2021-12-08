# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def hasCycle(self, head):
        if (head == None) or (head.next == None) or (head.next.next == None):
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if (fast == None) or (fast.next == None):
                return False
            slow = slow.next
            fast = fast.next.next
        return True    
        
class Solution:
    def reverseList(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        temp = head.next        
        cur = self.reverseList(head.next)
        head.next = None
        temp.next = head
        return cur
        
class Solution:
    def isPalindrome(self, head):
        pos1 = head
        pos2 = head
        while  pos2 and pos2.next:
            pos1 = pos1.next
            pos2 = pos2.next.next
            
        prev = None
        while pos1:
            temp = pos1
            pos1 = pos1.next
            temp.next = prev
            prev = temp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False            
            left = left.next
            right = right.next
        return True

class Solution:
    def removeElements(self, head, val):
        while (head != None) and (head.val == val):
            head = head.next
            
        curNode = head
        while (curNode != None) and (curNode.next != None):
            if curNode.next.val == val:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return head                            

class Solution:
    def oddEvenList(self, head):
        if head == None:
            return None
        headOdd = head
        headEven = head.next
        even = headEven
        while headEven and headEven.next:
            headOdd.next = headEven.next
            headOdd = headOdd.next
            headEven.next = headOdd.next
            headEven = headEven.next
        headOdd.next = even
        return head

class Solution:
    def middleNode(self, head):
        pos1 = head
        pos2 = head
        while pos2 is not None:
            if pos2.next is None:
                return pos1
            pos1 = pos1.next
            pos2 = pos2.next.next            
        return pos1

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

class Solution:
    def findLength(self, head):
        res = 0
        while head:
            res += 1
            head = head.next
        return res
    
    def cutLL(self, head, k):
        curr = head
        n = self.findLength(head) - k
        count = 1
        while count < n:
            curr = curr.next
            count += 1
        h1 = curr.next
        curr.next = None
        return head, h1       
                    
    def rotateRight(self, head, k):
        if head == None:
            return None
        if head.next == None or k == 0:
            return head
        else:
            n = self.findLength(head)
            # print(n,k)
            # print(k%n)
            if k < n:
                head, h1 = self.cutLL(head, k)
                h2 = h1
                while h1.next:
                    h1 = h1.next
                h1.next = head
                return h2
            elif n == k or k%n == 0:
                return head
            else:
                head, h1 = self.cutLL(head, k%n)
                h2 = h1
                while h1.next:
                    h1 = h1.next
                h1.next = head
                return h2

class Solution:
    # find mid
    # split the list into 2 list
    # sort 2 sublists
    # merge 2 sorted list
    def mergeTwoLists(self, l1, l2):
        # if one of list is empty
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        #if both list are empty
        if not (l1 and l2):
            return None
        
        # create dummy, curr lists
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1 # point curr to l1
                l1 = l1.next # shift l1 to the next node
            else:
                curr.next = l2 # point curr to l2
                l2 = l2.next # shift l2 to the next node
            curr = curr.next # # shift curr to the next node
        # connect the rest of longer list with the curr    
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next    
    
    def findMid(self, head):
        left = right = head
        while right.next and right.next.next:
            left = left.next
            right = right.next.next
        mid = left.next
        left.next = None
        return mid
            
    def sortList(self, head):
        if head == None or head.next == None: return head # head is none or head only have 1 node
        mid = self.findMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeTwoLists(left, right)

class Solution:
    def getIntersectionNode(self, headA, headB):
        h1 = headA
        h2 = headB
        if (h1 == None) or (h2 == None):
            return None
        while h1 != h2:
            if h1 == None:
                h1 = headB
            else:
                h1 = h1.next
                
            if h2 == None:
                h2 = headA
            else:
                h2 = h2.next 
        return h1

class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return None
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head    

                                                                        