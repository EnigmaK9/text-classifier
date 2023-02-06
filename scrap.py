import requests

url = "https://preview.redd.it/8c9ldxu5ygga1.png?width=1024&format=png&auto=webp&v=enabled&s=956f4379fe9f5b506d4c922ed19634771ea524d0"
response = requests.get(url)
open("image.png", "wb").write(response.content)
