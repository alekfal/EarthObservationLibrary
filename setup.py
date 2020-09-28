import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name = "earthobspy",
    version = "0.0.6",
    author = "Falagas Alekos",
    author_email = "alek.falagas@gmail.com",
    description = "Collection of functions for raster manipulation based on rasterio",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/alekfal/EarthObservationLibrary",
    packages = setuptools.find_packages(),
    license="GNU General Public License v3 or later (GPLv3+)",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
    install_requires=required,
)