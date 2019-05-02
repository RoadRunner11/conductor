import os

from setuptools import find_packages, setup

setup(
    name="conductor",
    version=os.environ["CICLE_BUILD_NUM"],
    packages=find_packages(exclude=["settings"]),
    include_package_data=True,
)
