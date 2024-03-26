from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.yahoo.co.jp/"


res = req.urlopen(url)


soup = BeautifulSoup(res, 'html.parser')

li_list = soup.find_all("li", class_="_2ljd8LLu")

for li in li_list:
    print("li text =", li.get_text().strip())
