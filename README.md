# Untappd Beer Info Fetcher

This is a simple Python program that allows you to fetch info for multiple beers you have Untappd links to.

Useful for making spreadsheets of beers you’ve bought, plan to share and so on.

This is the data that it currently gets:

* Name
* Brewery
* Style
* ABV
* IBU

# Setup

The recommended setup method is using virtualenv.

    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

# Running

Just run `python fetcher.py`. If you use virtualenv, first run `source .venv/bin/activate` to run the app in the previously created virtual environment.

    source .venv/bin/activate
    python fetcher.py

The app asks you to copy & paste all your Untappd links. Note that on each line there should be only one Untappd link, without any other text before and after it. Don‘t worry: the app warns you in case it doesn’t know what to do with what you pasted.

Finish with an empty line.

The app then fetches the data from Untappd, notifying you about the progress.

When all is done, a CSV file containing info about the beers is created.

# Using the CSV file

One way to make use of the CSV file is to import it to Google Sheets.

It can be done with **File → Import**. Also, you can simply copy & paste the contents and then split it with **Data → Split text to columns**.
