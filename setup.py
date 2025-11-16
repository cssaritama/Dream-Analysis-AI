from setuptools import setup, find_packages

setup(
    name="dream-analysis-ai",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.5.0",
        "streamlit>=1.12.0",
        "scikit-learn>=1.0.0"
    ],
)
