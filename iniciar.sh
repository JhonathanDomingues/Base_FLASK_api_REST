#!/bin/bash
echo "Criando venv"
python3 -m venv venv
source ./venv/bin/activate
echo "Instalando pacotes"
make install
