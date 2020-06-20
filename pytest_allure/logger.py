# -*- coding: utf-8 -*-

import os
import time
import logging

LOG_DIR = os.path.dirname(os.path.abspath(__file__)) + '/logs/'


def getLogger(loggerName):
    file_name = LOG_DIR + time.strftime('%Y%m%d%H%M',
                                        time.localtime(time.time())) + '.log'
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler(file_name)
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    logger = logging.getLogger(loggerName)
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.setLevel(logging.DEBUG)

    return logger
