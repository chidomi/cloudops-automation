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

        report = []

        report.append("CLOUDOPS AUTOMATION")
        report.append("Latest Repository Commits")
        report.append("-------------------------")

        for commit in commits:
            message = commit["commit"]["message"]
            author = commit["commit"]["author"]["name"]
            sha = commit["sha"][:7]

            report.append(f"\nCommit: {sha}")
            report.append(f"Author: {author}")
            report.append(f"Message: {message}")

        report_text = "\n".join(report)

        print(report_text)

        with open("commit_report.txt", "w") as file:
            file.write(report_text)

        print("\nReport successfully generated!")

    else:
        print("Unable to retrieve commits.")


if __name__ == "__main__":
    main()