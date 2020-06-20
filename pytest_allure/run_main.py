# -*- coding: utf-8 -*-

import os
import pytest

if __name__ == '__main__':
    pytest.main(['-s', '--alluredir', 'report/xml', 'testcases/'])
    os.system("allure generate report/xml/ -o report/html/ --clean")