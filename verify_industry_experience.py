import json
from requests import get

ENV = "demo"
PROVIDER_ID = "1d6ffd9a-8bfb-4867-82bd-3bcf579610f4"
QNA_SESSION = "3b9b0224-4c73-4206-915f-4c2fa5d6b2ea"
GOAL = "http://graph.globality.io/platform/providerHome/industryExperience"
RELATION_TYPE = "OPERATES_IN_INDUSTRY"


def main():
    test = Test(ENV, PROVIDER_ID, QNA_SESSION, GOAL, RELATION_TYPE)
    frigg_data = test.get_frigg_data()
    print("********** frigg **********")
    sorted_frigg_obj_values = test.get_frigg_obj_values(frigg_data)
    print()

    miranda_data = test.get_miranda_data()
    print("********** miranda **********")
    sorted_miranda_obj_values = test.get_miranda_obj_values(miranda_data)
    print()

    sphinx_data = test.get_sphinx_data()
    print("********** sphinx **********")
    sorted_sphinx_data = test.get_sphinx_obj_values(sphinx_data)
    print()

    test.compare_all_obj_values(sorted_frigg_obj_values, sorted_miranda_obj_values, sorted_sphinx_data)

def output(data):
    print(json.dumps(data, indent=2))


class Test(object):
    def __init__(self, env, provider_id, qna_session, goal, relation_type):
        self.env = env
        self.provider_id = provider_id
        self.qna_session = qna_session
        self.goal = goal
        self.relation_type = relation_type

    def get_response(self, url):
        max_attempts = 5
        for attempt in range(max_attempts):
            res = json.loads(get(url, verify=False).text)
            if ("_links" in res) and ("self" in res["_links"]):
                return res

        raise Exception("Getting response from '{0}' failed after {1} attempts".format(url, max_attempts))

    def get_frigg_data(self):
        url = "https://frigg.{0}.globality.io/api/v2/provider/{1}".format(self.env, self.provider_id)
        return self.get_response(url)

    def get_frigg_obj_values(self, frigg_data):
        frigg_obj_values = []
        for x in frigg_data["serviceProviderAssertion"]:
            if ((x["sourceType"] == "QNA_SESSION") and (x["relationType"] == self.relation_type)):
                frigg_obj_values.append(x["objectValue"])
        output(sorted(frigg_obj_values))
        return sorted(frigg_obj_values)

    def get_miranda_data(self):
        url = "https://miranda.{0}.globality.io/api/v1/service_provider/{1}/assertion?limit=1000"   .format(self.env, self.provider_id)
        return self.get_response(url)

    def get_miranda_obj_values(self, miranda_data):
        miranda_obj_values = []
        for x in miranda_data["items"]:
            if ((x["sourceType"] == "QNA_SESSION") and (x["relationType"] == self.relation_type)):
                miranda_obj_values.append(x["objectValue"])
        output(sorted(miranda_obj_values))
        return sorted(miranda_obj_values)

    def get_sphinx_data(self):
        url = "https://sphinx.{0}.globality.io/api/v1/fact_event?limit=1000&goal={1}&session_id={2}".format(self.env, self.goal, self.qna_session)
        return self.get_response(url)

    def get_sphinx_obj_values(self, sphinx_data):
        sphinx_obj_values = []
        for x in sphinx_data["items"][0]["values"]:
            sphinx_obj_values.append(x["value"])
        output(sorted(sphinx_obj_values))
        return sorted(sphinx_obj_values)

    def compare_all_obj_values(self, frigg_obj_values, miranda_obj_values, sphinx_obj_values):
        if (frigg_obj_values == miranda_obj_values) and (miranda_obj_values == sphinx_obj_values):
            print("Test Results => PASS")
        else:
            print("Test Results => FAIL")


if __name__ == "__main__":
    main()
