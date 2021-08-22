import re

def findStuff():
    
    url = 'http://instagram.com'
    Text = re.get(url)


    #Create a RegEx to look for ip addresses. The findall will look for any string that meets the given pattent in the Text
    #Same goes for Emails and other stuff

    IP = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', Text)    
    Email =  re.findall(r'([\w\.-]+@+[\w\.-]+\.+[\w]{1,5})', Text)
    subs = re.findall(r'[a-z0-9\.-]+\.+[a-z0-9.-]+\.+[a-z]{1,5}', Text) #the findall will return an empty list if there's no match. 
    JWT = re.findall(r'(ey+[\w]+\.[\w]+\.[\w]*)', Text)
    
    #Usually the findall function returns result in a list. 
    #So we use the for loop to print the result as a simple string.

    for i in IP:
    	#for item in the array IP, print the following...
    	print("Found an IP: " + str(i))

    for e in Email:
        print("Found emails: "+ str(e))
    
    for s in subs:
    	print("Found subdoamin: " + str(s))
    for j in JWT:
    	print("Found some JWT Tokens: "+ str(j))
  
findStuff()