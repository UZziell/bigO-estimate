import requests
import json


class Api:
    def __init__(self, user_input):
        self.url = "https://api.jdoodle.com/v1/execute"
        self.headers = {'Content-type': 'application//x-www-form-urlencoded'}
        self.payload = {"clientId": "348c57e0f1663952690f16dba2834798",
                        "clientSecret": "c6b227deeb8043545220457cd43ea3495d490fbd972acdc904df176864d37e4c",
                        "script": """{}""".format(user_input),
                        "language": "python3",
                        "versionIndex": "0",
                        }
        self.response = requests.post(url=self.url, data=json.dumps(self.payload), headers=self.headers)
        self.finalstring = self.response.json()

# print("Status code: ", response.status_code)
# print("\n")
# print(" memory used was: {}\n".format(output['memory']),
#       "cputime was {}\n".format(output["cpuTime"]),
#       "output: \n\n", output['output'])
