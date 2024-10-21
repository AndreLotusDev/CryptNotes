---
aliases: 
tags: 
date created: terça-feira, outubro 15º 2024, 7:53:38 pm
date modified: quarta-feira, outubro 16º 2024, 12:22:15 pm
---
A criptografia de chave pública consiste tem ter uma chave pública e privada onde as duas em conjunto conseguem descriptografar e criptografar uma mensagem.

Por exemplo, usamos RSA para trafegar dados na internet com o protocolo HTTPS.

A chave publica e privada elas são ligadas matematicamente, permitindo que as duas pessoas que facam o handshake consigam trafegar informacao com seguranca e o atacante no meio (man in the middle) não consiga ler, somente aos dois interessados das pontas.

A chave publica pode ser compartilhada com qualquer pessoa.

A chave privada deve ser mantido em segredo de estado e somente com voce, caso voce vaze sua chave privada, voce deve re gerar novamente ela para sua seguranca.

![[Pasted image 20241015201101.png]]

---

A criptografia assimetrica foi criada com propositos militares a priori. 

---

ARPANET 
	Inicio do protocolo TCP/IP

---

A criptografia se baseia em problemas de facil de ir e dificil de voltar, como por exemplo, multiplicar um numero por outro é relativamente fácil, só que o caminho contrário não é, dado que se tem infinitos caminhos de divisao para finalmente achar o numero correto.

---

A criptografia assimetrica se escora na premissa que algumas operações matemáticas são fáceis de se fazer, mas difíceis de se desfazer.

O problema do logaritmo discreto é um exemplo disso.
