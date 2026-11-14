import requests


def main():
    url = "https://api.github.com/repos/chidomi/cloudops-automation/commits"

    params = {
        "per_page": 5
    }

    response = requests.get(url, params=params)

    print("GitHub API Status:", response.status_code)

    if response.status_code == 200:
        commits = response.json()

        print("\nLatest Repository Commits")
        print("-------------------------")

        for commit in commits:
            message = commit["commit"]["message"]
            author = commit["commit"]["author"]["name"]
            sha = commit["sha"][:7]

            print("\nCommit:", sha)
            print("Author:", author)
            print("Message:", message)

    else:
        print("Unable to retrieve commits.")


if __name__ == "__main__":
    main()