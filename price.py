import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
        self.response = requests.get(url = self.url, headers= self.user_agent).text
        self.soup = BeautifulSoup(self.response , 'lxml')

    def product_title(self):
        title = self.soup.find('span' , { 'class' : "B_NuCI"})
        if title is not None:
            return title.text.strip()
        else:
            return 'Tag not found'


    def product_price(self):
        price = self.soup.find('div' , {'class' : "_30jeq3 _16Jk6d"})
        if price is not None:
            return price.text.strip()
        else:
            return 'Tag not found'

device = PriceTracer(url = 'https://www.flipkart.com/apple-iphone-13-pro-max-graphite-512-gb/p/itmbe5170f10a29f?pid=MOBG6VF5MNKYGQMA&lid=LSTMOBG6VF5MNKYGQMACWMKF8&marketplace=FLIPKART&q=iphone+13+pro+max&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=organic&iid=a4a3fc4c-65a0-4e93-966f-cba0ad32fbe3.MOBG6VF5MNKYGQMA.SEARCH&ppt=sp&ppn=sp&ssid=u0d0qpncgw0000001665149300566&qH=5556902974bb931a')
print(device.product_title())
print(device.product_price())

device1 = PriceTracer(url = 'https://www.flipkart.com/apple-iphone-11-white-128-gb/p/itme32df47ea6742?pid=MOBFWQ6B7KKRXDDS&lid=LSTMOBFWQ6B7KKRXDDSULUZ0N&marketplace=FLIPKART&q=mobile+phone&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=f12e8b10-efd7-42d1-877b-471daf2c268d.MOBFWQ6B7KKRXDDS.SEARCH&ppt=pp&ppn=pp&ssid=ofauteu7hs0000001665153097947&qH=37695f7554f510f0')
print(device1.product_title())
print(device1.product_price())



