import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/introduction-to-python-programming/').read()
soup=bs.BeautifulSoup(sauce,'lxml')

print(soup)