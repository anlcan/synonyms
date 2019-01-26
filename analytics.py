import json
import logging
from logging.handlers import SysLogHandler, RotatingFileHandler
from sys import argv

from requests import post

WEB_API_KEY = ""
logger = logging.getLogger("synonym")
logger.addHandler(SysLogHandler())
logger.addHandler(RotatingFileHandler(filename="/Users/anlcan/projects/anlcan/synonyms/syn.log", mode='a', ))
logger.setLevel(logging.DEBUG)


def post_run(time, host):
    r = post('https://synonym-anlcan.firebaseio.com/runtime.json',
             params={'auth': WEB_API_KEY},
             data=json.dumps({"time": time, host: host}))

    logger.debug(r.status_code)
    logger.debug(r.json())


def post_syn(text, selected,syn,):
    r = post('https://synonym-anlcan.firebaseio.com/selection.json',
             params={'auth': WEB_API_KEY},
             data=json.dumps({"text": text, "syn": syn, "selected": selected}))

    logger.debug(r.status_code)
    logger.debug(r.json())


if __name__ == "__main__":
    logger.debug(argv)
    if argv.__len__() >= 4:
        syn = argv[3].split('\\r')
        post_syn(argv[1], argv[2], syn)
