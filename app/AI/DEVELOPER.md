<h1>Documentação</h1>

## Índice
* [Como funciona o DATABASE](#funcionamento-do-database)
* [Como funciona o sistema de AI](#funcionamento-do-sistema-de-ai)
* [Arquivos e pastas](#arquivos-e-pastas)

## Funcionamento do DATABASE
<h3>Estrutura de dados</h3>

```
{
  "MESSAGE_RECEIVED": "OI", #Menssagem principal, quando o usuário enviar uma menssagem, vai ser filtrada usando essa.
  "FREQUENCY": 5, #Quantidade de vezes utilizadas
  "RESPONSE": [ #Array com lista de respostas para responder.
    {
      "message": "como vai?", #Menssagem para responder
      "frequency": 5, #Quantidade de vezes utilizada
      "context": [ #Contexto da conversa, normalmente as 3 últimas menssagens enviada pelo usuário. 
        "Tudo bem?",
        "Como vai?"
      ]
    }
  ]
}
```

## Funcionamento do sistema de AI

O sistema de <strong>AI</strong> funciona por processos, como uma situação de etapas.

Para entender o funcionamento do mesmo é essencial que você tenha vista o funcionamento da [estrutura de dados](#funcionamento-do-database), pois a partir dela você entenderá alguns termos.


### <strong>getMessage</strong>
É o primeiro processo chamado e tem como papel principal, verificar se existe algum "MESSAGE_RECEIVED" <strong>igual</strong> no database, caso haja retorna.
<br>
<strong>Obs.:</strong> Vale resaltar que estamos de valores totalmente iguais, sem qualquer diferença.
<br>

### <strong>messageNtFound</strong>
Caso o parametro acima falhe, nós iremos fazer uma busca por palavras que sejam a iguais, porém com variações de vogais.

Exemplo: Bom dia e booooom diaa, tem o mesmo significado, porém com variações de vogais.

### <strong>learnNew</strong>
Nesse caso, todos os passos acima falhou e o bot irá enviar um menssagem solicitando que o usuário ensine o que o Bot deve responder. 
<br>
<br>
<br>
## Arquivos e pastas
```
ai_system.py
```
Sistema que faz a AI funcionar, em resumo possui as funcionalidades acima.

```
crud.py
```
Faz requisições no DB.

```
machine.py
```
Arquivo que reune as defs e classes - arquivo principal.