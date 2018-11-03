#!/usr/bin/env python3
import json, requests
import pandas
import csv
from pandas.io.json import json_normalize

def get_last_id():
    df = pandas.read_csv('sample.csv', usecols = ['id'])[-2:-1]
    last = df.at[df.index.item(), 'id']
    # last = df.tail(1).index.item() 마지막 인덱스 리턴
    return last
    

def main():
    print(get_last_id())
    r = requests.get("https://api.github.com/users")
    data = json.loads(r.text)
    df = pandas.read_json(r.text)
    df.to_csv('sample.csv')

if __name__ == "__main__":
    main()