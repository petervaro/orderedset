## INFO ##
## INFO ##

# Import python modules
from collections import OrderedDict
from itertools   import chain, count


#------------------------------------------------------------------------------#
# HACK: at some point implement a real OrderedSet in C
class OrderedSet(OrderedDict):
    """
    OrderedSet() -> new empty OrderedSet object
    OrderedSet(iterable) -> new OrderedSet object

    Build an ordered collection of unique elements.
    """

    __DISABLED = {'__setitem__',
                  '__getitem__',
                  '__delitem__',
                  '__reversed__',
                  'items',
                  'keys',
                  'values',
                  'move_to_end',
                  'popitem',
                  'setdefault',
                  'fromkeys',
                  'get',}

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    @classmethod
    def fromkeys(cls, iterable, value=None):
        """Inherited class guard."""
        raise AttributeError('{.__class__.__name__!r} object has no '
                             'attribute {!r}'.format(self, attribute))

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __getattribute__(self, attribute):
        """Inherited class guard."""
        if attribute in OrderedSet.__DISABLED:
            raise AttributeError('{.__class__.__name__!r} object has no '
                                 'attribute {!r}'.format(self, attribute))
        return super().__getattribute__(attribute)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self, iterable=()):
        """Initialize self."""
        super().__init__()
        self.update(iterable)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __repr__(self):
        """Return repr(self)"""
        return ('{.__class__.__name__}'
                '({!r})').format(self, list(OrderedDict.keys(self)))


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def isdisjoint(self, other):
        """Return True if two sets have a null intersection."""
        return set(OrderedDict.keys(self)).isdisjoint(other)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __le__(self, other):
        """Return self<=other"""
        return set(OrderedDict.keys(self)) <= other
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def issubset(self, other):
        """Report whether another set contains this OrderedSet."""
        return self <= set(other)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __lt__(self, other):
        """Return self<other"""
        return set(OrderedDict.keys(self)) < other


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __ge__(self, other):
        """Return self>=other"""
        return set(OrderedDict.keys(self)) >= other
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def issuperset(self, other):
        """Report whether this set contains another OrderedSet."""
        return self >= set(other)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __gt__(self, other):
        """Return self>other"""
        return set(OrderedDict.keys(self)) > other


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __or__(self, other):
        """Return self|other"""
        result = OrderedSet(self)
        result.update(other)
        return result
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def union(self, other, *others):
        """
        Return the union of sets as a new OrderedSet.

        (i.e. all elements that are in either set.)
        """
        result = OrderedSet(self)
        result.update(other)
        for other in others:
            result.update(other)
        return result


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __and__(self, other):
        """Return self&other"""
        if isinstance(other, (set, frozenset, OrderedSet)):
            custom = set(self) & set(other)
        else:
            raise TypeError('unsupported operand type(s) for &: '
                            '{.__class__.__name__!r} and '
                            '{.__class__.__name__!r}'.format(self, other))
        result = OrderedSet()
        for item in chain(self, other):
            if item in custom:
                result.add(item)
        return result
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def intersection(self, other, *others):
        """
        Return the intersection of two sets as a new OrderedSet.

        (i.e. all elements that are in both sets.)
        """
        custom = set(self).intersection(other, *others)
        result = OrderedSet()
        for item in chain(self, other, *others):
            if item in custom:
                result.add(item)
        return result


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __sub__(self, other):
        """Return self-other"""
        if isinstance(other, (set, frozenset, OrderedSet)):
            custom = set(self) - set(other)
        else:
            raise TypeError('unsupported operand type(s) for &: '
                            '{.__class__.__name__!r} and '
                            '{.__class__.__name__!r}'.format(self, other))
        result = OrderedSet()
        for item in chain(self, other):
            if item in custom:
                result.add(item)
        return result
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def difference(self, other, *others):
        """
        Return the difference of two or more sets as a new OrderedSet.

        (i.e. all elements that are in this set but not the others.)
        """
        custom = set(self).difference(other, *others)
        result = OrderedSet()
        for item in chain(self, other, *others):
            if item in custom:
                result.add(item)
        return result


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __xor__(self, other):
        """Return self^other"""
        if isinstance(other, (set, frozenset, OrderedSet)):
            custom = set(self) ^ set(other)
        else:
            raise TypeError('unsupported operand type(s) for &: '
                            '{.__class__.__name__!r} and '
                            '{.__class__.__name__!r}'.format(self, other))
        result = OrderedSet()
        for item in chain(self, other):
            if item in custom:
                result.add(item)
        return result
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def symmetric_difference(self, other):
        """
        Return the symmetric difference of two sets as a new OrderedSet.

        (i.e. all elements that are in exactly one of the sets.)
        """
        return self ^ set(other)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def copy(self):
        """Return a shallow copy of an OrderedSet."""
        return OrderedSet(self)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __ior__(self, other):
        """Return self|=other"""
        if not isinstance(other, (set, frozenset, OrderedSet)):
            raise TypeError('unsupported operand type(s) for &: '
                            '{.__class__.__name__!r} and '
                            '{.__class__.__name__!r}'.format(self, other))
        return self.update(other) or self
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def update(self, other, *others):
        """Update an OrderedSet with the union of itself and others."""
        OrderedDict.update(self, OrderedDict.fromkeys(chain(other, *others)))


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __iand__(self, other):
        """Return self&=other"""
        if not isinstance(other, (set, frozenset, OrderedSet)):
            raise TypeError('unsupported operand type(s) for &: '
                            '{.__class__.__name__!r} and '
                            '{.__class__.__name__!r}'.format(self, other))
        return self.intersection_update(other) or self
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def intersection_update(self, other, *others):
        """Update an OrderedSet with the intersection of itself and another."""
        custom = set(self)
        custom.intersection_update(other, *others)
        for item in OrderedDict.keys(self):
            if item not in custom:
                self.remove(item)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __isub__(self, other):
        """Return self-=other"""
        if not isinstance(other, (set, frozenset, OrderedSet)):
            raise TypeError('unsupported operand type(s) for &: '
                            '{.__class__.__name__!r} and '
                            '{.__class__.__name__!r}'.format(self, other))
        return self.difference_update(other) or self
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def difference_update(self, other, *others):
        """Remove all elements of another set from this OrderedSet."""
        custom = set(self)
        custom.difference_update(other, *others)
        for item in OrderedDict.keys(self):
            if item not in custom:
                self.remove(item)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __ixor__(self, other):
        """Return self^=other"""
        if not isinstance(other, (set, frozenset, OrderedSet)):
            raise TypeError('unsupported operand type(s) for &: '
                            '{.__class__.__name__!r} and '
                            '{.__class__.__name__!r}'.format(self, other))
        return self.symmetric_difference_update(other) or self
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def symmetric_difference_update(self, other):
        ("""Update an OrderedSet with the symmetric """
         """difference of itself and another.""")
        custom = set(self)
        custom.symmetric_difference_update(other)
        for item in OrderedDict.keys(self):
            if item not in custom:
                self.remove(item)
        k_view = OrderedDict.keys(self)
        for item in custom:
            if item not in k_view:
                self.add(item)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def add(self, item):
        """
        Add an element to an OrderedSet.

        This has no effect if the element is already present.
        """
        OrderedDict.__setitem__(self, item, None)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def remove(self, item):
        """
        Remove an element from an OrderedSet; it must be a member.

        If the element is not a member, raise a KeyError.
        """
        OrderedDict.__delitem__(self, item)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def discard(self, item):
        """
        Remove an element from an OrderedSet if it is a member.

        If the element is not a member, do nothing.
        """
        try:
            OrderedDict.__delitem__(self, item)
        except KeyError:
            pass


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def pop(self):
        """
        Remove and return an arbitrary OrderedSet element.
        Raises KeyError if the OrderedSet is empty.
        """
        OrderedDict.popitem(self)



#------------------------------------------------------------------------------#
if __name__ == '__main__':
    tu1 = 'hello', 'world', 'how', 'are', 'you?'
    tu2 = 'good', 'bye', 'world', 'you', 'silly'

    # Regular sets
    rs1 = set(tu1)
    rs2 = set(tu1)
    rs3 = set(tu2)
    print('Regular sets:', rs1, rs2, rs3, sep='\n', end='\n\n')

    # Ordered sets
    os1 = OrderedSet(tu1)
    os2 = OrderedSet(tu1)
    os3 = OrderedSet(tu2)
    print('OrderedSets:', os1, os2, os3, sep='\n', end='\n\n')

    # Tiny unit-testing framework
    TEST = (lambda n:
               (lambda b=[]:
                   b.append('\033[1m' + n + ' test(s):\033[0m') or
                   (lambda i=count(1):
                       (' '.join(b), b.append(str(next(i))))))())
    PASS = lambda b, _: print('\033[1m[ \033[32mPASS \033[39m]\033[0m', b)
    FAIL = lambda b, _: print('\033[1m[ \033[31mFAIL \033[39m]\033[0m', b)

    # Length checking
    indx = TEST('Length')
    try:
        assert indx() and (len(rs1) == len(rs2))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Membership checking
    indx = TEST('Membership')
    try:
        assert indx() and (('hello'     in rs1) == ('hello'     in os1))
        assert indx() and (('abcde'     in rs1) == ('abcde'     in os1))
        assert indx() and (('hello' not in rs1) == ('hello' not in os1))
        assert indx() and (('abcde' not in rs1) == ('abcde' not in os1))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # No common elements
    indx = TEST('Disjoint')
    try:
        assert indx() and (rs1.isdisjoint(rs2) == os1.isdisjoint(os2))
        assert indx() and (rs1.isdisjoint(rs3) == os1.isdisjoint(os3))
        assert indx() and (rs1.isdisjoint(os1) == os1.isdisjoint(rs1))
        assert indx() and (rs1.isdisjoint(os3) == os3.isdisjoint(rs1))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Subset checking
    indx = TEST('Subset')
    try:
        assert indx() and ((rs1 <= rs2) == (os1 <= os2))
        assert indx() and ((rs1 <= rs3) == (os1 <= os3))
        assert indx() and (rs1.issubset(rs2) == os1.issubset(os2))
        assert indx() and (rs1.issubset(rs3) == os1.issubset(os3))
        assert indx() and (rs1.issubset(os1) == os1.issubset(rs1))
        assert indx() and (rs1.issubset(os3) == os3.issubset(rs1))
        assert indx() and (rs1.issubset(tu1) == os1.issubset(tu1))
        assert indx() and (rs1.issubset(tu2) == os1.issubset(tu2))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Superset checking
    indx = TEST('Superset')
    try:
        assert indx() and ((rs1 >= rs2) == (os1 >= os2))
        assert indx() and ((rs1 >= rs3) == (os1 >= os3))
        assert indx() and (rs1.issuperset(rs2) == os1.issuperset(os2))
        assert indx() and (rs1.issuperset(rs3) == os1.issuperset(os3))
        assert indx() and (rs1.issuperset(os1) == os1.issuperset(rs1))
        assert indx() and (rs1.issuperset(os3) == os3.issuperset(rs1))
        assert indx() and (rs1.issuperset(tu1) == os1.issuperset(tu1))
        assert indx() and (rs1.issuperset(tu2) == os1.issuperset(tu2))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Comparison checking
    indx = TEST('Comparison')
    try:
        assert indx() and ((rs1 == rs2) == (os1 == os2))
        assert indx() and ((rs1 != rs2) == (os1 != os2))
        assert indx() and ((rs1 == rs3) == (os1 == os3))
        assert indx() and ((rs1 != rs3) == (os1 != os3))
        assert indx() and (rs1 == set(os1))
        assert indx() and (rs1 != set(os3))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Union checking
    indx = TEST('Union')
    try:
        assert indx() and (rs1 | rs2       == set(os1 | os2))
        assert indx() and (rs1 | rs3       == set(os1 | os3))
        assert indx() and (rs1 | rs2 | rs3 == set(os1 | os2 | os3))
        assert indx() and (rs1.union(tu1) == set(os1.union(tu1)))
        assert indx() and (rs1.union(tu1, tu2, rs2, rs3) ==
                           set(os1.union(tu1, tu2, os2, os3)))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Intersection checking
    indx = TEST('Intersection')
    try:
        assert indx() and (rs1 & rs2       == set(os1 & os2))
        assert indx() and (rs1 & rs3       == set(os1 & os3))
        assert indx() and (rs1 & rs2 & rs3 == set(os1 & os2 & os3))
        assert indx() and (rs1.intersection(tu1) == set(os1.intersection(tu1)))
        assert indx() and (rs1.intersection(tu1, tu2, rs2, rs3) ==
                           set(os1.intersection(tu1, tu2, os2, os3)))
        assert indx() and (rs1.intersection(os1) == set(os1.intersection(rs1)))
        assert indx() and (rs1.intersection(os3) == set(os3.intersection(rs1)))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Difference checking
    indx = TEST('Difference')
    try:
        assert indx() and (rs1 - rs2       == set(os1 - os2))
        assert indx() and (rs1 - rs3       == set(os1 - os3))
        assert indx() and (rs1 - rs2 - rs3 == set(os1 - os2 - os3))
        assert indx() and (rs1.difference(tu1) == set(os1.difference(tu1)))
        assert indx() and (rs1.difference(tu1, tu2, rs2, rs3) ==
                           set(os1.difference(tu1, tu2, os2, os3)))
        assert indx() and (rs1.difference(os1) == set(os1.difference(rs1)))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Symmetric Difference checking
    indx = TEST('Symmetric Difference')
    try:
        assert indx() and (rs1 ^ rs2      == set(os1 ^ os2))
        assert indx() and (rs1 ^ rs3      == set(os1 ^ os3))
        assert indx() and (rs1 ^ set(os3) == set(os1 ^ rs3))
        assert indx() and (rs1.symmetric_difference(tu1) ==
                           set(os1.symmetric_difference(tu1)))
        assert indx() and (rs1.symmetric_difference(tu2) ==
                           set(os1.symmetric_difference(tu2)))
        assert indx() and (rs1.symmetric_difference(os1) ==
                           set(os1.symmetric_difference(rs1)))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Copy checking
    indx = TEST('Copy')
    try:
        assert indx() and ((rs1 == rs1.copy()) == (os1 == os1.copy()))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Update checking
    indx = TEST('Update')
    try:
        rs10 = rs1.copy()
        rs11 = rs1.copy()
        rs12 = rs1.copy()
        rs13 = rs1.copy()

        os10 = os1.copy()
        os11 = os1.copy()
        os12 = os1.copy()
        os13 = os1.copy()

        rs10 |= rs2
        os10 |= os2

        rs11 |= rs2 | rs3
        os11 |= os2 | os3

        rs12.update(tu2)
        os12.update(tu2)

        rs13.update(tu1, tu2, rs1, rs2)
        os13.update(tu1, tu2, rs1, rs2)

        assert indx() and (rs10 == set(os10))
        assert indx() and (rs11 == set(os11))
        assert indx() and (rs12 == set(os12))
        assert indx() and (rs13 == set(os13))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Intersection Update checking
    indx = TEST('Intersection Update')
    try:
        rs10 = rs1.copy()
        rs11 = rs1.copy()
        rs12 = rs1.copy()
        rs13 = rs1.copy()

        os10 = os1.copy()
        os11 = os1.copy()
        os12 = os1.copy()
        os13 = os1.copy()

        rs10 &= rs2
        os10 &= os2

        rs11 &= rs2 & rs3
        os11 &= os2 & os3

        rs12.intersection_update(tu2)
        os12.intersection_update(tu2)

        rs13.intersection_update(tu1, tu2, rs1, rs2)
        os13.intersection_update(tu1, tu2, rs1, rs2)

        assert indx() and (rs10 == set(os10))
        assert indx() and (rs11 == set(os11))
        assert indx() and (rs12 == set(os12))
        assert indx() and (rs13 == set(os13))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Difference Update checking
    indx = TEST('Difference Update')
    try:
        rs10 = rs1.copy()
        rs11 = rs1.copy()
        rs12 = rs1.copy()
        rs13 = rs1.copy()

        os10 = os1.copy()
        os11 = os1.copy()
        os12 = os1.copy()
        os13 = os1.copy()

        rs10 -= rs2
        os10 -= os2

        rs11 -= rs2 - rs3
        os11 -= os2 - os3

        rs12.difference_update(tu2)
        os12.difference_update(tu2)

        rs13.difference_update(tu1, tu2, rs1, rs2)
        os13.difference_update(tu1, tu2, rs1, rs2)

        assert indx() and (rs10 == set(os10))
        assert indx() and (rs11 == set(os11))
        assert indx() and (rs12 == set(os12))
        assert indx() and (rs13 == set(os13))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Symmetric Difference Update checking
    indx = TEST('Symmetric Difference Update')
    try:
        rs10 = rs1.copy()
        rs11 = rs1.copy()
        rs12 = rs1.copy()

        os10 = os1.copy()
        os11 = os1.copy()
        os12 = os1.copy()

        rs10 ^= rs2
        os10 ^= os2

        rs11 ^= rs2 ^ rs3
        os11 ^= os2 ^ os3

        rs12.symmetric_difference_update(tu2)
        os12.symmetric_difference_update(tu2)

        assert indx() and (rs10 == set(os10))
        assert indx() and (rs11 == set(os11))
        assert indx() and (rs12 == set(os12))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())

    # Discard checking
    indx = TEST('Discard')
    try:
        rs1.discard('hello')
        rs2.discard('abcde')

        os1.discard('hello')
        os2.discard('abcde')

        assert indx() and (rs1 == set(os1))
        assert indx() and (rs2 == set(os2))
        PASS(*indx())
    except AssertionError:
        FAIL(*indx())
