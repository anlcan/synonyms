from sys import argv

from requests import get

KEY = ""
HOST = "http://words.bighugelabs.com/api/2/"


def run(input):
    URL = HOST + "/".join([KEY, input, "json"])
    response = get(URL)
    if response.status_code != 200:
        return

    answer = response.json()

    for key, value in answer.items():
        if value.__contains__("syn"):
            for syn in value.get("syn"):
                # result.append(syn)
                print(syn)


if __name__ == "__main__":
    run(argv[1])
