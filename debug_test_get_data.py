import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from requests import session

#url = "https://juvenal.demo.globality.io/api/v2/company_event?event_type=CompanyOnboardingCompleted&limit=1000"
url = "https://juvenal.prod.globality.io/api/v2/company_event?event_type=CompanyOnboardingCompleted&limit=1000"

data = {}
data = json.dumps(data)
print(data)
method = "get"

r = session().request(url=url, method=method, data=data,
                      headers=None, verify=False)

d = json.loads(r.content)
print(json.dumps(d, indent=2))
