# Poker #
----
## Poker.py    
This modlue offers the winner of poker for the python language. it have "poker([hand, hand, ...])" function to solve what is the best of hand in hands. and it have more function to use such as "straight(hand)" , "flush(hand)", "fullhouse(ranks)" , "kind(n, ranks)" , "twopair(ranks)"      
------
### poker(hands) -> the best hand(s)    
Return the best hand from list of hands

###### **Example**  
~~~~~~
>>> sf = ['JC', 'TC', '9C', '8C', '7C']
>>> fk = ['5S', '5H', '5D', '5C', 'KS']
>>> sf2 = ['JS', 'TS', '9S', '8S', '7S']
>>> poker([sf, sf2])
['JC', 'TC', '9C', '8C', '7C']
>>> poker([sf, fk])
['JC', 'TC', '9C', '8C', '7C']
>>> fh = ['5S', '5H', '5D', '8C', '8S']
>>> poker([fh, fk])
['5S', '5H', '5D', '5C', 'KS']
>>> s1 = ['JC', 'TC', '9C', '8S', '7C']
>>> poker([fh, s1])
['5S', '5H', '5D', '8C', '8S']
>>> op = ['5S', '3H', '9D', '8C', '8S']
>>> tp = ['5S', '5H', '9D', '8C', '8S']
>>> hc = ['4S', '3H', '9D', '8C', 'TS']
>>> poker([op, tp])
['5S', '5H', '9D', '8C', '8S']
>>> poker([op, hc])
['5S', '3H', '9D', '8C', '8S']
>>> poker([op, hc, sf])
['JC', 'TC', '9C', '8C', '7C']
>>> poker([op])
['5S', '3H', '9D', '8C', '8S']
>>> al = ['5S', '4H', '3C', '2C', 'AC']
>>> fal = ['5S', '4S', '2S', '3S', 'AS']
>>> hand_rank(al)
(4, 5)
>>> hand_rank(fal)
(8, 5)
~~~~~~    
------
### ranking(hand) -> list of 5 ints     
Return rank of the cards in hand

###### **Example** 
~~~~~~
>>> ranking(['JC', 'TC', '9C', '8C', '7C'])
[11, 10, 9, 8, 7]
>>> ranking(['5S', '5H', '9D', '8C', '8S'])
[9, 8, 8, 5, 5]
~~~~~~
------
### hand_rank(hand) -> tuple of two int      
Return the hand rank of a hand

###### **Example** 
~~~~~~
>>> sf = ['JC', 'TC', '9C', '8C', '7C']
>>> hand_rank(sf)
(8, 11)
>>> fk = ['5S', '5H', '5D', '5C', 'KS']
>>> hand_rank(fk)
(7, 5)
>>> fh = ['5S', '5H', '5D', '8C', '8S']
>>> hand_rank(fh)
(6, 5)
>>> f1 = ['JC', '5C', '9C', '8C', '7C']
>>> hand_rank(f1)
(5, [11, 9, 8, 7, 5])
>>> s1 = ['JC', 'TC', '9C', '8S', '7C']
>>> hand_rank(s1)
(4, 11)
>>> tk = ['5S', '7H', '8D', '8C', '8S']
>>> hand_rank(tk)
(3, 8)
>>> tp = ['5S', '5H', '9D', '8C', '8S']
>>> hand_rank(tp)
(2, 8, 5, 9)
>>> op = ['5S', '3H', '9D', '8C', '8S']
>>> hand_rank(op)
(1, 8, [9, 8, 8, 5, 3])
>>> hc = ['4S', '3H', '9D', '8C', 'TS']
>>> hand_rank(hc)
(0, [10, 9, 8, 4, 3])
~~~~~~
------
### straight(hand) -> Boolean 
Return True if hand is straight,false otherwise    

###### **Example** 
~~~~~~
>>> sf = ['JC', 'TC', '9C', '8C', '7C']
>>> straight(sf)
True
>>> fk = ['5S', '5H', '5D', '5C', 'KS']
>>> straight(fk)
False
~~~~~~
------
### flush(hand) -> Boolean     
Return True if hand is flush, False otherwise.    

###### **Example** 
~~~~~~
>>> sf = ['JC', 'TC', '9C', '8C', '7C']
>>> flush(sf)
False
>>> fk = ['5S', '5H', '5D', '5C', 'KS']
>>> flush(fk)
True
~~~~~~
------
### fullhouse(ranks) -> Boolean     
Return True if hand is fullhouse,false otherwise     

~~~~~~
>>> sf_ranks = [11, 10, 9, 8, 7]
>>> fullhouse(sf_ranks)
False
>>> fk_ranks = [5, 5, 5, 5, 13]
>>> fullhouse(fk_ranks)
False
>>> fh_ranks = [5, 5, 5, 8, 8]
>>> fullhouse(fh_ranks)
True
~~~~~~
------
### kind(n, ranks) -> a tuple of int, list of rank    
Return rank if hand is n kind, false otherwise    

###### **Example**    
~~~~~~
>>> sf_ranks = [11, 10, 9, 8, 7]
>>> kind(4, sf_ranks)
0
>>> fk_ranks = [5, 5, 5, 5, 13]
>>> kind(4, fk_ranks)
5
>>> fh_ranks = [5, 5, 5, 8, 8]
>>> kind(3, fh_ranks)
5
>>> op_ranks = [5, 3, 9, 8, 8]
>>> kind(2, op_ranks)
8
~~~~~~
------  
### twopair(ranks) -> tuple  of two pair rank    

Return tuple of highpair and lowpair if hand is twopair, false otherwise    

###### **Example**     
~~~~~~
>>> sf_ranks = [11, 10, 9, 8, 7] 
>>> twopair(sf_ranks)
()
>>> tp_ranks = [5, 5, 9, 8, 8]
>>> twopair(tp_ranks)
(8, 5)
~~~~~~
