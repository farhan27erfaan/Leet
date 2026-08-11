# Last updated: 11/08/2026, 11:43:02
class Solution:
    def mergeTwoLists(self, list1, list2):

        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        