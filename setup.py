from setuptools import setup, find_packages

def ler(arquivo):
    return [
        req.strip() for req in open(arquivo).readlines()
    ]

setup(
    name = "Novo_projeto",
    version= "0.1.0",
    description="Novo projeto",
    packages= find_packages(),
    include_package_data= True,
    install_requires = ler("requirements.txt")
)

