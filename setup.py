import os
from setuptools import setup, find_packages


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def setup_package():
    setup(
        name = "My App",
        version = "0.1.0",
        author = "<author>",
        author_email = "<email>",
        description = ("My App - Python Boilerplate"),
        license = "MIT",
        keywords = "",
        url = "http://github.com/kishstats/myapp",
        install_requires = [],
        long_description=read('README.md'),
        classifiers=[
            "Development Status :: 4 - Beta",
            "Topic :: Utilities",
            "License :: OSI Approved :: MIT License",
        ],
        packages=find_packages(exclude=('tests', 'docs')),
    )


if __name__ == "__main__":
    setup_package()