import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from requests import session

url = "https://levant.demo.globality.io/api/v1/translation"
data = {
    "inputFact": {
      "goal": "http://graph.globality.io/platform/providerHome/officeLocation",
      "factType": "AREA",
      "values": [
        {
          "coordinates": {
            "latitude": 52.3679843,
            "longitude": 4.903561399999944
          },
          "country": "Netherlands",
          "formatted": "Amsterdam, Netherlands",
          "locality": "North Holland",
          "province": "North Holland"
        }
      ]
    },
    "outputType": "PLACE"
  }
print(type(data))
#data = json.dumps(data)
print(type(data))
method = "post"

r = session().request(url=url, method=method, data=data,
                      headers=None, verify=False)

d = json.loads(r.content)
print(json.dumps(d, indent=2))