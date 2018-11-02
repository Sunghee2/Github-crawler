#!/usr/bin/env python3
import json, requests
import pandas
import csv
from pandas.io.json import json_normalize

def get_last_id():
    df = pandas.read_csv('sample.csv', usecols=['id'])

def main():
    r = requests.get("https://api.github.com/users")
    data = json.loads(r.text)
    df = pandas.read_json(r.text)
    df.to_csv('sample.csv')

if __name__ == "__main__":
    main()