from setuptools import setup, find_packages

def read(filename):
    return [requirement.strip() for requirement in open(filename).readlines()]

setup(
    name="school-system",
    version="0.1.0", # major, minor, patch
    description="a school system API",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")}
    )