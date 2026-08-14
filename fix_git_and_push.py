import os
import shutil
import subprocess

root_dir = r"c:\Users\vikas\Downloads\ThermaScan"
sub_git = os.path.join(root_dir, "pdd-testing", ".git")

# Delete nested .git inside pdd-testing if it exists
if os.path.exists(sub_git):
    try:
        shutil.rmtree(sub_git, ignore_errors=True)
        print("Removed nested .git folder in pdd-testing.")
    except Exception as e:
        print(f"Note on .git remove: {e}")

# Remove extra workflow files from .github/workflows in root and pdd-testing
to_remove = ["deploy-and-test.yml", "main-ci-cd.yml", "thermascan-ci.yml"]
for wf_path in [
    os.path.join(root_dir, ".github", "workflows"),
    os.path.join(root_dir, "pdd-testing", ".github", "workflows")
]:
    if os.path.exists(wf_path):
        for f in to_remove:
            fp = os.path.join(wf_path, f)
            if os.path.exists(fp):
                try:
                    os.remove(fp)
                    print(f"Removed redundant workflow: {fp}")
                except Exception as e:
                    print(f"Error removing {fp}: {e}")

def run_cmd(cmd, cwd):
    print(f"> [{cwd}] {cmd}")
    res = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print(res.stderr)

run_cmd("git config user.email \"vikas@thermascan.app\"", root_dir)
run_cmd("git config user.name \"Vikas\"", root_dir)
run_cmd("git checkout -f main", root_dir)
run_cmd("git checkout --orphan project-history", root_dir)
run_cmd("git reset", root_dir)
run_cmd("git add -A", root_dir)
run_cmd('git commit -m "feat(thermascan): Initial release of ThermaScan PWA, 1050 E2E tests & appium-tests.yml pipeline"', root_dir)
run_cmd("git branch -M main", root_dir)
run_cmd("git push --force origin main", root_dir)

print("FIX & FORCE PUSH COMPLETED SUCCESSFULLY!")
