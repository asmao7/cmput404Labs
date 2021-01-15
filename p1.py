import requests
print(requests.__version__)

# part 5
content = requests.get("http://google.com")
print(content)

# part 7 - download file
my_url = "https://raw.githubusercontent.com/asmao7/cmput404labs/main/p1.py"
content = requests.get(my_url)
print(content.text)

filename = content.url[my_url.rfind('/')+1:]
with open(filename, 'wb') as out_file :
    out_file.write(content.content)