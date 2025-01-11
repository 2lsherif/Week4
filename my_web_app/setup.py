# setup.py
from setuptools import setup, find_packages

setup(
    name="my_web_app",  # Name of your package
    version="0.1",      # Version of your package
    packages=find_packages(),  # Automatically finds all packages under your project
    install_requires=["flask"],  # Dependencies
)
