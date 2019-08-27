import json
import sys
from requests import Session

URL = "https://juvenal.demo.globality.io/api/v2/project/{}"


def main(project_id):
    session = Session()
    res = session.get(URL.format(project_id))
    res_dict = json.loads(res.text)
    # print(res_dict)
    print(json.dumps(res_dict, indent=2))


if __name__ == "__main__":
    # project_id = "cec785fc-b681-438f-94b4-448abf07d117"
    project_id = sys.argv[1]
    main(project_id)