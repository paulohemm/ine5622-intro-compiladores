# Makefile

.PHONY: all run clean

SRC1 := ./lexico.py
SRC2 := ./sintatico.py

all: run

run:
	@echo "=== Executando o programa ==="
	@python3 $(SRC1) 
	@python3 $(SRC2) 

venv:
	@echo "=== Configurando ambiente virtual ==="
	@python3 -m venv venv

run_venv: venv
	@echo "=== Executando o programa no ambiente virtual ==="
	@venv/bin/python $(SRC1)
	@venv/bin/python $(SRC2)

clean:
	@echo "=== Limpando arquivos temporários ==="
	@rm -rf __pycache__ venv run.log

help:
	@echo "=== Comandos disponíveis ==="
	@echo "make           - Executa o programa"
	@echo "make run_venv  - Executa o programa usando um ambiente virtual"
	@echo "make clean     - Limpa arquivos temporários"