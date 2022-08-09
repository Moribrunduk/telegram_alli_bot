import transliterate.exceptions
from transliterate import translit
import requests
from bs4 import BeautifulSoup

ru_text = "Архангельская область северодвинск"


def Weather(city):
    # city = city.replace(" ","+")
    Site = "https://www.google.ru/search?q=погода+" + str(city)
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    ful_page = requests.get(Site, headers=headers)
    soup = BeautifulSoup(ful_page.content, 'html.parser')

    # Локация
    search_soup_location = soup.findAll("div", {"class": "wob_loc q8U8x", "id": "wob_loc"})
    location = search_soup_location[0].text
    # Градусы
    search_soup_degrees = soup.findAll("span", {"class": "wob_t q8U8x"})
    degrees = search_soup_degrees[0].text
    # вероятность осадков
    search_soup_rain = soup.findAll("span", {"id": "wob_pp"})
    rain = search_soup_rain[0].text
    # влажность
    search_soup_hymidity = soup.findAll("span", {"id": "wob_hm"})
    hymidity = search_soup_hymidity[0].text
    # Ветер
    search_soup_wind = soup.findAll("span", {"id": "wob_ws"})
    wind = search_soup_wind[0].text
    weather = location \
              + "\n" + degrees + "\xb0" \
              + "\n" + "Вероятность осадков - " + rain \
              + "\n" + "Влажность - " + hymidity \
              + "\n" + "Ветер - " + wind

    return weather


"""x = input()
try:
    text = x
    ru_text = translit(text, reversed=True)
except transliterate.exceptions.LanguageDetectionError:
    text = x
    ru_text = text
print(ru_text)"""
