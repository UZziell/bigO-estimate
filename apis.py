import requests
import json


class Compiler:
    def __init__(self, user_input):
        self.url = "https://api.jdoodle.com/v1/execute"
        self.headers = {'Content-type': 'application/json'}
        self.payload = {"clientId": "348c57e0f1663952690f16dba2834798",
                        "clientSecret": "48d28c9a27eb657d3682c73276d55352ae67edbde419547bede62bc0c8c99a35",
                        "script": """{}""".format(user_input),
                        "language": "python3",
                        "versionIndex": "0",
                        }
        self.response = requests.post(url=self.url, data=json.dumps(self.payload), headers=self.headers)
        self.pyresponse = self.response.json()
        print("JDOODLE COMPILER STATUS CODE WAS: ", self.response.status_code)


# print("Status code: ", response.status_code)
# print("\n")
# print(" memory used was: {}\n".format(output['memory']),
#       "cputime was {}\n".format(output["cpuTime"]),
#       "output: \n\n", output['output'])

class DcodeFR:
    def __init__(self, points):
        self.url = "https://www.dcode.fr/api/"
        self.headers = {'Content-type': 'application/x-www-form-urlencoded'}
        self.payload = {"tool": "lagrange-interpolating-polynomial",
                        "points": f"{points}"
                        }

        self.response = requests.post(url=self.url, data=self.payload, headers=self.headers)
        self.output = self.response.json()

        print(f"DCODEFR API STATUS CODE WAS: ", self.response.status_code)
        # print("\n")
        # print("test output: {}".format(self.output['results']))
