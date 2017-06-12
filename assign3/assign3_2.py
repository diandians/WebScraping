# requirement:
#
# Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html 
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah
# Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Sophi.html 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: P

# using urllib to get data
import urllib.request
from bs4 import BeautifulSoup


url = input('Enter - ')
count = int(input('count: '))
position = int(input('position: '))


for i in range(count):
	html = urllib.request.urlopen(url)
	soup = BeautifulSoup(html, 'html.parser')

	# Retrieve all of the span tags
	tags = soup('a')
	tag = tags[position - 1]
	url = tag.get('href', None)

print(tag.contents[0])

