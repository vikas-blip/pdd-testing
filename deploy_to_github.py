import subprocess, os

def run(cmd, cwd):
    print(f"Running: {cmd} in {cwd}")
    res = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    print("RETURN CODE:", res.returncode)
    return res.returncode

root = r"c:\Users\vikas\Downloads\ThermaScan"
pdd = r"c:\Users\vikas\Downloads\ThermaScan\pdd-testing"

# Push root
code1 = run("git push origin main --force", root)
# Push pdd-testing
code2 = run("git push origin main --force", pdd)

if code1 == 0 or code2 == 0:
    print("SUCCESSFULLY PUSHED TO GITHUB!")
else:
    print("PUSH FAILED WITH CODES:", code1, code2)
