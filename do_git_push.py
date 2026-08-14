import subprocess, os

cwd = r"c:\Users\vikas\Downloads\ThermaScan"
res = subprocess.run(["git", "push", "-f", "origin", "main"], cwd=cwd, capture_output=True, text=True)

log = f"RETURNCODE: {res.returncode}\nSTDOUT:\n{res.stdout}\nSTDERR:\n{res.stderr}\n"
with open(os.path.join(cwd, "push_log.txt"), "w") as f:
    f.write(log)
print(log)
