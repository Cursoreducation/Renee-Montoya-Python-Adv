import urllib.request
import urllib.parse
import re
import requests
from bs4 import BeautifulSoup


url = "http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80%D0%B5%D1%81_%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1%88%D1%82%D0%BE%D0%B2%D0%B8%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D1%96%D0%B2_%D1%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D1%83"

req_2 = requests.get(url)
soup = BeautifulSoup(req_2.text, 'html.parser')

values = {'s': 'python programming',
          'submit': 'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

# names = re.findall(r'((?:(?:[А-ЯҐЄІЇа-яґєії]+(?:(?:\-| |, )))){1,5}[А-ЯҐЄІЇа-яґєії]+))', str(respData))
emails = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', str(respData))
list_emails = []
list_emails.append(emails)

names_with_emails = []
search = soup.find_all('p')
for data in search:
    names_with_emails.extend(re.findall(r"((?:(?:[А-ЯҐЄІЇа-яґєії]+(?:(?:\-| |, )))){1,5}[А-ЯҐЄІЇа-яґєії]+)\s<b>([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", str(data)))


if __name__ == "__main__":
    print("All emails.\n")
    print(list_emails)
    print("\nNames with emails.\n")
    print(names_with_emails)
