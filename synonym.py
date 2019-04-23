from os import getenv
from sys import argv

from dotenv import load_dotenv
from requests import get
from functools import reduce
from operator import concat
from re import sub

load_dotenv()


def bighugelabs(input):
    HOST = "http://words.bighugelabs.com/api/2/"
    URL = HOST + "/".join([getenv("BIGHUGELABS_KEY"), input, "json"])
    response = get(URL)
    if response.status_code != 200:
        return

    answer = response.json()

    for key, value in answer.items():
        if value.__contains__("syn"):
            for syn in value.get("syn"):
                # result.append(syn)
                print(syn)


def thesaurus_altervista(input):
    """
    thesaurus.altervista.
    :param input:
    :return:
    """
    HOST = "http://thesaurus.altervista.org/thesaurus/v1"
    params = {
        "language": "en_US",
        "key": getenv("THESAURUS_KEY"),
        "word": input,
        "output": "json"
    }
    response = get(HOST, params=params)

    if response.status_code != 200:
        return

    answer = response.json()
    p = [x['list']['synonyms'].split("|") for x in answer['response']]
    k = reduce(concat, p)
    # k = [x.replace(' (generic term)', '') for x in k]
    k = [sub(" (.*)", '', x) for x in k]
    syn = list(dict.fromkeys(k))  # replace duplicates

    for s in syn:
        print(s)


if __name__ == "__main__":
    #bighugelabs(argv[1])
    thesaurus_altervista(argv[1])
