def poker(hands):
    """
   ([hand, hand, ...])-> hand(s)
 
   Return the best hand(s) from list of hands
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
   """
    return max(hands, key=hand_rank)

def ranking(hand):
    '''
    (hand)-> [int,int,int,int,int]

    Return rank of the cards in hand
    >>> sf = ['JC', 'TC', '9C', '8C', '7C']
    >>> ranking(sf)
    [11, 10, 9, 8, 7]
    >>> tp = ['5S', '5H', '9D', '8C', '8S']
    >>> ranking(tp)
    [9, 8, 8, 5, 5]
    >>> sal = ['5S', '4H', '3C', '2C', 'AC']
    >>> ranking(sal)
    [5, 4, 3, 2, 1]
    '''
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    if ranks == [14,5,4,3,2]:
        ranks = [5,4,3,2,1]
    return ranks

def hand_rank(hand):
    """
   (hand)-> int
 
   Return the hand rank of a hand
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
   """
    ranks = ranking(hand)
    if straight(hand, ranks):
        if flush(hand):
            return (8, max(ranks))
        else:
            return (4, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif fullhouse(ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif twopair(ranks):
        return (2, twopair(ranks), kind(1, ranks))
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def straight(hand, ranks):
    """
   (hand)-> Bool
 
   Return True if hand is straight,
   false otherwise
 
   >>> sf = ['JC', 'TC', '9C', '8C', '7C']
   >>> straight(sf)
   True
   >>> fk = ['5S', '5H', '5D', '5C', 'KS']
   >>> straight(fk)
   False
   """

    return max(ranks)-min(ranks) == 4 and len(set(ranks)) == 5

def flush(hand):
    """
   (hand)-> Bool
 
   Return True if hand is flush, False otherwise.
 
   >>> sf = ['JC', 'TC', '9C', '8C', '7C']
   >>> flush(sf)
   True
   >>> fk = ['5S', '5H', '5D', '5C', 'KS']
   >>> flush(fk)
   False
   """
   
    suits = [s for r,s in hand]
 
    return len(set(suits)) == 1
 
def fullhouse(ranks):
    """
   (ranks)-> Bool
 
   Return True if hand is fullhouse,
   false otherwise
 
   >>> sf_ranks = [11, 10, 9, 8, 7]
   >>> fullhouse(sf_ranks)
   False
   >>> fk_ranks = [5, 5, 5, 5, 13]
   >>> fullhouse(fk_ranks)
   False
   >>> fh_ranks = [5, 5, 5, 8, 8]
   >>> fullhouse(fh_ranks)
   True
   """
   
    return True if kind(3, ranks) and kind(2, ranks) else False
 
def kind(n, ranks):
    """
   (ranks)-> int
 
   Return rank if hand is n kind,
   false otherwise
 
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
   """
   
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return 0
 
def twopair(ranks):
    """
   (ranks)-> tuple
 
   Return tuple of highpair and lowpair if hand is twopair,
   false otherwise
 
   >>> sf_ranks = [11, 10, 9, 8, 7]
   >>> twopair(sf_ranks)
   ()
   >>> tp_ranks = [5, 5, 9, 8, 8]
   >>> twopair(tp_ranks)
   (8, 5)
   """
    high_pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    return (high_pair, low_pair) if high_pair > low_pair else (low_pair, high_pair) if high_pair < low_pair else ()

