from setuptools import setup, find_packages

setup(
    name="svilniper",
    version="1.2.0",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "svilniper = svilniper.cli:main",
        ],
    },
    author="Svilniper Team",
    description="Modern Black & Orange Recon Tool",
    python_requires=">=3.8",
)