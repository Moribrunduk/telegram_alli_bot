import requests
from bs4 import BeautifulSoup

DOLLAR_RUB = "https://www.google.ru/search?q=курс+доллара&newwindow=1&sxsrf=ALiCzsa_kIppVJjsxKVSgPNat06iyglZFg%3A1659972495921&source=hp&ei=jyvxYqvBNMWBxc8Pg4WXmAU&iflsig=AJiK0e8AAAAAYvE5n0-8rkmXIIHcv93jBKOTMMihFLwq&oq=курс&gs_lcp=Cgdnd3Mtd2l6EAMYADIQCAAQgAQQsQMQgwEQRhCCAjILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIICAAQgAQQsQMyCwgAEIAEELEDEIMBMggIABCABBCxAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgUIABCABDoHCCMQ6gIQJzoLCC4QgAQQsQMQgwE6DgguEIAEELEDEMcBENEDOhEILhCABBCxAxCDARDHARDRAzoOCC4QsQMQgwEQxwEQ0QM6BQguEIAEOgsIABCABBAKEAEQKjoJCAAQgAQQChABUJgEWJwXYIAkaARwAHgAgAHhAYgB-QeSAQUxLjQuMpgBAKABAbABAQ&sclient=gws-wiz"
headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
ful_page = requests.get(DOLLAR_RUB,headers=headers)
soup = BeautifulSoup(ful_page.content, 'html.parser')
convert = soup.findAll("span",{"class":"DFlfde SwHCTb"})
Dollar_rub = convert[0].text
print(Dollar_rub)