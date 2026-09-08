<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:9D50BB,100:6E48AA&height=220&section=header&text=Harsh%20Sakharkar&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Programmer%20•%20Python%20•%20C⨨⨨%20•%20Open%20Source&descAlignY=58&descSize=18" width="100%"/>

<a href="https://github.com/hxrshu21">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=800&color=B983FF&center=true&vCenter=true&width=600&lines=Welcome+to+my+corner+of+GitHub+%E2%9C%A8;I+turn+%E2%98%95+into+code;Currently+exploring+Content+Creation;Python+%7C+C%2B%2B+%7C+Open+Source+enthusiast" alt="Typing SVG" />
</a>

<img src="https://komarev.com/ghpvc/?username=hxrshu21&label=Profile%20Views&color=9D50BB&style=for-the-badge" alt="profile views"/>
<img src="https://img.shields.io/github/followers/hxrshu21?label=Followers&style=for-the-badge&color=B983FF" alt="followers"/>

<br/><br/>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="500">

</div>

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E48AA,100:FF6AC1&height=3&section=header"/>
</div>

<br/>

## ⋆｡°✩ About Me ✩°｡⋆

- 🌱 Currently learning **Content Creation**
- 👨‍💻 All my projects live at **[github.com/hxrshu21](https://github.com/hxrshu21)**
- 💬 Ask me about **Python • C++ • Coding • Open Source • Tech**
- 📫 Reach me at **harshsakharkar455@gmail.com**
- ⚡ Fun fact: **I turn ☕ into code**

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:FF6AC1,100:6E48AA&height=3&section=header"/>
</div>

<br/>

## ⋆｡°✩ Tech Stack ✩°｡⋆

<div align="center">

<img src="https://skillicons.dev/icons?i=py,cpp,java,js,html,css,react,reactnative,nodejs,git,graphql,linux,arduino,jenkins,ps,ai&theme=dark" />

</div>

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E48AA,100:FF6AC1&height=3&section=header"/>
</div>

<br/>

## ⋆｡°✩ GitHub Analytics ✩°｡⋆

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

## ⋆｡°✩ Contribution Snake ✩°｡⋆

<div align="center">

<img src="https://raw.githubusercontent.com/hxrshu21/hxrshu21/output/github-contribution-grid-snake.svg" alt="snake animation"/>

<sub>🐍 Yeh animated snake tumhare contribution graph ko khaata hua dikhega — setup ke liye neeche "Snake ko activate karna" section dekho.</sub>

</div>

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6E48AA,100:FF6AC1&height=3&section=header"/>
</div>

<br/>

## ⋆｡°✩ Connect With Me ✩°｡⋆

<div align="center">

<a href="https://fb.com/hyy.hxrsh" target="_blank">
  <img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white"/>
</a>
<a href="https://instagram.com/hxrshu21" target="_blank">
  <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/>
</a>
<a href="mailto:harshsakharkar455@gmail.com" target="_blank">
  <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>

<br/><br/>

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="300">

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6E48AA,100:9D50BB&height=120&section=footer&animation=twinkling" width="100%"/>

<br/>
