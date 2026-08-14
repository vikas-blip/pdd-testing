import os

dirs = [
    r"c:\Users\vikas\Downloads\ThermaScan\.github\workflows",
    r"c:\Users\vikas\Downloads\ThermaScan\pdd-testing\.github\workflows"
]

to_delete = ["deploy-and-test.yml", "main-ci-cd.yml", "thermascan-ci.yml"]

for d in dirs:
    if os.path.exists(d):
        for f in to_delete:
            target = os.path.join(d, f)
            if os.path.exists(target):
                os.remove(target)
                print(f"Removed redundant workflow: {target}")

print("Cleaned up workflows successfully. Only appium-tests.yml remains.")
