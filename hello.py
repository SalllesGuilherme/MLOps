#!/bin/python
import logging

def hello():
    print('Hello Git!')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    hello()