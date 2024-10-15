---
aliases: 
tags: 
date created: terça-feira, outubro 15º 2024, 6:34:00 pm
date modified: terça-feira, outubro 15º 2024, 6:46:24 pm
---
O metodo de brute force consiste em tentar por meio de falha e re tentativa ate achar o hash correto, todavia esse metodo consome muitos recursos computacionais e acaba sendo na maior parte do tempo o menos eficiente, com exceção para hashs antigos e faceis de serem quebrados, como o MD5.

A eficiencia de um brute force está diretamente interligado com a qualidade do algoritmo de hashing, hashing com mts colisões apresentam metodos menos seguros contra brute force.

Certos algoritmos rodam mais rapido em hardware especializado, por isso alguns ataques são feitos por servidores especializados em cometer ataques de forca bruta, isso quando o sistema tem uma falha que permite isso.

---

Mask Attack:

É um ataque de força bruta que utiliza uma mascara para tentar achar a senha, por exemplo, se a senha tem 8 caracteres e é composta por letras minusculas e numeros, a mascara seria: ?l?l?l?l?l?l?l?l?d?d?d?d

Consumindo assim, muito menos tempo para achar a senha.

Esses ataques tendem a serem avassaladores, pois as pessoas tendem a usar mesmas senhas e mesmo padrões ao criar suas senhas.

---

Ou seja, caso o atacante use um ataque sofisticado, nossa única maneira de nós protegermos é usar algoritmos lentos, e tambem dar lock no usuário caso alguém tente acessar ele diversas vezes em algum curto periodo de tempo.