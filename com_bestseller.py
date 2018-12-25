from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
filename = "output/com_book.csv"
f = open(filename, "w")
headers = "Name;URL;Author;Price;Number of Ratings;Average Rating\n"
f.write(headers)
for page in range(1, 6):
    my_url = "https://www.amazon.com/gp/bestsellers/books/ref=zg_bs_pg_" + \
        str(page) + "?ie=UTF8&pg=" + str(page)
    uclient = urlopen(my_url)
    page_html = uclient.read()
    uclient.close()
    page_soup = BeautifulSoup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "zg_itemImmersion"})
    for container in containers:
        try:
            temp = container.findAll("a", {"class": "a-link-normal"})
            name = temp[0].text.strip()
        except:
            name = "Not available"
        try:
            temp1 = container.findAll("a", {"class": "a-link-normal"})
            url = "https://www.amazon.com" + temp1[0]["href"]
        except:
            url = "Not available"
        if container.findAll("div", {"class": "a-row a-size-small"})[0].a is None:
            author = container.findAll(
                "div",
                {"class": "a-row a-size-small"})[0].span.text
        else:
            temp2 = container.findAll("div", {"class": "a-row a-size-small"})
            author = temp2[0].a.text
        try:
            temp3 = container.findAll(
                "span",
                {"class": "a-size-base a-color-price"})
            price = temp3[0].text.strip()
        except:
            price = "Not available"
        try:
            temp4 = container.findAll(
                "a",
                {"class": "a-size-small a-link-normal"})
            nor = temp4[0].text
        except:
            nor = "Not available"
        try:
            temp5 = container.findAll("span", {"class": "a-icon-alt"})
            ar = temp5[0].text
            if container.findAll("span", {"class": "a-icon-alt"})[0].text == "Prime":
                ar = "Not available"
        except:
            ar = "Not available"
        f.write(
            name +
            ";" +
            url +
            ";" +
            author +
            ";" +
            price +
            ";" +
            nor +
            ";" +
            ar +
            "\n")
f.close()
