<h1>Desenvolvedores</h1>

## Índice
* [Pastas](#pastas)
* [Arquivos](#arquivos)

## Pastas
```
ServerAPI
```
Pasta do qual hospeda o servidor api através do fastAPI e controla a questão do database também, como se fosse um CRUD.

```
BOT
```
Onde recebe as requisições(menssagens) do usuário final, faz envio para o servidor API, recebe a resposta e retorna para o usuário final.

```
AI
```
Pasta responsável pelo sistema de inteligência e processamento de menssagens. Para entender melhor como o sistema de AI utilizado no projeto funciona, por favor [clique aqui](AI/DEVELOPER.md)

```
var
```
Onde está hospedado alguns arquivos, como localização de databases e chave token. Nesse caso ignorado pelo .gitignore por medidas de segurança.





## Arquivos
```
__main__.py 
```

Arquivo principal do qual executa o projeto inteiro. A execução se dá na pasta root(app) do projeto em modo script.

Ex.: python -m app

