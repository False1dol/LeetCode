# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0
        i = 0
        A = []
        while l1 != None or l2 != None:
            #print(i)
            if l1 == None:
                #print(l2.val)
                sum += (l2.val) * (10**i)
                l2 = l2.next
            elif l2 == None:
                #print(l1.val)
                sum += (l1.val) * (10**i)
                l1 = l1.next
            else:
                sum += (l1.val + l2.val) * (10**i)
                l1 = l1.next
                l2 = l2.next
            #print(sum)
            i += 1
            
        if sum == 0:
            return [0]
        
        while sum > 0:
            #print(sum)
            A.append(sum % 10)
            sum = sum / 10
        
        return A
