# setup.py
from setuptools import setup, find_packages

setup(
    name="modis",                          # package name used by pip and #egg=
    version="0.1.0",
    description="Code snippets from MODIS Global Flood Database (https://github.com/cloudtostreet/MODIS_GlobalFloodDatabase) explained in Tellman et al, Satellite imaging reveals increased proportion of population exposed to floods; Nature; https://doi.org/10.1038/s41586-021-03695-w. The fork consider following changes (i) keeping only code relevant to code detection, (ii) converting code to Python 3 (from Python 2) and (iii) correcting references to satellite repositories. Please quote the reference paper when using. ",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    python_requires=">=3.11.4",
    install_requires=[
        # 'ee' on import corresponds to the earthengine-api package on PyPI
        "earthengine-api==1.7.17",
        # note: 'math' is a builtin module and must NOT be listed here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author="cloudtostreet",
    url="https://github.com/MathildeBossut/MODIS_GlobalFloodDatabase",
    license="MIT",
)