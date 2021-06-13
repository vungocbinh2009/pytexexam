from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pytexexam',
    version='2.1.0',
    packages=['pytexexam'],
    include_package_data=True,
    url='https://github.com/vungocbinh2009/pytexexam',
    license='Apache License, Version 2.0',
    author='binh',
    author_email='vungocbinh@protonmail.com',
    description='A simple library to create latex exam in python ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['jinja2'],
)
