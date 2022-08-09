import transliterate.exceptions
from transliterate import translit
import requests
from bs4 import BeautifulSoup
ru_text = "Архангельская область северодвинск" вшк
ru_text = ru_text.replace(" ","+")
def Weather():
    global ru_text
    Site = "https://www.google.ru/search?q=погода+"+ru_text
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    ful_page = requests.get(Site, headers=headers)
    soup = BeautifulSoup(ful_page.content, 'html.parser')
    search_soup_location = soup.findAll("div", {"class": "wob_loc q8U8x","id":"wob_loc"})
    location = search_soup_location[0].text
    print(location)
    search_soup_weather = soup.findAll("span", {"class": "wob_t q8U8x"})
    weather = search_soup_weather[0].text
    print(weather+"\xb0")

def From_CB():
    Site = "https://www.google.ru/search?q=курс+доллара&newwindow=1&sxsrf=ALiCzsa_kIppVJjsxKVSgPNat06iyglZFg%3A1659972495921&source=hp&ei=jyvxYqvBNMWBxc8Pg4WXmAU&iflsig=AJiK0e8AAAAAYvE5n0-8rkmXIIHcv93jBKOTMMihFLwq&oq=курс&gs_lcp=Cgdnd3Mtd2l6EAMYADIQCAAQgAQQsQMQgwEQRhCCAjILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIICAAQgAQQsQMyCwgAEIAEELEDEIMBMggIABCABBCxAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgUIABCABDoHCCMQ6gIQJzoLCC4QgAQQsQMQgwE6DgguEIAEELEDEMcBENEDOhEILhCABBCxAxCDARDHARDRAzoOCC4QsQMQgwEQxwEQ0QM6BQguEIAEOgsIABCABBAKEAEQKjoJCAAQgAQQChABUJgEWJwXYIAkaARwAHgAgAHhAYgB-QeSAQUxLjQuMpgBAKABAbABAQ&sclient=gws-wiz"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    ful_page = requests.get(Site, headers=headers)
    soup = BeautifulSoup(ful_page.content, 'html.parser')
    search_soup = soup.findAll("span",{"class":"DFlfde SwHCTb"})
    Dollar_rub_cb = search_soup[0].text
    print(Dollar_rub_cb)



"""x = input()
try:
    text = x
    ru_text = translit(text, reversed=True)
except transliterate.exceptions.LanguageDetectionError:
    text = x
    ru_text = text
print(ru_text)"""
From_CB()
Weather()