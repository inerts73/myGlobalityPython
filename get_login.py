import json
from requests import Session

PROJECT_ID = "cec785fc-b681-438f-94b4-448abf07d117"
URL = "https://juvenal.demo.globality.io/api/v2/project/{}".format(PROJECT_ID)


def main():
    session = Session()
    res = session.get(URL)
    res_dict = json.loads(res.text)
    print(json.dumps(res_dict, indent=2))


if __name__ == "__main__":
    # project_id = sys.argv[1]
    main()