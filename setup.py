import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fp:
    long_description = fp.read()

about = {}
with open(os.path.join(here, "oshash", "__version__.py"), "r") as f:
    exec(f.read(), about)

setuptools.setup(
    name="oshash",
    version=about["__version__"],
    author=about["__author__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    license=about["__license__"],
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["oshash = oshash.command:main"]},
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ]
)
