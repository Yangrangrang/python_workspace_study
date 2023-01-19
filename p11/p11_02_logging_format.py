"""
파일명 : p11_02_logging_format.py
설 명 : logging format
    - %(asctime)s
    - %(levelname)s
    - %(filename)s
    - %(name)s
    - %(lineno)d
    - %(message)s
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

    # log 출력
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    for i in range(10):
        logging.info('{}번째 방문입니다.'.format(i))


main()

"""
2023-01-19 09:45:37,060 - INFO - p11_02_logging_format.py - root - 34 - 0번째 방문입니다.
2023-01-19 09:45:37,060 - INFO - p11_02_logging_format.py - root - 34 - 1번째 방문입니다.
2023-01-19 09:45:37,060 - INFO - p11_02_logging_format.py - root - 34 - 2번째 방문입니다.
2023-01-19 09:45:37,060 - INFO - p11_02_logging_format.py - root - 34 - 3번째 방문입니다.
2023-01-19 09:45:37,060 - INFO - p11_02_logging_format.py - root - 34 - 4번째 방문입니다.
2023-01-19 09:45:37,060 - INFO - p11_02_logging_format.py - root - 34 - 5번째 방문입니다.
2023-01-19 09:45:37,060 - INFO - p11_02_logging_format.py - root - 34 - 6번째 방문입니다.
2023-01-19 09:45:37,060 - INFO - p11_02_logging_format.py - root - 34 - 7번째 방문입니다.
2023-01-19 09:45:37,060 - INFO - p11_02_logging_format.py - root - 34 - 8번째 방문입니다.
2023-01-19 09:45:37,060 - INFO - p11_02_logging_format.py - root - 34 - 9번째 방문입니다.
"""