from bs4 import BeautifulSoup
import requests

def print_ad(title, link, price, info):
    # Help method for printing out the data
    print(80 * "*")
    print(f"Title: {title}\nPrice: {price}\nLink: {link}\nInfo: {info}\n")

url = "https://www.index.hr/oglasi/osobni-automobili/gid/27?num="

# There are lots of ads in classifieds
pages = 0
while pages == 0:
    try:
        pages_str = input("How many pages would you like to scan? ")
        pages = int(pages_str)
    except:
        print("Please enter integer")

for page in range(pages):
    page_response = requests.get(f"{url}{page+1}")
    soup = BeautifulSoup(page_response.content, "html.parser")
    ads = soup.find_all(class_="OglasiRezHolder")

    for ad in ads:
        try:
            ad_a = ad.a
            title = ad_a.find("span", class_="title px18").text.strip()
            link = ad_a["href"]
            price = ad_a.find("span", class_="price").text
            info = [i.text.strip().replace("\r\n", "") for i in ad_a.find("ul", class_="tags hide-on-small-only").find_all("li")]
            print_ad(title, link, price, info)
        except:
            pass
