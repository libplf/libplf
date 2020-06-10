import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libplf",
    version="0.0.4",
    author="vang1ong7ang",
    author_email="vang1ong7ang@outlook.com",
    description="library for multidimensional piecewise linear function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/libplf/libplf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
