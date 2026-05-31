import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary
response_dict = r.json()

# print(response_dict.keys())
print(f"Total Repositories: {response_dict.get("total_count", 0)}")
print(f"Complete Results: {not response_dict.get("incomplete_results", False)}")

# Explore information about the repositories
repo_dicts = response_dict.get("items", {})
print(f"Repositories Returned: {len(repo_dicts)}")

# # Examine the first repository
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nSelected Information about Each Repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict.get("name", None)}")
    print(f"Owner: {repo_dict.get("owner", None).get("login", None)}")
    print(f"Stars: {repo_dict.get("stargazers_count", 0)}")
    print(f"Repository: {repo_dict.get("html_url", None)}")
    print(f"Description: {repo_dict.get("description", None)}")
