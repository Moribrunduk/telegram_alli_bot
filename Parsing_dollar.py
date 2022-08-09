import requests
from bs4 import BeautifulSoup
from random import randint

def From_CB():
    Site = "https://www.google.ru/search?q=курс+доллара&newwindow=1&sxsrf=ALiCzsa_kIppVJjsxKVSgPNat06iyglZFg%3A1659972495921&source=hp&ei=jyvxYqvBNMWBxc8Pg4WXmAU&iflsig=AJiK0e8AAAAAYvE5n0-8rkmXIIHcv93jBKOTMMihFLwq&oq=курс&gs_lcp=Cgdnd3Mtd2l6EAMYADIQCAAQgAQQsQMQgwEQRhCCAjILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIICAAQgAQQsQMyCwgAEIAEELEDEIMBMggIABCABBCxAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgUIABCABDoHCCMQ6gIQJzoLCC4QgAQQsQMQgwE6DgguEIAEELEDEMcBENEDOhEILhCABBCxAxCDARDHARDRAzoOCC4QsQMQgwEQxwEQ0QM6BQguEIAEOgsIABCABBAKEAEQKjoJCAAQgAQQChABUJgEWJwXYIAkaARwAHgAgAHhAYgB-QeSAQUxLjQuMpgBAKABAbABAQ&sclient=gws-wiz"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    ful_page = requests.get(Site, headers=headers)
    soup = BeautifulSoup(ful_page.content, 'html.parser')
    search_soup = soup.findAll("span",{"class":"DFlfde SwHCTb"})
    Dollar_rub_cb = search_soup[0].text
    return Dollar_rub_cb

def From_Aliexpress():
    Site = "https://www.google.ru/search?q=курс+доллара+али&newwindow=1&sxsrf=ALiCzsZJFiOoYJ3zUuBHeooPFSC_N5jMQA%3A1659973866026&source=hp&ei=6TDxYrziO4jRrgS19rrwBA&iflsig=AJiK0e8AAAAAYvE--vrpQhVOnI7iVsc4aNjleAjQTD04&ved=0ahUKEwj8-vjEzLf5AhWIqIsKHTW7Dk4Q4dUDCAc&uact=5&oq=курс+доллара+али&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgQIIxAnOhAIABCABBCHAhCxAxCDARAUOhEILhCABBCxAxCDARDHARDRAzoICAAQgAQQsQM6CQgjECcQRhCCAjoICAAQsQMQgwFQAFi3JWDNLmgAcAB4AIABjwGIAZAKkgEEMTQuMpgBAKABAQ&sclient=gws-wiz"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    ful_page = requests.get(Site, headers=headers)
    soup = BeautifulSoup(ful_page.content, 'html.parser')
    search_soup = soup.findAll("td", {"class": "OSrXXb TUOsUe"})
    dollar_Ali = search_soup[8].text
    return dollar_Ali
def Love_words():
    Site = "https://love.romanticcollection.ru/blog/500-trogatelnyh-komplimentov-devushke/"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    ful_page = requests.get(Site, headers=headers)
    soup = BeautifulSoup(ful_page.content, 'html.parser')
    compliments = soup.findAll("li")
    compliment = compliments[randint(13,512)].text
    return compliment
