import requests
from bs4 import BeautifulSoup
import re

URL = 'http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80%D0%B5%D1%81_%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1%88%D1%82%D0%BE%D0%B2%D0%B8%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D1%96%D0%B2_%D1%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D1%83'

res = []
results = {}

regex_title = re.compile(r"(?:(?:(?:[А-ЩЬЮЯҐЄІЇа-щьюяґєії]+(?:(?:\-| {1,2}|, )))){1,8}[А-ЩЬЮЯҐЄІЇа-щьюяґєії]+)")
regex_mail = re.compile(r"((?:[А-ЩЬЮЯҐЄІЇа-щьюяґєії\-,a\.\" ]+)+)\s+([a-zA-z_]+@vsau\.vin\.ua)")
r = requests.get(URL)

soup = BeautifulSoup(r.text, 'html.parser')

headline = soup.find_all(class_="mw-headline")


#old logic but let it stay
def list_of_titles(headline):
    titles = []

    for el in headline:
        titles.extend(re.findall(r"(?:(?:(?:[А-ЩЬЮЯҐЄІЇа-щьюяґєії]+(?:(?:\-| {1,2}|, )))){1,8}[А-ЩЬЮЯҐЄІЇа-щьюяґєії]+)", str(el)))
    # print(titles)
    return titles


def task1(res):
    articles = soup.find_all('p')

    # print(articles)
    for el in articles:
        res.extend(re.findall(r"((?:(?:[А-ЩЬЮЯҐЄІЇа-щьюяґєії]+(?:(?:\-| |, )))){1,8}[А-ЩЬЮЯҐЄІЇа-щьюяґєії]+)\s<b>(?:([a-z_]+@vsau\.vin\.ua))", str(el)))
    print(res)


#I wanted to do it in one line, but this is already pretty awful code
def update_results_values(results):
    results = {(re.search(regex_title, k).group(0) if re.search(regex_title, k) else None): v for k, v in results.items()}

    for l in results.values():
        for idx, el in enumerate(l):
            match = re.search(regex_mail, el)
            if match:
                l[idx] = re.search(regex_mail, el).groups()
    return results


def clear_res(results):
    for l in results.values():
        for idx, el in enumerate(l):
            if el == '\n':
                l.pop(idx)
    return results


def task_asterisk(results):
    for p in soup.select('p'):
        results.setdefault(p.find_previous('h2').text, []).append(p.text)
    # print(results)
    results = update_results_values(results)
    results = clear_res(results)
    print(results)


if __name__ == '__main__':
    print("=========================TASK1=========================\n")
    task1(res)
    print("\n=========================TASK WITH *=========================\n")
    task_asterisk(results)
