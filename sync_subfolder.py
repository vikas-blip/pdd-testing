import os
import shutil

src_wf = r"c:\Users\vikas\Downloads\ThermaScan\.github"
dst_wf = r"c:\Users\vikas\Downloads\ThermaScan\pdd-testing\.github"

if os.path.exists(dst_wf):
    shutil.rmtree(dst_wf, ignore_errors=True)

shutil.copytree(src_wf, dst_wf)
print("Synchronized .github/ workflows to pdd-testing subfolder.")
