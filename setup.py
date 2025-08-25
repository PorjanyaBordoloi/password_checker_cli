from setuptools import setup, find_packages

setup(
    name="pwd_checker",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pwd_checker = pwd_checker.cli:main",
        ],
    },
    install_requires=[],
    python_requires=">=3.6",
    description="Password Strength Checker CLI Tool",
    author="Paul Bordoloi",
    url="https://github.com/PorjanyaBordoloi/password_checker_cli.git",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
