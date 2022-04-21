# Tests for find_euler_cycle.py
from nose.tools import assert_equal
from ..find_euler_cycle import find_euler_cycle

def test_find_euler_cycle0():
    G = [(1,2), (2,1)]
    exp = [1,2]
    obs = find_euler_cycle(G)
    assert_equal(exp, obs)
