# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(params=[1, 2, 3])
def data(request):
    return request.param


def test_one(data):
    print(f'testone{data}')


# if __name__ == '__main__':
#     pytest.main(['-s', '-v'])
