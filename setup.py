from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name= "asuna_api",
    packages= ["asuna_api"],
    version= "0.3.1",
    license= "MIT",
    description= "An async python wrapper for the asuna api",
    long_description= long_description,
    long_description_content_type= "text/markdown",
    author= "JDJG3493",
    author_email= "jdjgbot@gmail.com",
    url= "https://github.com/Senarc-Studios/asuna_api",
    download_url= "https://github.com/Senarc-Studios/asuna_api/archive/0.1.5.tar.gz",
    keywords= ["wrapper", "api", "random"],
    install_requires= ["aiohttp", "yarl"],
    classifiers= [
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
