import csv
import re
import time

import requests

from bs4 import BeautifulSoup

from user_agent import user_agent


beer_page_re = re.compile(r"https:\/\/untappd\.com\/b\/[\w-]+\/\d+")

# Time between requests in seconds
TIME_BETWEEN_REQUESTS = 1

# Filename for the CSV file
BEERS_LIST_FILENAME = "beers.csv"


def get_beer_info(url):
    headers = {
        "User-Agent": user_agent(),
    }

    response = requests.get(url, headers=headers)

    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    beer_data = {"url": url}

    beer_data["name"] = soup.find("div", class_="name").h1.text.strip()
    beer_data["brewery"] = soup.find("p", class_="brewery").a.text.strip()
    beer_data["style"] = soup.find("p", class_="style").text.strip()
    beer_data["abv"] = soup.find("p", class_="abv").text.strip().split()[0]
    beer_data["ibu"] = soup.find("p", class_="ibu").text.strip().split()[0]

    return beer_data


def prompt_for_urls():
    print(
        "Copy & paste all Untappd links you want to get\n"
        "the data for. Finish with an empty line."
    )

    urls = []

    while True:
        user_input = input().strip()

        if not user_input:
            break

        if not beer_page_re.match(user_input):
            print("Please check if this is a valid Untappd beer page link.")
            continue

        urls.append(user_input)

    return urls


def get_beers_list(urls):
    beers_list = []

    for i, url in enumerate(urls):
        if i > 0:
            time.sleep(TIME_BETWEEN_REQUESTS)

        print("{}/{}".format(i + 1, len(urls)))

        beer_info = get_beer_info(url)
        beers_list.append(beer_info)

    return beers_list


def write_csv(beers_list):
    with open(BEERS_LIST_FILENAME, "w") as beers_file:
        writer = csv.DictWriter(
            beers_file,
            fieldnames=["url", "brewery", "name", "style", "abv", "ibu"],
        )
        for beer in beers_list:
            writer.writerow(beer)


def main():
    urls = prompt_for_urls()
    beers_list = get_beers_list(urls)
    write_csv(beers_list)


if __name__ == "__main__":
    main()
