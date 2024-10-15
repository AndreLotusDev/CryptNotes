---
aliases: 
tags: 
date created: terça-feira, outubro 15º 2024, 6:48:40 pm
date modified: terça-feira, outubro 15º 2024, 7:00:02 pm
---
Lookup table: Consiste em fazer o caminho reverso, alguém iterou um banco de senhas geralmente usadas, hasheou usando algum algoritmo e fez um de para, exemplo, senha A em MD5 produz X, assim permite que se faça o caminho de IDA e volta, ai quando o atacante tem acesso ao banco de dados basta ele consultar a tabela de consulta.

Isso é muito usado em bancos que utilizam MD5 para hashing, o atacante acessa o banco e tenta usar a lookup table para descobrir as senhas, por isso é importante em sistemas como esse o uso de SALT ou simplesmente atualizar para uma algoritmo mais moderno.

---

Rainbow table: A diferença entre o lookup table e rainbow table se dá que em vez de guardar um hash inteiro, ele guarda parte do hash e outra parte como algoritmos de reduces, com isso trocando espaco em disco por espaco em memoria.

Ambos ataques dependem que o sistema não tenha SALT no meio, pois se tem, acaba dificultando a descoberta reversa dos plain text. (isso se cada senha recebe um SALT diferente). Pois se o sistema inteiro usa o mesmo SALT, é só questão do atacante re gerar as duas tabelas (isso se o algoritmo for permissivel computacionalmente falando).

---

