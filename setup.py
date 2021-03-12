import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="print2d",
    version="0.1.1",
    author="Jino Park",
    author_email="pjessesco@gmail.com",
    description="print2d : Replacement of `print()` for printing 2d array with readability.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pjessesco/print2d",
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)