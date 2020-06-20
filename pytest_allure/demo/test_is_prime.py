# -*- coding: utf-8 -*-

import pytest


def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


@pytest.mark.parametrize(
    "num, exp",
    [(1, False), (13, True), (4, False)],
    ids=["case1", "case2", "case3"]
)
def test_is_prime(num, exp):
    assert is_prime(num) == exp
