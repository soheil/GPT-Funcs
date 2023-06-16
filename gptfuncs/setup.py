from setuptools import setup, find_packages

setup(
    name="GPT-Funcs",
    version="1.0.0",
    author="Soheil Sam Yasrebi",
    author_email="ysoheil@gmail.com",
    description="A short description of your package",
    long_description=long_description,
    url="https://github.com/soheil/GPT-Funcs",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
