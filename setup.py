from setuptools import setup, find_packages

setup(
    name="match",
    version="0.0.2",
    description="Truepic Image Matching Service",
    url="http://truepic.com",
    author="Truepic Inc.",
    author_email="oliver@truepic.com",
    license="Proprietary",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3.6",
    packages=find_packages("src/main/python"),
    package_dir={"": "src/main/python"},
    entry_points={"console_scripts": ["match = app:app"]},
    test_suite="nose.collector",
    install_requires=[
        "numpy==1.16.2",
        "scipy==0.19.0",
        "flask==1.0.2",
        "scikit-image==0.14.2",
        "flasgger==0.9.2",
        "python-dotenv==0.10.1",
        "certifi==2019.3.9",
        "elasticsearch==6.3.0",
        "six==1.12.0",
        # Dev
        "pre-commit==1.14.4",
        "black==18.9b0",
        "isort==4.3.4",
        "pylint==2.2.2",
        "pytest==4.0.1",
        "pytest-cov==2.6.1",
        "pytest-picked==0.4.0",
        "pytest-sugar==0.9.2",
        "autoflake==1.2",
        "nose==1.3.7",
        "mypy==0.650",
        # Prod
        "gunicorn==19.9.0",
    ],
)
