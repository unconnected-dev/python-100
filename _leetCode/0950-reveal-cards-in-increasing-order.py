#Reveal Cards In Increasing Order
#https://leetcode.com/problems/reveal-cards-in-increasing-order/description/

caseDeck_1 = [17,13,11,2,3,5,7]
caseDeck_2 = [1,1000]
caseDeck_3 = [17,13,11,2,3,5,7]

if True:
    def deckRevealedIncreasing(deck):
        deck.sort(reverse=True)
        result = []

        for n in deck:
            if len(result) > 0:
                result.insert(0, result.pop())
                
            result.insert(0, n)

        return result
    
print(f"{deckRevealedIncreasing(caseDeck_1)}")
print(f"{deckRevealedIncreasing(caseDeck_2)}")