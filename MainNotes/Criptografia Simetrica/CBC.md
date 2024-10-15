---
aliases: 
tags: 
date created: sexta-feira, outubro 11º 2024, 5:41:23 pm
date modified: sexta-feira, outubro 11º 2024, 5:46:22 pm
---
O resultado de um bloco alimenta o bloco seguinte via XOR.
Initialization vector para o primeiro bloco.

É feita de forma sequencial, portanto não se beneficia do paralelismo.

![[Pasted image 20241011174319.png]]

É mais seguro que o ECB.

---

O CBC acaba sendo mais seguro que o ECB justamente por ter um vetor de inicialização e cada bloco conseguinte depender do anterior, dificultando assim a analise.