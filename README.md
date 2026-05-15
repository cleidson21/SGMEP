# SGMEP - Sistema de Gestão

Este repositório contém o **SGMEP**, um sistema de gerenciamento leve e eficiente desenvolvido inteiramente em **Python**. O projeto tem como objetivo automatizar e organizar o cadastro de clientes e o controle de ordens de manutenção, utilizando uma interface interativa via terminal (CLI).

## 🚀 Arquitetura e Funcionalidades
O código foi estruturado de forma modular para aplicar boas práticas de Engenharia de Software, facilitando a escalabilidade e a manutenção do sistema:

- **`clientes.py`:** Módulo dedicado à gestão dos usuários, contendo as lógicas de adição, busca e controle de dados dos clientes.
- **`manutencao.py`:** Módulo responsável pelo registro, acompanhamento e atualização do status dos serviços de manutenção.
- **`sistema.py` e `main.py`:** Ponto de entrada e motor da aplicação. Eles integram os módulos de clientes e manutenção, gerenciando os menus e a interação com o usuário final.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Paradigma:** Programação estruturada/modular
- **Interface:** Command Line Interface (CLI)
