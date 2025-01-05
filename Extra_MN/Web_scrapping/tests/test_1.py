import requests

url = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png'
response = requests.get(url)
with open('image.jpg', 'wb') as file:
    file.write(response.content)