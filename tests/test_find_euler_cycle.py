# Tests for find_euler_cycle.py
from nose.tools import assert_equal
from ..find_euler_cycle import find_euler_cycle

def test_find_euler_cycle0():
    V = [1,2]
    E = [(1,2), (2,1)]
    exp = [1,2,2,1]
    obs = find_euler_cycle(V, E)
    assert_equal(exp, obs)

def test_find_euler_cycle1():
    V = [1,2,3]
    E = [(1,2), (2,3)]
    exp = []
    obs = find_euler_cycle(V, E)
    assert_equal(exp, obs)

def test_find_euler_cycle2():
    V = ['A','B','C','D']
    E = [('A','B'),('B','A'),('A','C'),('B','C'),
            ('B','D'),('D','B'),('C','D')]
    exp = []
    obs = find_euler_cycle(V, E)
    assert_equal(exp, obs)

def test_find_euler_cycle3():
    V = ['A','B','C','D']
    E = [('A','B'),('A','C'),('B','D'),('C','D')]
    exp = ['A','B','D','C','A']
    obs = find_euler_cycle(V, E)
    assert_equal(exp, obs)
