import json
from requests import Session

PROJECT_ID = "cec785fc-b681-438f-94b4-448abf07d117"
ENV = "demo"


def main():
    login = Login(PROJECT_ID, ENV)
    creator_id = login.get_creator_id()
    creator_email = login.get_email(creator_id)
    print("Project '{0}' was created by '{1}'.".format(login.projec_id, creator_email))


class Login(object):
    def __init__(self, project_id, env):
        self.projec_id = project_id
        self.env = env
        self.session = Session()

    def get_creator_id(self):
        url = "https://juvenal.{0}.globality.io/api/v2/project/{1}".format(self.env, self.projec_id)
        res = json.loads(self.session.get(url).text)
        return res["createdBy"]

    def get_email(self, user_id):
        url = "https://ariza.{0}.globality.io/api/v1/user/{1}".format(self.env, user_id)
        res = json.loads(self.session.get(url).text)
        return res["email"]


if __name__ == "__main__":
    main()