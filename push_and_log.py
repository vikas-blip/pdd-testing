import subprocess, os

cwd = r"c:\Users\vikas\Downloads\ThermaScan"
p = subprocess.run(["git", "push", "origin", "main", "--force"], cwd=cwd, capture_output=True, text=True, timeout=30)
with open(os.path.join(cwd, "git_result.txt"), "w") as f:
    f.write(f"CODE: {p.returncode}\nOUT: {p.stdout}\nERR: {p.stderr}\n")
print(p.stdout)
print(p.stderr)
