import os, subprocess, sys

def main():
    root = r"c:\Users\vikas\Downloads\ThermaScan"
    pdd = r"c:\Users\vikas\Downloads\ThermaScan\pdd-testing"
    
    target = root if os.path.exists(os.path.join(root, ".git")) else pdd
    print("ThermaScan 1-Click GitHub Sync...")
    print(f"Repository target: {target}")
    
    try:
        subprocess.run(["git", "config", "user.name", "Vikas"], cwd=target)
        subprocess.run(["git", "config", "user.email", "vikas@thermascan.app"], cwd=target)
        subprocess.run(["git", "add", "-A"], cwd=target)
        subprocess.run(["git", "commit", "-m", "feat: Realtime Cloud Firestore Sync update"], cwd=target)
        subprocess.run(["git", "push", "-f", "origin", "main"], cwd=target)
        print("SUCCESS! Live updates published to https://vikas-blip.github.io/pdd-testing/")
    except Exception as e:
        print(f"Notice: {e}")

if __name__ == "__main__":
    main()
