# setup.py - Package Configuration for Vehicle Insurance ML Ops Project
# This file is used to configure the Python package for distribution and installation.
# It defines metadata about the package and specifies which modules to include.

from setuptools import setup, find_packages

# Define the package setup configuration
setup(
    # Package name (should match the project directory name)
    name = "src",
    # Version number for the package
    version = "0.0.1",
    # Author's name
    author = "ShalinVachheta017",
    # Author's email address
    author_email = "shalinvachheta2016@hotmail.com",
    # Automatically find and include all Python packages in the project
    packages = find_packages(),
)