import time
import datetime
import json

print(time.time())
print(datetime.datetime.today().strftime("%Y-%m-%d"))
print((datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d"))

with open('config.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data['bucket'])

