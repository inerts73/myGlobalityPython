import sys
from os.path import basename
from verify_provider_lib import Test


def main(env, provider_id, qna_session_id):
    goal = "http://graph.globality.io/platform/providerHome/industryExperience"
    relation_type = "OPERATES_IN_INDUSTRY"

    test = Test(env, provider_id, qna_session_id, goal, relation_type)
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

    test.compare_all_obj_values(sorted_frigg_obj_values,
                                sorted_miranda_obj_values, sorted_sphinx_data)




if __name__ == "__main__":
    usage = "python3 {} <env> <provider_id> <qna_session_id>".format(
        basename(__file__))
    example = ("python3 {} demo 1d6ffd9a-8bfb-4867-82bd-3bcf579610f4 "
               "3b9b0224-4c73-4206-915f-4c2fa5d6b2ea").format(
        basename(__file__))

    if len(sys.argv) == 4:
        main(env=sys.argv[1], provider_id=sys.argv[2],
             qna_session_id=sys.argv[3])
    else:
        print("Usage: " + usage)
        print("Example: " + example)
        sys.exit(1)

