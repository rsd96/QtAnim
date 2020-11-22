from setuptools import setup

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='QtAnim',
    version='0.0.1',
    description='Easy animation for PyQt!',
    py_modules=['QtAnim'],
    package_dir={'': 'src'},
    long_description=description,
    long_description_content_type='text/markdown',
    extras_require = {
        "dev" : [
            "pytest>=3.7",
        ],
    },
)