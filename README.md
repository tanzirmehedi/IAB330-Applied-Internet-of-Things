# IAB330 Applied Internet of Things

Environment Setup: 

Installing Python, PIP, and Jupyter Notebook on Ubuntu 24.04: 

# Installing Python

Step 1: Install Python 3
~~~
sudo apt update
sudo apt install python3
python3 --version
~~~

# Installing PIP

Step 1: Install pip

~~~
sudo apt install python3-pip
pip --version
~~~

Upgrade pip (Optional)

~~~
pip3 install --upgrade pip
~~~

# Installing Jupyter Notebook

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




# Some Solution, If You are Facing Python3-xyz Type Error 


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


