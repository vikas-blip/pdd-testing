import subprocess
import os

cwd = r"c:\Users\vikas\Downloads\ThermaScan"

print(f"Directory: {cwd}")
print("Executing git push -f origin main...")
result = subprocess.run(["git", "push", "-f", "origin", "main"], cwd=cwd, capture_output=True, text=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("RETURNCODE:", result.returncode)
