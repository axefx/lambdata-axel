from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_axel",  # the name that you will install via pip
    version="1.2.1",
    author="Axel Corro",
    author_email="axacorro@gmail.com",
    description="Some data science tools",
    long_description=long_description,
    # required if using a md file for long desc
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/axefx/lambdata-axel",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
