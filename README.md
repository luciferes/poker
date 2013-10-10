# Poker.py      


This module offers the winner of poker for the python language. it have "poker([hand, hand, ...])" function to solve what is the best of hand in hands. and it have more function to use such as "straight(hand)" , "flush(hand)", "fullhouse(ranks)" , "kind(n, ranks)" , "twopair(ranks)"      


*Our Contacts below*:    
Noppadol Trongkij: s6070070@kmitl.ac.th    
Bussakorn Wonghorm: s6070080@kmitl.ac.th    

======
### poker(hands) -> the best hand(s)    
Return a list of the best hand(s) from list of hands    


###### **Example**    
~~~~~~
>>> sf = ['JC', 'TC', '9C', '8C', '7C']
>>> sf2 = ['JS', 'TS', '9S', '8S', '7S']
>>> poker([sf, sf2])
[['JC', 'TC', '9C', '8C', '7C'], ['JS', 'TS', '9S', '8S', '7S']]
>>> fh = ['5S', '5H', '5D', '8C', '8S']
>>> fk = ['5S', '5H', '5D', '5C', 'KS']
>>> poker([fh, fk])
[['5S', '5H', '5D', '5C', 'KS']]
>>> op = ['5S', '3H', '9D', '8C', '8S']
>>> tp = ['5S', '5H', '9D', '8C', '8S']
>>> hc = ['4S', '3H', '9D', '8C', 'TS']
>>> poker([op, hc, sf])
[['JC', 'TC', '9C', '8C', '7C']]
~~~~~~    


======
### ranking(hand) -> list of 5 ints     


Return rank of the cards in hand    

###### **Example** 
~~~~~~
>>> ranking(['JC', 'TC', '9C', '8C', '7C'])
[11, 10, 9, 8, 7]
>>> ranking(['5S', '5H', '9D', '8C', '8S'])
[9, 8, 8, 5, 5]
~~~~~~
======    
### hand_rank(hand) -> tuple of two int      


Return the hand rank of a hand.    

###### **Example**    
~~~~~~
>>> sf = ['JC', 'TC', '9C', '8C', '7C']
>>> hand_rank(sf)
(8, 11)
>>> f1 = ['JC', '5C', '9C', '8C', '7C']
>>> hand_rank(f1)
(5, [11, 9, 8, 7, 5])
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
======
### straight(hand) -> Boolean    


Return True if hand is straight,false otherwise    

###### **Example**     
~~~~~~
>>> straight(['JC', 'TC', '9C', '8C', '7C'])
True
>>> fk = ['5S', '5H', '5D', '5C', 'KS']
>>> straight(fk)
False
~~~~~~
======
### flush(hand) -> Boolean       


Return True if hand is flush, False otherwise.      

###### **Example**       
~~~~~~
>>> sf = ['JC', 'TC', '9C', '8C', '7C']
>>> flush(sf)
False 
>>> flush(['5S', '5H', '5D', '5C', 'KS'])
True
~~~~~~
======
### fullhouse(ranks) -> Boolean     


Return True if hand is fullhouse,false otherwise     

###### **Example**   
~~~~~~
>>> sf_ranks = [11, 10, 9, 8, 7]
>>> fullhouse(sf_ranks)
False
>>> fullhouse([5, 5, 5, 8, 8])
True
~~~~~~    
======    
### kind(n, ranks) -> a tuple of int, list of rank    


Return rank if hand is n kind, false otherwise.    

###### **Example**    
~~~~~~
>>> sf_ranks = [11, 10, 9, 8, 7]
>>> kind(4, sf_ranks)
0
>>> fk_ranks = [5, 5, 5, 5, 13]
>>> kind(4, fk_ranks)
5
>>> op_ranks = [5, 3, 9, 8, 8]
>>> kind(2, op_ranks)
8
~~~~~~   
======    
### twopair(ranks) -> tuple  of two pair rank    


Return tuple of highpair and lowpair if hand is twopair, false otherwise.    

###### **Example**     
~~~~~~
>>> sf_ranks = [11, 10, 9, 8, 7] 
>>> twopair(sf_ranks)
()
>>> tp_ranks = [5, 5, 9, 8, 8]
>>> twopair(tp_ranks)
(8, 5)
~~~~~~

------
# poker_test.py    

this module offers to check testcase of poker.py, if you want to add more test just add a function like ...   
~~~~~~
    def test_poker_example_xx(self):
        '''Test what?.'''
 
        actual = *[!]put the module you want to test it[!]*
        expected = *[!]put output that you expected[!]*
        self.assertEqual(actual, expected)
~~~~~~    

------
# Reference    

[1]  Assoc.Prof. Dr.Chotipat Pornavalai    

[2]  Peter Norvig    