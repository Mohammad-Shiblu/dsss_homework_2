from distutils.core import setup
from setuptools import find_packages

setup(
    name="math_quiz",
    version="0.1",
    author="Shiblu",
    author_email="mohammad.shiblu@fau.de",
    packages=find_packages(),
    install_requires=["numpy"],
)
