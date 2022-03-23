from requests import get, utils

def currency_rates(valute):
    response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))
    content = response.split('Valute ID=')
    for el in content:
        if valute.upper() in el:
            print(valute.upper())
            print(float(el.replace('/', '').split('<Value>')[1].replace(',', '.')))

if __name__ == '__main__':
    currency_rates('usd')
    currency_rates('eur')
