import requests
import re
import urllib
url = 'http://challenge01.root-me.org/web-client/ch12/ch12.html'
r = requests.get(url=url)
#print(r.text)
#var pass = unescape("unescape%28%22String.fromCharCode%2528104%252C68%252C117%252C102%252C106%252C100%252C107%252C105%252C49%252C53%252C54%2529%22%29");
str = urllib.parse.unquote('104%2C68%2C117%2C102%2C106%2C100%2C107%2C105%2C49%2C53%2C54')
str2 = ''
list2 = str.split(',')
for list in list2:
	str2 +=chr(int(list))
print(str2)