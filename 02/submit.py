"""
curl 'https://code-two.replit.app/api/challenge/submit' \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'Cookie: connect.sid=s%3AYKDcyaksSHOxvIiiFBsjB.mfZAacFprreQ2nooxaMUmVm1XkyGFqoFugwDEhrGMOc' \
  --data-raw '{"code": "undergroundnet.ru"}'
"""

import requests


def main():
    guesses = ["testtt", "abcdef"]

    for guess in guesses:
        cookies = {
            "connect.sid": "s%3AYKDcyaksSHOxvIiiFBsjB.mfZAacFprreQ2nooxaMUmVm1XkyGFqoFugwDEhrGMOc",
        }

        req = requests.post(
            "https://code-two.replit.app/api/challenge/submit",
            cookies=cookies,
            data={"code": guess},
        )

        print(f"{guess=}\n{req.text}")

        if req.status_code != 400:
            print("Holy crap, success?")
            break


if __name__ == "__main__":
    main()
