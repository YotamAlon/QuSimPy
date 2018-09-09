import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QuSimPy",
    version="0.0.1",
    author="Adam Kelly",
    author_email="to-be@replaced.com",
    description="A Multi-Qubit Ideal Quantum Computer Simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamisntdead/QuSimPy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ),
    dependency_links=[
        'git+https://github.com/adamisntdead/QuSimPy.git#egg=QuSimPy-0'
    ]
)