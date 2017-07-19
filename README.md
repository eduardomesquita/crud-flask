# crud-flask
Exemplo de um CRUD utilizando Flask

## Versões

- python (>= 2.7.13)
- pip (>= 9.0.1)
- Docker (>= 1.13.1)
- Docker-Compose (>= 1.8.1)

## Subindo o mysql com Docker

- Dentro da pasta do projeto rode:

```bash
cd docker
docker-compose build
docker-compose up
```
## Ambiente Virtual python (Recomendado)

- Rode a aplicação dentro de um ambiente virtual para não bagunçar seu ambiente

```bash
virtualenv flask_crud
source flask_crud/bin/activate
```
## Instalando as dependências

- Dentro da raiz do projeto rode:
```bash
cd codigo-fonte/app
pip install -r requirements.txt
```

## rodando o projeto

```bash
python app.py 
```

## Utilizando a api

Criando o schema e tabelas no banco de dados:
```bash
curl http://localhost:5000/crud/generate
```
Console:
```console
database created successful
```
  Adicionando um dado:
  ```bash
  curl  -X POST -d '{"id": "1","nome":"Eduardo", "sobrenome": "Mesquita", "idade": "25", "endereco": {"id": "1", "logradouro": "SQS 406", "cidade": "Brasilia", "uf": "DF" } }' http://localhost:5000/crud/add
  ```
  Console:
  ```console
  ok
  ```
  Pesquisando um dados
  ```bash
  curl http://localhost:5000/crud/search/id?id_pessoa=5
  ```
  Console:
  ```console
  {"idade": 25, "endereco": {"cidade": "SQS 406", "uf": "Brasilia", "logradouro": 5, "id": 5}, "sobrenome": "Mesquita", "id": 5, "nome": "Eduardo"}
  ```
   Pesquisando todos os dados
  ```bash
  curl http://localhost:5000/crud/search/all
  ```
  Console:
  ```console
  [{"idade": 25, "endereco": {"cidade": "SQS 406", "uf": "Brasilia", "logradouro": 4, "id": 4}, "sobrenome": "Mesquita", "id": 4, "nome": "Eduardo"}", "{"idade": 25, "endereco": {"cidade": "SQS 406", "uf": "Brasilia", "logradouro": 5, "id": 5}, "sobrenome": "Mesquita", "id": 5, "nome": "Eduardo"}", "{"idade": 25, "endereco": {"cidade": "SQS 406", "uf": "Brasilia", "logradouro": 6, "id": 6}, "sobrenome": "Mesquita", "id": 6, "nome": "Eduardo"}"]
  ```
Removendo um dado:
  ```bash
  curl -X DELETE  http://localhost:5000/crud/delete/2
  ```
  Console:
  ```console
  ok
 ```
Alterando um dado:
  ```bash
  curl  -X PUT  http://localhost:5000/crud/update/1/Eduardo
  ```
  Console:
  ```console
  ok
 ```
