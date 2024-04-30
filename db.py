import csv
import pandas as pd


def add_event(userid, date, time, event):
    with open('events.csv', 'a', newline='\n', encoding='utf-8') as f:
        fieldnames = ['userid', 'date', 'time', 'event']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'userid': userid, 'date': date, 'time': time, 'event': event})


def del_event(userid, e, d, t):
    df = pd.read_csv('events.csv')
    df = df.drop(df[(df['userid'] == userid) &
                    (df['date'] == d) &
                    (df['time'] == t) &
                    (df['event'] == e)].index)
    df.to_csv('events.csv', index=False)


def view_event(userid):
    with open('events.csv', 'r', newline='\n', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        a = []
        for line in reader:
            if line['userid'] == userid:
                a.append(line)
        return a
