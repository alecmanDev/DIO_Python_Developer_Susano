from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="mymath-alves-test",
    version="0.0.1",
    author="Alessandro Alves",
    description="Pacote de operações matemáticas básicas",
    long_description=page_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],  # Nenhuma dependência
    python_requires='>=3.5',
)
 