import subprocess

cmd = [r"C:\Program Files\Git\cmd\git.exe", "push", "origin", "main", "--force"]
print("Launching:", cmd)
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=r"c:\Users\vikas\Downloads\ThermaScan")
out, err = p.communicate(timeout=20)
print("OUT:", out)
print("ERR:", err)
print("EXIT CODE:", p.returncode)
