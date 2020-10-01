import sys
import subprocess
from subprocess import STDOUT, check_call
import os


check_call(['sudo apt-get', 'install', '-y', 'python3-pip libopenmpi-dev libopenblas-base'],
     stdout=open(os.devnull,'wb'), stderr=STDOUT)
        
subprocess.check_call([sys.executable, '-m', 'pip3', 'install',
'Cython==0.29.21'])

subprocess.check_call([sys.executable, '-m', 'pip3', 'install',
'torch===1.6.0 torchvision===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html'])
     
check_call(['apt-get', 'install', '-y', 'python3-pip'],
     stdout=open(os.devnull,'wb'), stderr=STDOUT)

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip3', 'install',
'<packagename>'])

# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip',
'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print(installed_packages)
