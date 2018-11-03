#!/usr/bin/env python3
import json, requests
import pandas
import csv

client_id = 
client_secret = 

def get_last_id():
    try:
        df = pandas.read_csv('sample.csv', usecols=['id'])[-1:]
        last_id = df.at[df.index.item(), 'id']
    except FileNotFoundError:
        last_id = 0
    return last_id

def add_user_details(df):
    df_details = pandas.DataFrame(columns=[
            'id', 'name', 'company',
            'blog', 'location', 'email',
            'public_repos', 'public_gists', 
            'followers', 'following',
            'created_at', 'updated_at'
    ])
    for login in df['login']:
        r = requests.get("https://api.github.com/users/" + login, params={
            'client_id': client_id,
            'client_secret': client_secret
        })
        s = pandas.read_json(r.text, typ='series')[[
            'id', 'name', 'company',
            'blog', 'location', 'email',
            'public_repos', 'public_gists', 
            'followers', 'following',
            'created_at', 'updated_at'
        ]]
        df_details = df_details.append(s, ignore_index=True)
    return df.join(df_details.set_index('id'), on='id')

def main():
    last_id = get_last_id()
    r = requests.get("https://api.github.com/users", params={
            'since': last_id, 
            'client_id': client_id,
            'client_secret': client_secret
    })
    df = pandas.read_json(r.text)
    df_join = add_user_details(df)
    # print(df.tail(1).index.item())
    if last_id == 0:
        df_join.to_csv('sample.csv', index=False)
    else:
        df_join.to_csv('sample.csv', mode='a', header=False, index=False)

if __name__ == "__main__":
    main()