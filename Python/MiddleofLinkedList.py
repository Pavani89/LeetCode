'''
1480. Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Time complexity: O(n)
Space complexity: O(1)
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findMiddleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

middle = findMiddleNode(head)
print(middle.val)  # Output: 3
