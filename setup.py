from setuptools import setup
from setuptools import find_packages

setup(
    name="libplf",
    version="0.0.4",
    author="vang1ong7ang",
    author_email="vang1ong7ang@outlook.com",
    description="library for multidimensional piecewise linear function",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/libplf/libplf",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
