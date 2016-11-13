# import the setup function, which does all the work of installing the code
from distutils.core import setup

# tell setup about the code to install
setup(
    # name of project, can be any string but simplest to keep it same as project name
    name='palindrome',
    # can be any string, python doesn't rely on it to follow any rules
    version='1.0.0',
    # specify python modules to be installed as a list, don't specify .py extension
    py_modules=['palindrome'],

    # metadata
    author='John Doe',
    author_email='john.doe@whatever.com',
    description='A module for finfding palindromic numbers.',
    license='Public domain',
    keywords='example'
)
