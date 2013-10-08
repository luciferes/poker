import unittest
import poker
 
class TestPoker(unittest.TestCase):
    '''Example unittest test methods for poker.'''
    sf = ['JC', 'TC', '9C', '8C', '7C']
    fk = ['5S', '5H', '5D', '5C', 'KS']
    fh = ['5S', '5H', '5D', '8C', '8S']
    s1 = ['JC', 'TC', '9C', '8S', '7C']
    op = ['5S', '3H', '9D', '8C', '8S']
    tp = ['5S', '5H', '9D', '8C', '8S']
    hc = ['4S', '3H', '9D', '8C', 'TS']
    al = ['5S', '4H', '3C', '2C', 'AC']
    fal = ['5S', '4S', '2S', '3S', 'AS']
    
    def test_poker_example_1(self):
        '''Test poker with sf(straight flush) and fk(4 kinds).'''
 
        actual = poker.poker([TestPoker.sf,TestPoker.fk])
        expected = ['JC', 'TC', '9C', '8C', '7C']
        self.assertEqual(actual, expected)
 
    def test_poker_example_2(self):
        '''Test poker with fh(full house) and fk(4 kinds).'''
 
        actual = poker.poker([TestPoker.fh,TestPoker.fk])
        expected = ['5S', '5H', '5D', '5C', 'KS']
        self.assertEqual(actual, expected)

    def test_poker_example_3(self):
        '''Test hand ranks with sf(straight flush).'''
 
        actual = poker.hand_rank(TestPoker.sf)
        expected = (8, 11)
        self.assertEqual(actual, expected)

    def test_poker_example_4(self):
        '''Test hand ranks with Ace to five low.'''
 
        actual = poker.hand_rank(TestPoker.al)
        expected = (4, 5)
        self.assertEqual(actual, expected)
        
    def test_poker_example_5(self):
        '''Test hand ranks with 10 high card.'''
 
        actual = poker.hand_rank(TestPoker.hc)
        expected = (0, poker.ranking(TestPoker.hc))
        self.assertEqual(actual, expected)

    def test_poker_example_6(self):
        '''Test hand ranks with Ace to five low and flush.'''
 
        actual = poker.hand_rank(TestPoker.fal)
        expected = (8, 5)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
