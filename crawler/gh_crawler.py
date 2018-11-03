#!/usr/bin/env python3
import json, requests
import pandas
import csv

def get_last_id():
        df = pandas.read_csv('sample.csv', usecols = ['id'])[-1:]
        last_id = df.at[df.index.item(), 'id']
    # last = df.tail(1).index.item() 마지막 인덱스 리턴
    return last_id
    

def main():
    data = json.loads(r.text)
    df = pandas.read_json(r.text)

if __name__ == "__main__":
    main()