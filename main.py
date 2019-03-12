from datetime import datetime
ts = int("1541962108935000000")
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))