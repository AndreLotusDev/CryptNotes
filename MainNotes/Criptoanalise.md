---
aliases: 
tags: 
date created: quarta-feira, outubro 9º 2024, 12:09:44 pm
date modified: quarta-feira, outubro 9º 2024, 12:53:42 pm
---
O processo de criptoanalise é o estudo de como encontrar pontos fracos no processo de criptografia para poder fazer a operação reversa e encontrar a mensagem original.

Passos da criptoanalise:
- Estudo do algoritmo
- Quebra total
- Dedução global
- Dedução de informação

---

Por exemplo, mesmo tendo criptografia de forma aleatoria, isso não esconde propriedades estáticas que se referem a linguagem humana, como a frequência de letras.

Por exemplo, a letra A é a mais comum em textos em portugues, então se um hacker souber disso, ele pode tentar quebrar a criptografia de um texto em portugues.

---

Outro exemplo é o ataque de força bruta, que consiste em tentar todas as combinações possiveis de chaves até encontrar a correta. Todavia em sistemas seguros, quando alguém tenta força bruta logo ele é bloqueado de fazer requests sucessivos, portanto sendo uma técnica muito antiga e pouco eficaz.

---

# Criptoanalise - The Caesar Cipher

O passo mais importante de uma criptoanalise, quando possível é analisar a origem e linguagem empregada no texto, isso se da pois, quando sabemos a origem e língua de um texto podemos ter uma distribuição de letras empregada em determinada linguagem, facilitando assim a analise.

Por exemplo, no português a letra 'a' é a mais comum, logo se encontrarmos uma letra que se repete muito, podemos inferir que ela é a letra 'a'.

![[Pasted image 20241009125112.png]]

---

# Criptoanalise - Vigenere Cipher

- O primeiro passo é observar repetições de letras no texto cifrado, isso pode indicar que a chave é curta e que a cifra é uma cifra de substituição polialfabética.
- O segundo passo é tentar descobrir o tamanho da chave, isso pode ser feito com o uso de ferramentas como o indice de coincidência.
- Fazer analise de frequencia.

![[Pasted image 20241009125334.png]]

---

Por fim, a criptoanalise é um campo muito complexo e que exige muito tempo e dedicação para se tornar um especialista.



