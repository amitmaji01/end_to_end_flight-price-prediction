import setuptools
#reading my readme file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

#initial project version
__version__ = "0.0.0"

#this are the author and repository detail
REPO_NAME = "end_to_end_flight-price-prediction"
AUTHOR_USER_NAME = "AmitMaji"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "amitmaji810156@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)