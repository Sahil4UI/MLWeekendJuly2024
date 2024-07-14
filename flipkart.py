#it is a package used to send req and recieve response
import urllib.request as url
# bs4 is used to fetch data(HTML)
import bs4
# Beautiful SOup4 ->Data Fetching
name = input("Enter Name : ")
path = "https://www.flipkart.com/search?q="+name
response = url.urlopen(path)
# print(response)
# HTML + XML - >LXML - Library XML
data = bs4.BeautifulSoup(response,features="lxml")
# print(data)
p_name=data.find("div",class_="KzDlHZ")
print(p_name.text)