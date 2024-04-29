import csv

def add_event(userid, date, time, event):
    with open('events.csv', 'a', newline='\n', encoding='utf-8') as f:
        fieldnames = ['userid', 'date', 'time', 'event']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'userid': userid, 'date': date, 'time': time, 'event': event})