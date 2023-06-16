from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gptfuncs",
    version="1.0.0",
    author="Soheil Sam Yasrebi",
    author_email="ysoheil@gmail.com",
    description="Automatically pass your funcions defined in Python to ChatGPT have it call them back seemlessly.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/soheil/GPT-Funcs",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
