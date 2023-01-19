"""
파일명 : p11_01_logging.py
설 명 : logging
생성일 : 2023-01-19
생성자 : Hanbi

since 2023.01.10 Copyright (C) by KandJang All right reserved. 
"""
import logging


def main():
    logging.basicConfig(level=logging.DEBUG)

    logging.debug('debug message')  # 10
    logging.info('info message')  # 20
    logging.warning('warning message')  # 30
    logging.error('error message')  # 40
    logging.critical('critical message')  # 50


main()
