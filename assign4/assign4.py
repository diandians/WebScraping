import urllib.request
import xml.etree.ElementTree as ET

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    # url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved',len(data),'characters')
    # print(data)
    tree = ET.fromstring(data)


    counts = tree.findall('.//count')
    print("Count: ", len(counts))
    sum_num = 0
    for count in counts:
        sum_num += int(count.text)
    print("Sum: ", sum_num)