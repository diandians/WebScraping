# requirement: 
# website to access
# Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_306893.html (Sum ends with 47)



# using socket to get data
# import socket
# from bs4 import BeautifulSoup

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# url = input('Enter - ')
# words = url.split('/')
# host = words[2]

# mysock.connect((host, 80))
# mysock.send(('GET ' + url + ' HTTP/1.0\n\n').encode(encoding='utf-8'))

# html=''
# while True:
#     data = mysock.recv(512)
#     if ( len(data) < 1 ) :
#         break
#     html += str(data)

# mysock.close()

# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anchor tags
# tags = soup('a')
# print(tags)
# for tag in tags:
#     print(tag.get('href', None))



# using urllib to get data
import urllib.request
from bs4 import BeautifulSoup


url = input('Enter - ')
html = urllib.request.urlopen(url)
  
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')
sum_num = 0
count = 0
for tag in tags:
	sum_num += int(tag.contents[0])
	count += 1

print("Count "+ str(count))
print("Sum " + str(sum_num))