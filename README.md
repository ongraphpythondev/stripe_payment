# Stripe Payment Gateway

The Stripe Python library provides convenient access to the Stripe API from applications written in the Python language. It includes a pre-defined set of classes for API resources that initialize themselves dynamically from API responses which makes it compatible with a wide range of versions of the Stripe API.

## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.5+
* Virtual Environment

To install virtual environment on your system use:

```bash
pip install virtualenv

or

pip3 install virtualenv #if using linux(for python 3 and above)
```

## Installation and Running :

```bash
git clone https://github.com/ongraphpythondev/stripe_payment.git

cd stripe_payment

virtualenv venv 
      or 
virtualenv venv -p python3 #if using linux(for python 3 and above)

venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# install required packages for the project to run
pip install -r requirements.txt

python manage.py runserver
```
