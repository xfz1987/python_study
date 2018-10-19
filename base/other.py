# subprocess执行shell脚本
import subprocess
output = subprocess.check_out('dir', shell=Tr)
print(output)
# 优于subprocess
import os
os.system('dir')