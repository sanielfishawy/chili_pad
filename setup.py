#pylint: disable=invalid-name
import platform
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requirements = []
dependency_links = []
if platform.system is 'raspberry':
    install_requirements.append('RPi.gpio')
else:
    dependency_links.append('git+https://github.com/sanielfishawy/rpi_gpio_stub#egg=rpi')

print(dependency_links)

setuptools.setup(
    name="chili_pad",
    version="0.0.1",
    author="Sani Elfishawy",
    author_email="elfishawy.sani@gmail.com",
    description="A driver for the chili_pad modified by sani replacing the controller and powersupply.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sanielfishawy/chili_pad",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    install_requires=install_requirements,
    dependency_links=dependency_links,
)
