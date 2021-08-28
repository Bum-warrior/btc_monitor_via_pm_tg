import bs4
import requests
import cfg

urls = {'BTC/USD': cfg.btc_usd, 'ETH/USD': cfg.eth_usd, 'USD/RUB': cfg.usd_rub}


def html(url):
    page = requests.get(url, cfg.headers)
    pretty = bs4.BeautifulSoup(page.text, 'html.parser')
    return pretty.prettify()


def get(url):
    page = requests.get(url, cfg.headers)
    '''class="BNeawe iBp4i AP7Wnd"'''
    parser = bs4.BeautifulSoup(page.text, 'html.parser')
    res = parser.find_all(class_="BNeawe iBp4i AP7Wnd")
    return res[1].text


def rate():
    try:
        global urls
        keys = list(urls.keys())
        string = 'Текущие курсы:'
        for i in keys:
            string = string + '\n ' + i + ' ' + get(urls[i])
        return string
    except:
        return 'Гугл сломался, курсов не будет'
