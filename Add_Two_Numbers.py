from functools import reduce
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def get_num(list_node):
            list_num = []
            def get_num_two(list_node):
                if list_node:
                    list_num.append(list_node.val)
                    get_num_two(list_node.next)
                return list_num[::-1]
            # print('e', get_num_two(list_node))
            return get_num_two(list_node)


        def get_answer_list(num):
            return list(str(num))


        def get_lino(num, n):
            list_answer = get_answer_list(num)
            # print(1, list_answer)
            list_answer.reverse()
            def get_lino_two(list_answer, n):
                if n < len(list_answer):
                    #print(2, list_answer)
                    node = ListNode(int(list_answer[n]))
                    #print(33, int(list_answer[n]))
                    if node.val is not None:
                        n = n + 1
                        node.next = get_lino_two(list_answer, n)
                    return node
            return get_lino_two(list_answer, n)


        def add(x, y):
            return 10*x + y


        def answer(l1, l2):
            first = reduce(add, get_num(l1))
            second = reduce(add, get_num(l2))
            add_sum = int(first) + int(second)
            return get_lino(add_sum, 0)

        return answer(l1, l2)