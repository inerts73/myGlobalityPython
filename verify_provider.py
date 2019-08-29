import sys
import verify_provider_industry_experience


def main():
    verify_provider_industry_experience.main(
        env=sys.argv[1], provider_id=sys.argv[2],
        qna_session_id=sys.argv[3])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("error => " + str(e))