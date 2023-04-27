# Fastapi Tutorial

Código do projeto desenvolvido na série de vídeos nessa [playlist](https://www.youtube.com/playlist?list=PLstjCH2DwkBnKO9PdHc5NO1JOwbJdcq22).



## Criando o embiente virtual (venv) no Windows

Caso esteja no windows, rode o comando a seguir na raiz do prohjeto para criar o ambiente, caso não tenha criado antes:
```
python -m venv fastapi-env
```
Ative o ambiente com o comando se estiver utilizando o cmd
```
fastapi-env\Scripts\activate.bat
```
Caso esteja utilizando o PowerShell, ative com o comando abaixo:
```
fastapi-env\Scripts\Activate.ps1
```

## Criando o embiente virtual (venv) no Linux

Depois de instalar o pacote do python3 e python3-venv, crie o ambiente na raiz do projeto com o comando:
```
python3 -m venv fastapi-env
```
Ative o ambiente com o comando:
```
source fastapi-env/bin/activate
```

## Saindo do embiente virtual (venv)
Digite o comando deactivate para sair do ambiente virtual.

## Instalando as dependências

Utilize o pip para baixar as dependências do projeto:

```
pip install -r requirements.txt
```

ou 

```
pip3 install -r requirements.txt
```

## Execução

Para executar o projeto, utilize o comando abaixo na raiz do projeto:

```
uvicorn main:app --reload 
```

Para gerar um arquivo SQLite com as tabelas do projeto, rode o script cria_tabelas.py  

```
python3 cria_tabelas.py    
```

## Testes

Para executar os testes rode:

```
pytest tests/
```

Para consultar a documentação da API, acesse http://localhost:8000/docs e para interomper a execução pressione «Ctrl»+«C».