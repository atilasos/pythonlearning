import socket
import re

url = raw_input('Enter url - ')
# shortcut for ass data
if len(url) < 1: url = 'http://www.pythonlearn.com/code/intro-short.txt'
host = (re.findall('http://(.+?)/', url))[0]
print 'Connecting to host:', host
url = 'GET ' + url + ' HTTP/1.0\n\n'
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
mysock.send(url)
working = mysock.recv(512)
mysock.close()

print re.findall('.*?ied: (.+?)\r', working)
print re.findall('.*?ag: "(.+?)"', working)
print re.findall('.*?ength: (.+?)\r', working)
print re.findall('.*?trol: (.+?)\r', working)
print re.findall('.*?ype: (.+?)\r', working)
