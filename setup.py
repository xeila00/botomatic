import os
from setup import setup
from botomatic.botomatic import os
from setup import os
from botomatic.botomatic import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "botomatic",
    version = "0.0.1",
    author = "Hilary Mason",
    author_email = "me@hilarymason.com",
    description = ("A module to make it trivial to create new twitter bots"),
    license = "BSD",
    keywords = "twitter bots",
    url = "https://github.com/hmason/botomatic",
    packages=['botomatic'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
