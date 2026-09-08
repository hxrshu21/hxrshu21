import os
import re
import requests

USERNAME = "hxrshu21"
TOKEN = os.environ["GH_TOKEN"]
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

def get_user_data():
    r = requests.get(f"https://api.github.com/users/{USERNAME}", headers=HEADERS)
    r.raise_for_status()
    return r.json()

def get_total_stars():
    stars = 0
    page = 1
    while True:
        r = requests.get(
            f"https://api.github.com/users/{USERNAME}/repos",
            headers=HEADERS,
            params={"per_page": 100, "page": page},
        )
        r.raise_for_status()
        repos = r.json()
        if not repos:
            break
        stars += sum(repo["stargazers_count"] for repo in repos)
        page += 1
    return stars

def get_year_commits():
    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          totalCommitContributions
          restrictedContributionsCount
        }
      }
    }
    """
    r = requests.post(
        "https://api.github.com/graphql",
        headers=HEADERS,
        json={"query": query, "variables": {"login": USERNAME}},
    )
    r.raise_for_status()
    data = r.json()["data"]["user"]["contributionsCollection"]
    return data["totalCommitContributions"] + data["restrictedContributionsCount"]

def main():
    user = get_user_data()
    repos = user["public_repos"]
    followers = user["followers"]
    stars = get_total_stars()
    commits = get_year_commits()

    row = f"|  **{repos}**  |  **{stars}**  |  **{followers}**  |  **{commits}**  |"

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r"(<!--START_SECTION:github-stats-->\s*\|.*?\|\s*\n\|.*?\|\s*\n).*?(\n<!--END_SECTION:github-stats-->)",
        lambda m: m.group(1) + row + m.group(2),
        content,
        flags=re.DOTALL,
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    main()
