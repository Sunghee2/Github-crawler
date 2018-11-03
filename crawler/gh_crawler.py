#!/usr/bin/env python3
import json, requests
import pandas
import csv

def get_last_id():
    try:
        df = pandas.read_csv('sample.csv', usecols=['id'])[-1:]
        last_id = df.at[df.index.item(), 'id']
        print(df.tail(1).index.item()) # 마지막 인덱스
    except FileNotFoundError:
        last_id = 0
    return last_id
    

def main():
    last_id = get_last_id()
    r = requests.get("https://api.github.com/users", params={'since': last_id})
    data = json.loads(r.text)
    df = pandas.read_json(r.text)
    if last_id == 0:
        df.to_csv('sample.csv')
    else:
        df.to_csv('sample.csv', mode='a', header=False)

if __name__ == "__main__":
    main()