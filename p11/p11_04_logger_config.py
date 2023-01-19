"""
파일명 : p11_04_logger_config.py
설 명 : 
생성일 : 2023-01-19
생성자 : Hanbi

since 2023.01.10 Copyright (C) by KandJang All right reserved. 
"""
import logging
import logging.config
import json
import os


with open('logging.json', 'rt') as f:
    config = json.load(f)

    logging.config.dictConfig(config)
    logger = logging.getLogger()

    for i in range(10):
        logger.info('logging.json test!')
