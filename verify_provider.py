import sys
import verify_provider_industry_experience


def main():
    try:
        verify_provider_industry_experience.main(
            env=sys.argv[1], provider_id=sys.argv[2],
            qna_session_id=sys.argv[3])
    except Exception as e:
        print("error => " + str(e))


if __name__ == "__main__":
    main()
