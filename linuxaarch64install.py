import os

def install_function():
    os.system('wget https://nvidia.box.com/shared/static/yr6sjswn25z7oankw8zy1roow9cy5ur1.whl -O torch-1.6.0rc2-cp36-cp36m-linux_aarch64.whl')
    os.system('sudo apt-get install python3-pip libopenblas-base libopenmpi-dev')
    os.system('sudo pip3 install Cython')
    os.system('sudo pip3 install torch-1.6.0rc2-cp36-cp36m-linux_aarch64.whl')
    os.system('sudo apt-get install libjpeg-dev zlib1g-dev')
    os.system('git clone --branch v0.6.0 https://github.com/pytorch/vision torchvision')
    os.system('cd ~/torchvision')  
    os.system('sudo python3 setup.py install')
    os.system('cd ~/')
    os.system('')
    os.system('')

install_function()
