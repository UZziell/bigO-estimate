import requests
import json

url = "https://www.dcode.fr/api/"
headers = {'Content-type': 'application/x-www-form-urlencoded'}
payload = {"tool": "lagrange-interpolating-polynomial",
           "points": "(2,4)(4,16)(3,9)(5,25)"
           }

response = requests.post(url=url, data=payload, headers=headers)
output = response.json()

print(f"Status code: ", response.status_code)
print("\n")
print("test output: {}".format(output['results']))
