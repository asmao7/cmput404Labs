
import requests
print(requests.__version__)

content = requests.get("http://google.com")
print(content)


