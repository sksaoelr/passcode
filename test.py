import requests

param = {
    'token': '$2y$10$z0PDxiNJeRYH6u32sCbkT.ZgdyVsp/VvHHjYsruMwPs8CYXfOAgSW',
    'limit': 1
}
url = f"https://www.cryptohub.or.kr/api/v1/news"
response = requests.post(url, param)

print(response.text)