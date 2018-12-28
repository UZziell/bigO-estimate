import requests
import json


class Api:
    def __init__(self, user_input):
        self.url = "https://api.jdoodle.com/v1/execute"
        self.headers = {'Content-type': 'application/json'}
        self.payload = {"clientId": "348c57e0f1663952690f16dba2834798",
                        "clientSecret": "48d28c9a27eb657d3682c73276d55352ae67edbde419547bede62bc0c8c99a35",
                        "script": """{}""".format("print(666)"),
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
