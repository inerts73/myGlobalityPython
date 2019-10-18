import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from requests import session

method = "get"
url = "https://miranda.prod.globality.io/api/v1/assertion?subject_id=622fd264-24b4-41bc-b652-480208f08a49&source_type=QNA_SESSION&relation_type=OPERATES_IN_INDUSTRY&limit=2000"

r = session().request(url=url, method=method,
                      headers=None, verify=False)

d = json.loads(r.content)
print(json.dumps(d, indent=2))
