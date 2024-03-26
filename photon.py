from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.yahoo.co.jp/"


res = req.urlopen(url)


soup = BeautifulSoup(res, 'html.parser')


span_text = soup.find("span", class_="_3u11DF4X _3Ib3sCcm").get_text()
print("span text = ", span_text)
