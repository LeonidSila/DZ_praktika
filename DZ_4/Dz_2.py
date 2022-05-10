from datetime import datetime
import requests
def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):
    if not (currency_code and url):
        return None
    currency_code = currency_code.upper()
    respond = requests.get(url)
    if respond.ok:
        cur = respond.text.split(currency_code)
        if len(cur) == 1:
            return None
        value = cur[1].split("</Value>")[0].split("<Value>")[1]
        value = cur[1].split("</Value>")[0].split("<Value>")[1]
        date = respond.headers["Date"]
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()
        return (value, date)
    else:
        return None
print((currency_rates("Usd")))
print((currency_rates("eUR")))
