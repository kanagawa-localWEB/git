from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.yahoo.co.jp/"


res = req.urlopen(url)


soup = BeautifulSoup(res, 'html.parser')


title1 = soup.find("h1").string
print("title = ", title1)

p_list = soup.find_all("p")

for p in p_list:
	print(p.get_text())
