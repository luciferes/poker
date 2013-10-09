import unittest
import poker
 
class TestPoker(unittest.TestCase):
    '''Example unittest test methods for poker.'''
    rsf = ['AS', 'KS', 'QS', 'JS', 'TS']  # Royal straight flush
    sf = ['JC', 'TC', '9C', '8C', '7C']   # Jack high, straight flush
    sf2 = ['JS', 'TS', '9S', '8S', '7S']  # Jack high, staight flush
    sf3 = ['TH', '9H', '8H', '7H', '6H']  # 10 high, straight flush
    fk = ['5S', '5H', '5D', '5C', 'KS']   # 5 four kind, King high
    fk2 = ['9S', '9H', '9D', '9C', '2C']  # 9 four kind, 2 high
    fh = ['5S', '5H', '5D', '8C', '8S']   # Full House 5,8
    fh2 = ['TS', 'TH', 'TD', '6C', '6S']  # Full House 10,6
    f1 = ['JC', '5C', '9C', '8C', '7C']   # flush 11 9 8 7 5
    f2 = ['KD', '9D', '5D', '4D', '2D']   # flush 13 9 5 4 2
    s1 = ['JC', 'TC', '9C', '8S', '7C']   # Jack high, straight
    s2 = ['7D', '9D', '8H', 'TS', 'JD']   # Jack high, straight
    s3 = ['AD', 'KH', 'QS', 'JS', 'TD']   # Ace high, straight
    op = ['5S', '3H', '9D', '8C', '8S']   # 8 one pair, 9 8 8 5 3
    op2 = ['5S', '5C', 'TS', 'JH', '8H']  # 5 one pair, 11 10 8 5 5
    tk = ['5S', '7H', '8D', '8C', '8S']   # 8 three kind, 8 8 8 7 5
    tk2 = ['6S', '6C', '6H', '9S', 'TD']  # 6 three kind, 10 9 6 6 6
    tp = ['5S', '5H', '9D', '8C', '8S']   # 8,5 two pair and 9
    tp2 = ['4S', '4D', '9H', '9D', '3D']  # 9,4 two pair and 3
    hc = ['4S', '3H', '9D', '8C', 'TS']   # 10 high, 10 9 8 4 3
    hc2 = ['JS', '9H', '8D', '3C', '2C']  # Jack high, 11 9 8 3 2
    sal = ['5S', '4H', '3C', '2C', 'AC']  # 5 high, straight
    sfal = ['5S', '4S', '2S', '3S', 'AS'] # 5 high, straight flush
    
    def test_poker_example_1(self):
        '''Test poker with sf(straight flush) and fk(4 kinds).'''
 
        actual = poker.poker([TestPoker.sf,TestPoker.fk])
        expected = [['JC', 'TC', '9C', '8C', '7C']]
        self.assertEqual(actual, expected)
 
    def test_poker_example_2(self):
        '''Test poker with fh(full house) and fk(4 kinds).'''
 
        actual = poker.poker([TestPoker.fh,TestPoker.fk])
        expected = [['5S', '5H', '5D', '5C', 'KS']]
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

    def test_poker_example_16(self):
        '''Test hand rank func with straight.'''
 
        actual = poker.hand_rank(TestPoker.s1)
        expected = (4, 11)
        self.assertEqual(actual, expected)

    def test_poker_example_17(self):
        '''Test twopair func with 2 pairs.'''
 
        actual = poker.twopair([9, 8, 8, 5, 5])
        expected = (8, 5)
        self.assertEqual(actual, expected)

    def test_poker_example_18(self):
        '''Test twopair func with 2 pairs but didn't sort ranks.'''
 
        actual = poker.twopair([5, 5, 9, 8, 8])
        expected = (8, 5)
        self.assertEqual(actual, expected)

    def test_poker_example_19(self):
        '''Test twopair func with straight flush.'''
 
        actual = poker.twopair(poker.ranking(TestPoker.sf))
        expected = ()
        self.assertEqual(actual, expected)

    def test_poker_example_20(self):
        '''Test poker func with 2 hands and they are straight.'''
 
        actual = poker.poker([TestPoker.s1,TestPoker.s2])
        expected = [['JC', 'TC', '9C', '8S', '7C'], ['7D', '9D', '8H', 'TS', 'JD']]
        self.assertEqual(actual, expected)

    def test_poker_example_21(self):
        '''Test poker func with full house and straight.'''
 
        actual = poker.poker([TestPoker.fh,TestPoker.s1])
        expected = [['5S', '5H', '5D', '8C', '8S']]
        self.assertEqual(actual, expected)

    def test_poker_example_22(self):
        '''Test poker func with one pairs , high card and straight flush.'''
 
        actual = poker.poker([TestPoker.op,TestPoker.hc,TestPoker.sf])
        expected = [['JC', 'TC', '9C', '8C', '7C']]
        self.assertEqual(actual, expected)

    def test_poker_example_23(self):
        '''Test poker func with 2 straight flushs.'''
 
        actual = poker.poker([TestPoker.sf,TestPoker.sf2])
        expected = [['JC', 'TC', '9C', '8C', '7C'], ['JS', 'TS', '9S', '8S', '7S']]
        self.assertEqual(actual, expected)

    def test_poker_example_24(self):
        '''Test poker func with royal straight flush, 2 straight flushs.'''
 
        actual = poker.poker([TestPoker.rsf,TestPoker.sf,TestPoker.sf2,TestPoker.op])
        expected = [TestPoker.rsf]
        self.assertEqual(actual, expected)

    def test_poker_example_25(self):
        '''Test poker func with 3 straights.'''
 
        actual = poker.poker([TestPoker.sf,TestPoker.sf2,TestPoker.sf3])
        expected = [TestPoker.sf,TestPoker.sf2]
        self.assertEqual(actual, expected)

    def test_poker_example_26(self):
        '''Test poker func with 2 of 4kind cards.'''
 
        actual = poker.poker([TestPoker.fk,TestPoker.fk2])
        expected = [TestPoker.fk2]
        self.assertEqual(actual, expected)

    def test_poker_example_27(self):
        '''Test poker func with 2 of full house cards.'''
 
        actual = poker.poker([TestPoker.fh,TestPoker.fh2])
        expected = [TestPoker.fh2]
        self.assertEqual(actual, expected)

    def test_poker_example_28(self):
        '''Test poker func with 2 of flush cards.'''
 
        actual = poker.poker([TestPoker.f1,TestPoker.f2])
        expected = [TestPoker.f2]
        self.assertEqual(actual, expected)

    def test_poker_example_29(self):
        '''Test poker func with 3 of straight cards.'''
 
        actual = poker.poker([TestPoker.s1,TestPoker.s2,TestPoker.s3])
        expected = [TestPoker.s3]
        self.assertEqual(actual, expected)

    def test_poker_example_30(self):
        '''Test poker func with straight cards and two pair.'''
 
        actual = poker.poker([TestPoker.s3,TestPoker.tp])
        expected = [TestPoker.s3]
        self.assertEqual(actual, expected)

    def test_poker_example_31(self):
        '''Test poker func with 2 of one pairs cards.'''
 
        actual = poker.poker([TestPoker.op,TestPoker.op2])
        expected = [TestPoker.op]
        self.assertEqual(actual, expected)

    def test_poker_example_32(self):
        '''Test poker func with 2 of 3 kind cards.'''
 
        actual = poker.poker([TestPoker.tk,TestPoker.tk2])
        expected = [TestPoker.tk]
        self.assertEqual(actual, expected)

    def test_poker_example_33(self):
        '''Test poker func with 2 of high cards.'''
 
        actual = poker.poker([TestPoker.hc,TestPoker.hc2])
        expected = [TestPoker.hc2]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
