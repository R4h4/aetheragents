from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="aetheragents",
    version="0.0.1",
    author="Karsten Eckhardt",
    author_email="karsten.eckhardt@gmail.com",
    description="AetherAgents is an easy to use framework for creating AI agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/R4h4/aetheragents",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=2.0.0",
        "openai",
    ],
    extras_require={
        "dev": ["pytest"],
    },
)
