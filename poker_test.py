import unittest
import poker
 
class TestPoker(unittest.TestCase):
    '''Example unittest test methods for poker.'''
    sf = ['JC', 'TC', '9C', '8C', '7C']
    fk = ['5S', '5H', '5D', '5C', 'KS']
    fh = ['5S', '5H', '5D', '8C', '8S']
    f1 = ['JC', '5C', '9C', '8C', '7C']
    s1 = ['JC', 'TC', '9C', '8S', '7C']
    op = ['5S', '3H', '9D', '8C', '8S']
    tk = ['5S', '7H', '8D', '8C', '8S']
    tp = ['5S', '5H', '9D', '8C', '8S']
    hc = ['4S', '3H', '9D', '8C', 'TS']
    sal = ['5S', '4H', '3C', '2C', 'AC']
    sfal = ['5S', '4S', '2S', '3S', 'AS']
    
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
        '''Test hand ranks with Ace to five low(straight).'''
 
        actual = poker.hand_rank(TestPoker.sal)
        expected = (4, 5)
        self.assertEqual(actual, expected)
        
    def test_poker_example_5(self):
        '''Test hand ranks with 10 high card.'''
 
        actual = poker.hand_rank(TestPoker.hc)
        expected = (0, [10, 9, 8, 4, 3])
        self.assertEqual(actual, expected)

    def test_poker_example_6(self):
        '''Test hand ranks with Ace to five low straight and flush.'''
 
        actual = poker.hand_rank(TestPoker.sfal)
        expected = (8, 5)
        self.assertEqual(actual, expected)
        
    def test_poker_example_7(self):
        '''Test hand ranks with 4 kinds.'''
 
        actual = poker.hand_rank(TestPoker.fk)
        expected = (7, 5, 13)
        self.assertEqual(actual, expected)

    def test_poker_example_8(self):
        '''Test hand ranks with full house.'''
 
        actual = poker.hand_rank(TestPoker.fh)
        expected = (6, 5, 8)
        self.assertEqual(actual, expected)

    def test_poker_example_9(self):
        '''Test hand ranks with 3 kinds.'''
 
        actual = poker.hand_rank(TestPoker.tk)
        expected = (3, 8, [8, 8, 8, 7, 5])
        self.assertEqual(actual, expected)

    def test_poker_example_10(self):
        '''Test hand ranks with two pairs.'''
 
        actual = poker.hand_rank(TestPoker.tp)
        expected = (2, (8, 5), 9)
        self.assertEqual(actual, expected)

    def test_poker_example_11(self):
        '''Test hand ranks with flush.'''
 
        actual = poker.hand_rank(TestPoker.f1)
        expected = (5, [11, 9, 8, 7, 5])
        self.assertEqual(actual, expected)

    def test_poker_example_12(self):
        '''Test hand ranks with 2 kinds(one pairs).'''
 
        actual = poker.hand_rank(TestPoker.op)
        expected = (1, 8, [9, 8, 8, 5, 3])
        self.assertEqual(actual, expected)

    def test_poker_example_13(self):
        '''Test ranking func with straight flush.'''
 
        actual = poker.ranking(TestPoker.sf)
        expected = [11, 10, 9, 8, 7]
        self.assertEqual(actual, expected)

    def test_poker_example_14(self):
        '''Test ranking func with two pairs.'''
 
        actual = poker.ranking(TestPoker.tp)
        expected = [9, 8, 8, 5, 5]
        self.assertEqual(actual, expected)

    def test_poker_example_15(self):
        '''Test ranking func with Ace to five low straight.'''
 
        actual = poker.ranking(TestPoker.sal)
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
