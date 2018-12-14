import requests
import json

url = "https://api.jdoodle.com/v1/execute"
headers = {'Content-type': 'application/json'}

payload = {"clientId": "348c57e0f1663952690f16dba2834798",
           "clientSecret": "c6b227deeb8043545220457cd43ea3495d490fbd972acdc904df176864d37e4c",
           "script": """for i in range(1, 999):
    print(i*i)""",
           "language": "python3",
           "versionIndex": "0",
           }



response = requests.post(url=url, data=json.dumps(payload), headers=headers)

output = response.json()
print("Status code: ", response.status_code)
print("\n")
print(" memory used was: {}\n".format(output['memory']),
      "cputime was {}\n".format(output["cpuTime"]),
      "output: \n\n", output['output'])
