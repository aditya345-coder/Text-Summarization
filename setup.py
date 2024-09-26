import setuptools

with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()
    

__version__ = "0.0.0"

REPO_NAME="Text-Summarization"
AUTHOR_USER_NAME="aditya345-coder"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="neuralninja01@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarization app in python using nlp.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https:/github/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https:/github/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
)