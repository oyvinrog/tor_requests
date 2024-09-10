from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tor_requests",
    version="0.1.0",
    author="sflkjdfskjl@sfpoksfpo",
    author_email="sflkjdfskjl@sfpoksfpo",
    description="A TOR requests wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oyvinrog/tor_requests",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",
        "ipwhois",
        "colorama",
        "pysocks",
    ],
)