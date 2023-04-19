#!/usr/bin/env python3
import os
try:
    from urllib.request import urlopen,urljoin
    import re
except:
    os.system("pip install urllib")
    from urllib.request import urlopen,urljoin

def download_page(url):
    return urlopen(url).read().decode('utf-8')

def extract_image_location(page):
    img_regex = re.compile('<img[^>]+src=["\'](.*?)["\']',re.IGNORECASE)
    locations = img_regex.findall(page)
    if not locations:
        print("No image locations found.")
    else:
        for loc in locations:
            print(urljoin(target_url, loc))

if __name__ == "__main__":
    target_url = input("Enter Your Url:")
    try:
        page = download_page(target_url)
        # print(page)
        extract_image_location(page)
    except:
        print("Anything Went Wrong")
