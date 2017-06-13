
# We provide two files for this assignment. One is a sample file where we give you the sum for
# your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_306894.json (Sum ends with 50)

import json
import urllib.request


while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved',len(data),'characters')
    # print(data)
    info = json.loads(data)

    count = 0
    sum_num = 0
    for item in info['comments']:
      count += 1
      sum_num += int(item['count'])

    print('Count: ', count)
    print('Sum: ', sum_num)
