import requests


def main():
    url = "https://api.github.com/repos/chidomi/cloudops-automation"

    response = requests.get(url)

    print("GitHub API Status:", response.status_code)

    if response.status_code == 200:
        repository = response.json()

        print("\nRepository Information")
        print("----------------------")
        print("Name:", repository["name"])
        print("Description:", repository["description"])
        print("Stars:", repository["stargazers_count"])
        print("Forks:", repository["forks_count"])
        print("Language:", repository["language"])

    else:
        print("Unable to retrieve repository information.")


if __name__ == "__main__":
    main()