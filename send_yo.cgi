#!/usr/bin/python
# -*- coding: utf-8 -*-
#import cgi

import urllib
import urllib2


url = "http://api.justyo.co/yo/"
params = {"api_token":"input_Api_token","username":"NYARU"}
params = urllib.urlencode(params)

req = urllib2.Request(url)
req.add_header("Content-Type","application/x-www-form-urlencoded")
req.add_data(params)

#仕様上1分に1Yoしかできないっぽい。
#それ以上するとBadRequestが返ってくる
try:
	res = urllib2.urlopen(req)
except:
	x = "Error, Only 1 Yo/min"
else:
	x = "OK! Thank you!"

print "Content-type: text/html\n"
print
print x
