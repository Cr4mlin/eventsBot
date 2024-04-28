import csv

def add_event(userid, date, time, event):
    with open('events.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow({'userid': userid, 'date': date, 'time': time, 'event': event})