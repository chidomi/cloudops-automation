import requests
from datetime import datetime


def main():
    repo_url = "https://api.github.com/repos/chidomi/cloudops-automation"
    commits_url = "https://api.github.com/repos/chidomi/cloudops-automation/commits"

    repo_response = requests.get(repo_url)
    commits_response = requests.get(commits_url, params={"per_page": 5})

    print("GitHub API Status:", commits_response.status_code)

    if repo_response.status_code == 200 and commits_response.status_code == 200:
        repository = repo_response.json()
        commits = commits_response.json()

        report = []
        report.append("CLOUDOPS AUTOMATION")
        report.append(f"Generated: {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z')}")
        report.append("")
        report.append("REPOSITORY SUMMARY")
        report.append("------------------")
        report.append(f"Repository: {repository['name']}")
        report.append(f"Description: {repository['description']}")
        report.append(f"Commits Retrieved: {len(commits)}")
        report.append("")
        report.append("LATEST REPOSITORY COMMITS")
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
        print("Unable to retrieve repository information or commits.")


if __name__ == "__main__":
    main()