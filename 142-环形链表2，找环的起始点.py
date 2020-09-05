# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法1：（会超出时间限制）可以看到，当快慢指针相遇时，让其中任一个指针重新指向头节点，然后让它俩以相同速度前进，再次相遇时所在的节点位置就是环开始的位置
# 方法2：我们分配一个 Set 去保存所有的列表节点。我们逐一遍历列表，检查当前节点是否出现过，如果节点已经出现过，那么一定形成了环且它是环的入口。否则如果有其他点是环的入口，我们应该先访问到其他节点而不是这个节点。其他情况，没有成环则直接返回 null


# 方法2
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        node = head
        while node and node.next:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None

# 方法1
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = head.next
            fast = head.next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next 
        return slow