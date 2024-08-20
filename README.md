# IAB330 Applied Internet of Things

Unit Coordinator: A/Prof Sara Khalifa (sara.khalifa@qut.edu.au)

Tutor: Mr. Tao Liu (t24.liu@hdr.qut.edu.au)

Tutor: Mr. Sk Tanzir Mehedi (s.tanzir@qut.edu.au)


# Environment Setup for Ubuntu

Installing Python, PIP, and Jupyter Notebook on Ubuntu 24.04

## Installing Python

Step 1: Install Python 3
~~~
sudo apt update
sudo apt install python3
python3 --version
~~~

## Installing PIP

Step 1: Install pip

~~~
sudo apt install python3-pip
pip --version
~~~

Upgrade pip (Optional)

~~~
pip3 install --upgrade pip
~~~

## Installing Jupyter Notebook

Step 1: Install Jupyter Notebook

~~~
pip3 install notebook
~~~

Step 2: Start and Access Jupyter Notebook

~~~
jupyter notebook
~~~

Jupyter Notebook will start, and your web browser will open displaying the Notebook dashboard. If it does not open automatically, open your web browser and type the following URL:

~~~
http://{your-ip}:8888/
~~~

Now, you should see the Jupyter Notebook interface, where you can create new notebooks, open existing notebooks, or manage your files.


## Some Solution, If You are Facing Python3-xyz Type Error 


1. Install the Python package using APT:
   
For instance, if you want to install the requests Python library, you can install it using APT instead, like this:

~~~
sudo apt install python3-requests
~~~

This will install this library system-wide.


2. Use pipx:
   
pipx lets you install and run Python applications in isolated environments. This is the recommended way to install PyPI packages that represent command-line applications.

To install pipx, run:

~~~
sudo apt install pipx
~~~
~~~
pipx ensurepath
~~~


3. In a terminal, delete this file with:

~~~
sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
~~~

and everything will be OK!



#####################################################################################

# Environment Setup for Windows

Installing Python, PIP, and Jupyter Notebook on Windows 11

## Install Python

Step 1. Download Python
   
Download Python: https://www.python.org/downloads

Step 2. Install Python

Run the downloaded installer.
Make sure to check the box that says Add Python to PATH before clicking the Install button.
Choose "Install Now" to proceed with the default settings.

Step 3. Verify Python Installation
   
Open Command Prompt and type-

~~~
python --version
~~~

You should see the version of Python you installed.


## Install PIP

PIP is included with Python 3.4 and later, so it should be installed automatically. To verify PIP installation, open Command Prompt and type:
~~~
pip --version
~~~

If it's not installed, you can download get-pip.py and install it manually:


## Install Jupyter Notebook

~~~
pip install jupyterlab
~~~
~~~
pip install jupyter notebook
~~~

Now, go to Desktop, Create a folder “Test Jupyter ” open that folder. Once CMD open, you just need to run command-
~~~
jupyter notebook or python -m notebook
~~~

## Troubleshooting:

Python not recognized: If Python isn't recognized, ensure it's added to your PATH. You can add it manually by going to System Properties -> Advanced -> Environment Variables, and adding the path to Python and Scripts to the PATH variable.

PIP not recognized: Similarly, ensure PIP is in your PATH.

Jupyter not launching: Ensure that Jupyter is installed correctly and that no firewall or antivirus is blocking it.

These steps should help you get Python, PIP, and Jupyter Notebook up and running on your Windows machine. If you encounter any specific issues or need further assistance, feel free to ask!


#####################################################################################

# Environment Setup for Mac OS

Link: https://www.dataquest.io/blog/installing-python-on-mac/ 


## Error: dpkg was interrupted, you must manually run 'sudo dpkg --configure -a' to correct the problem.

Run the Commands: 

~~~
sudo dpkg --configure -a
~~~

~~~
sudo apt-get update
sudo apt-get upgrade
~~~

~~~
sudo reboot
~~~

