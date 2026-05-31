import requests
import plotly.express as px

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process overall results
response_dict = r.json()
print(f"Complete results: {not response_dict.get("Incomplete Results", False)}")

# Process repositiory information
repo_dicts = response_dict.get("items", {})

repo_names = [repo_dict.get("name", None) for repo_dict in repo_dicts]
stars = [repo_dict.get("stargazers_count", 0) for repo_dict in repo_dicts]
repo_urls = [repo_dict.get("html_url", None) for repo_dict in repo_dicts]
repo_links = [
    f"<a href='{repo_urls[i]}'>{repo_names[i]}</a>" for i in range(len(repo_dicts))
]

owners = [repo_dict.get("owner", None).get("login") for repo_dict in repo_dicts]
descriptions = [repo_dict.get("description", None) for repo_dict in repo_dicts]
hover_texts = [f"{owners[i]}<br />{descriptions[i]}" for i in range(len(repo_dicts))]

# Make visualization
title = "Most-Starred Python Projects on Github"
labels = {"x": "Repo", "y": "Stars"}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
)

fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)

fig.show()
