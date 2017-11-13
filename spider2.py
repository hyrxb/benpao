import urllib
import urllib2
postobject = {"diaryid":'612'}
postdata = urllib.urlencode(postobject)
url = "xxxx"
request = urllib2.Request(url,postdata)
response = urllib2.urlopen(request)
print(response.read())

