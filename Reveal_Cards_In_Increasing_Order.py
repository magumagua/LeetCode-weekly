from itertools import permutations

class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        list_answer = []
        sort_deck = sorted(deck)
        if len(deck) < 2:
            return deck
        else:
            for i in range(len(deck)):
                if len(list_answer) == 0:
                    list_answer.append(sort_deck.pop())
                else:
                    list_answer.insert(0, list_answer.pop())
                    list_answer.insert(0, sort_deck.pop())
        return list_answer
        