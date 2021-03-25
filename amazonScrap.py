import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def infocheck(context):
        price = soup.find("span", attrs={'class':'priceText'}).string.strip()
        if price != '$4,000':
            context.bot.send_message(chat_id=YOUR_CHAT_ID, text=f'Price changed in: {URL}.')

# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("span", attrs={'class':'priceText'}).string.strip()
    except AttributeError:
        price = ""
    return price


# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = ""

    return available

if __name__ == '__main__':

    # Headers for request
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    URL = ''
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Function calls to display all necessary product information
    print("Price =", get_price(soup))
    print("Stock =", get_availability(soup))
    print()
    print()


def init(context):
    context.bot.send_message(chat_id=YOUR_CHAT_ID, text=f'Bot Initialized.')

updater = Updater(token='YOUR_TOKEN', use_context=True)
updater.job_queue.run_once(init,when=0)
updater.job_queue.run_repeating(infocheck, interval=60, first=0)
updater.start_polling()
