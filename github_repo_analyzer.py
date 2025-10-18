import requests

def analyze_repo(repo_url):
    # Extract owner and repo name from URL
    parts = repo_url.rstrip('/').split('/')
    owner = parts[-2]
    repo = parts[-1]

    # GitHub API URL
    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    # Fetch repo info
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        print("Repository Name:", data['name'])
        print("Description:", data['description'])
        print("Stars:", data['stargazers_count'])
        print("Forks:", data['forks_count'])
        print("Open Issues:", data['open_issues_count'])
        print("Primary Language:", data['language'])
    else:
        print("Failed to fetch repo data")

# Example usage
if __name__ == "__main__":
    analyze_repo("https://github.com/DaveKavya/gradient-python")
