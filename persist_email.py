import json
import requests

COMPANY_ID = "27d80a54-f0ab-4f19-8a69-9e2f37b06071"
ENV = "demo"
URL = "https://juvenal.{}.globality.io/api/v2/resource_tag".format(ENV)


def main():
    payload = {
        "resourceId": COMPANY_ID,
        "resourceType": "COMPANY",
        "resourceTagType": "PERSIST_EMAIL_CONTENT"
    }
    payload = json.dumps(payload)

    headers = {
        'Content-Type': "application/json",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "juvenal.{}.globality.io".format(ENV),
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "143",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url=URL, data=payload, headers=headers)
    res_dict = json.loads(response.text)
    print(json.dumps(res_dict, indent=2))


if __name__ == "__main__":
    main()