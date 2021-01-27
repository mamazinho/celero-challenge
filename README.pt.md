Essa aplicação faz parte do desafio Back-end da Celero

Leia essa documentação em [EN-US](README.md)

## Tecnologias
* Django
* Django Rest framework
* AngularJs

## A base do projeto:
* Temos um template principal renderizado pelo Django, após carregado, os resto do front-end é renderizado pelo AngularJS, onde ele começará a enviar requisições para a API, que esta rodando no Django Rest Framework.


## Dúvidas:
***Por que usar um Framework Front-end?***
* Eu optei por usar um framework front-end porque ele é de grande ajuda na interatividade e em como os dados são mostrados ao usuário, como o principal objetivo do Django Rest Framework é ser um API, eu o tratei assim, deixando as renderizações para o front-end e entregando um fluxo completo.

***Por que AngularJs?***
* Apesar de eu preferir VueJs para front-end, o angularJs permite uma simplicidade por rodar dentro do Django, dessa maneira o angularJs pode ser usado como um mini-framework melhor do que o vueJs.

***Por que a relação ManyToMany ocorre no Athlete_infos e não no Atleta?***
* Se a relação fosse feita usando o atleta eu poderia abrir o atleta e ter todos os eventos que ele participou mais facilmente, mas eu não teria a mesma facilidade para pegar as informações dos atletas por evento. Então, é melhor a informação do atleta ter vários eventos e vários eventos com essas informações ao invés do atleta em si. Mas estou aberto para receber sugestões sobre modelagem de dados ou qualquer outro problema.

***Tempo para rodar o comando de popular o banco de dados***
* Eu testei dois caminhos, o mais usado para performar em batchs é o bulk_create, para fazer apenas uma query para o banco de dados. Eu tentei seguir esse caminho (disponível no arquivo 'populateDB2.py'), mas o ganho de performance ainda é baixo, porque ainda demora muito para ler e popular as listas, e foi apenas um teste, eu deixei o arquivo como uma ideia não finalizada. Outro caminho, que funcionou, foi usar o basico get_or_create (disponível no arquivo 'populateDB.py'). Ambas as versões podem levar mais de meia hora para rodar todas as queries necessárias. Por esse motivo eu deixei um arquivo sql, caso não queira esperar todo o processo para popular o banco de dados, é melhor rodar o comando `mysql celero < challenge/utils/athlete_events.sql` depois de fazer as migrations. Estou aceitando sugestões,  fazer a rotina performar bem foi a parte mais difícil para mim.

***Por que Heroku?***
* Heroku foi o melhor custo-benefício encontrado, pois oferece um plano gratuito com 10.000 linhas disponíveis para uso nas tabelas do banco de dados e tem uma integração muito fácil com o github. Ele tem um delay para fazer as operações de CRUD, as vezes a página precisa ser recarregada para aplicar o que foi feito, isso é um problema entre a reatividade do angularJs e o heroku, localmente isso não ocorre.


## Servers:
Você pode acessar a aplicação no Heroku App clicando [aqui](https://challenge-celero.herokuapp.com/).
Heroku tem um limite na quantidade de linhas que podem ser salvas por tabela no banco de dados no seu plano gratuito, por isso, essa versão possui menos registro de atletas e eventos. Eu coloquei um limite fixo também, para deixar-lo criar novos atletas, eventos e informações.

## Rodando em uma máquina local
Você pode entrar as instruções para rodar o projeto em sua máquina Linux no texto abaixo:

## Instalando virtualenvwrapper and criando um virtualenv:
    $ sudo apt-get install python-pip
    $ pip install --upgrade virtualenv
    $ sudo apt-get install python3 python3-pip virtualenvwrapper libmysqlclient-dev libsnappy-dev gcc libssl-dev
    $ source /etc/bash_completion.d/virtualenvwrapper
    $ mkvirtualenv -p /usr/bin/python3 celc

## Como configurar o banco de dados:
    $ sudo apt install mysql-server
    $ sudo mysql -e "CREATE DATABASE celero"
    $ sudo mysql -e "CREATE USER celero IDENTIFIED BY 'c3l3r0'"
    $ sudo mysql -e "GRANT ALL ON celero.* TO 'celero'@'%' IDENTIFIED BY 'c3l3r0'"
    $ sudo mysql -e "GRANT ALL ON test_celero.* TO 'celero'@'%' IDENTIFIED BY 'c3l3r0'"

## Como fazer as configurações básicas do projeto:
    $ workon celc
    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py populateDB
    or, the fast way to populate:
    $ sudo mysql celero < challenge/utils/celero.sql

## Como rodar:
    $ python manage.py runserver

## Como rodar os testes unitários:
    $ python manage.py test

## Como accessar:
    No terminal mostrará algo como 'http://127.0.0.1:[port number]', basta colocar esse endereço no seu navegador e usa-lo.