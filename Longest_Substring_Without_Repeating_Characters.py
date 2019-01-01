from functools import reduce
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def child(l):
            list_num = []

            def child_list(l):
                if l:
                    list_str = []
                    n = 0
                    x = 0
                    for i in l:
                        if i not in list_str:
                            n = n + 1
                            list_str.append(i)
                            list_num.append(len(list_str))
                        else:
                            break
                    x = x + 1
                    child_list(l[x:])
                else:
                    return 0
                list_num.sort()
                return list_num
            return child_list(l)


        def answer(l):
            print('a')
            list_num = child(l)

            if list_num:
                print('s')
                return list_num[-1]
            else:
                return 0


        return answer(s)