import os
import time
from demo_opts import get_device
from luma.core.virtual import terminal
from PIL import ImageFont
import requests


def getLastTimelinePost():
    try:
        tweetRequest = requests.get('http://192.168.121.13:9111/api/status/last')
        
        if tweetRequest.status_code == 200:
            tweet = tweetRequest.json()
            return tweet
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False
    


def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)


def main():
    while True:
        #for fontname, size in [("ProggyTiny.ttf", 16), ("creep.bdf", 16), ("miscfs_.ttf", 12)]:
        fontname, size = ("miscfs_.ttf", 12)
        font = make_font(fontname, size) if fontname else None
        term = terminal(device, font)
        
        tweet = getLastTimelinePost()
        
        if tweet != False:
            term.println(tweet['data']['text'])
        else:
            term.println('Network error. Please check your internet connection.')
        
        term.flush()
        time.sleep(30)


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
