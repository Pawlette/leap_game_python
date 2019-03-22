import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="leap_game-pawlette",
    version="0.0.1",
    author="Paulette ZorBa",
    author_email="paulette.bautista@thoughtworks.com",
    description="A simple prototype for Leap Motion with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pawlette",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
