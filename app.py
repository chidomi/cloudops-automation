
import requests


def main():
    username = "chidomi"

    url = f"https://api.github.com/users/{username}/repos"

    params = {
        "per_page": 100,
        "sort": "updated"
    }

    response = requests.get(url, params=params)

    print("GitHub API Status:", response.status_code)

    if response.status_code == 200:
        repositories = response.json()

        print(f"\nRepositories belonging to {username}")
        print("--------------------------------------")

        for repo in repositories:
            print("\nRepository:", repo["name"])
            print("Description:", repo["description"])
            print("Language:", repo["language"])
            print("Stars:", repo["stargazers_count"])
            print("Last Updated:", repo["updated_at"])

        print(f"\nTotal repositories retrieved: {len(repositories)}")

    else:
        print("Unable to retrieve repositories.")
        print("Response:", response.text)


if __name__ == "__main__":
    main()
