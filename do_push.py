import subprocess

cwd = r"c:\Users\vikas\Downloads\ThermaScan"
print("Running force push...")
res = subprocess.run(["git", "push", "-f", "origin", "main"], cwd=cwd, capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
print("RETURNCODE:", res.returncode)
