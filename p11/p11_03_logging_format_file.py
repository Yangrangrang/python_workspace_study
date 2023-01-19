"""
파일명 : p11_03_logging_format_file.py
설 명 : logging format + file
생성일 : 2023-01-19
생성자 : Hanbi

since 2023.01.10 Copyright (C) by KandJang All right reserved. 
"""
import logging


def main():
    # log 생성
    logger = logging.getLogger()

    # log 레벨
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(lineno)d - %(message)s')

    # console log 출력
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # file log 출력
    file_handler = logging.FileHandler('my.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    for i in range(10):
        logging.info('{}번째 방문입니다.'.format(i))


main()

