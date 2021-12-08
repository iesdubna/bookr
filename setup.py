import setuptools
from setuptools import find_packages


setuptools.setup(
    name="bookr",
    version="0.0.1",
    packages=find_packages(),
    description="Bookr",
    author="Dubna IES",
    classifiers=["Intended Audience :: Information Technology",
                 "Operating System :: POSIX :: Linux",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3",
                 ],
    entry_points={
        "console_scripts": [
            "bookr = bookr.main:cli",
        ]
    },
)