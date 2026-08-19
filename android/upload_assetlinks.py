import subprocess
import os

cwd = r"c:\Users\vikas\Downloads\ThermaScan"

print("Checking status...")
res = subprocess.run(["git", "status"], cwd=cwd, capture_output=True, text=True)
print(res.stdout)

print("Force adding .well-known/assetlinks.json and .nojekyll...")
subprocess.run(["git", "add", "-f", ".well-known/assetlinks.json"], cwd=cwd)
subprocess.run(["git", "add", "-f", ".nojekyll"], cwd=cwd)

print("Committing...")
res = subprocess.run(["git", "commit", "-m", "fix(twa): add .well-known/assetlinks.json and .nojekyll"], cwd=cwd, capture_output=True, text=True)
print(res.stdout)
print(res.stderr)

print("Pushing...")
res = subprocess.run(["git", "push", "-f", "origin", "main"], cwd=cwd, capture_output=True, text=True)
print(res.stdout)
print(res.stderr)
