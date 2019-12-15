#pylint: disable=invalid-name
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chili-pad",
    version="0.0.1",
    author="Sani Elfishawy",
    author_email="elfishawy.sani@gmail.com",
    description="A driver for the chili-pad modified by sani replacing the controller and powersupply.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sanielfishawy/chili-pad",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)