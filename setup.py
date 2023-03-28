import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1" # update as per your need

REPO_NAME = "ML_project"
AUTHOR_USER_NAME = "demohari"
SRC_REPO = "census-income"
AUTHOR_EMAIL = "kishore_koneru@yahoo.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "census-income"},
    packages=setuptools.find_packages(where="census-income")
)