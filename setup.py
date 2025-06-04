from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="AniStack",
    version="0.1",
    author="Deep",
    packages=find_packages(),
    install_requires=requirements,
)