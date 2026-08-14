import subprocess, os

env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"
env["GCM_INTERACTIVE"] = "never"

cwd = r"c:\Users\vikas\Downloads\ThermaScan"
p = subprocess.run(["git", "push", "origin", "main", "--force"], cwd=cwd, env=env, capture_output=True, text=True)

with open(os.path.join(cwd, "git_result.txt"), "w") as f:
    f.write(f"CODE: {p.returncode}\nOUT: {p.stdout}\nERR: {p.stderr}\n")

print("RETURN CODE:", p.returncode)
print("STDOUT:", p.stdout)
print("STDERR:", p.stderr)
