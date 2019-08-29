import json
from requests import Session

PROJECT_ID = "6f87c214-48ef-4b93-a240-3bf27d755919"
ENV = "demo"


def main():
    login = Login(PROJECT_ID, ENV)
    creator_id = login.get_creator_id()
    creator_email = login.get_email_by_user_id(creator_id)

    print("*" * 80)
    print("Project '{0}' was created by '{1}'.".format(login.projec_id, creator_email))
    print("*" * 80)

    matching_provider_ids = login.get_matching_provider_ids()
    for matching_id in matching_provider_ids:
        print()
        print(login.get_company_name_by_id(matching_id))
        output(login.get_emails_by_company_id(matching_id))


def output(data):
    print(json.dumps(data, indent=2))


class Login(object):
    def __init__(self, project_id, env):
        self.projec_id = project_id
        self.env = env
        self.session = Session()

    def get_response(self, url):
        return json.loads(self.session.get(url).text)

    def get_creator_id(self):
        url = "https://juvenal.{0}.globality.io/api/v2/project/{1}".format(self.env, self.projec_id)
        return self.get_response(url)["createdBy"]

    def get_email_by_user_id(self, user_id):
        url = "https://ariza.{0}.globality.io/api/v1/user/{1}".format(self.env, user_id)
        return self.get_response(url)["email"]

    def get_matching_provider_ids(self):
        url = "https://juvenal.{0}.globality.io/api/v2/project/{1}/workspace".format(self.env, self.projec_id)
        res = self.get_response(url)
        matching_provider_ids = []
        for ws in res["items"]:
            if ws["workspaceType"] == "MATCHING":
                matching_provider_ids.append(ws["serviceProviderId"])
        return matching_provider_ids

    def get_company_name_by_id(self, company_id):
        url = "https://juvenal.{0}.globality.io/api/v2/company/{1}".format(self.env, company_id)
        return self.get_response(url)["name"]
    
    def get_emails_by_company_id(self, company_id):
        url = "https://ariza.{0}.globality.io/api/v1/user?company_id={1}".format(self.env, company_id)
        res = self.get_response(url)
        emails = []
        for item in res["items"]:
            emails.append(item["email"])
        return emails


if __name__ == "__main__":
    main()
