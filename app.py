import requests


def main():
    url = "https://api.github.com"

    response = requests.get(url)

    print("GitHub API Status:", response.status_code)

    if response.status_code == 200:
        print("Successfully connected to GitHub API!")
    else:
        print("Connection failed.")


if __name__ == "__main__":
    main()