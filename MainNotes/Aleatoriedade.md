---
aliases: 
tags: 
date created: sexta-feira, outubro 11º 2024, 8:49:39 am
date modified: sexta-feira, outubro 11º 2024, 9:32:42 am
---
# Notas
 
- Random Number Generator
- Pseudorandom Number Generator
- Nem tudo que é único significa que aleatório
- Por exemplo o NET não gera GUID's criptograficamente seguro

Os computadores podem gerar aleatoriedade confiável, todavia isso continua não sendo aleatoriedade real, somente o mundo real pode produzir aleatoriedade real (ou pode não ser, apenas não podemos inferir de forma externa, já que estamos inseridos nele internamente).

---

Em jogos aleatoriedade é muito importante, pois garante que a imersão no jogo seja bem feita, exemplo, calcular entre dano mínimo e máximo para dar de output em algum MOB. 

---

Outro ponto a se considerar, é que sistemas pseudo aleatórios devem ser protegidos, pois, se o atacante tem acesso ao algoritmo que produz os códigos pseudo aleatorios portanto ele irá conseguir quebrar a criptografia.

Além do que, geração procedural sempre se baseiam em uso de seed (sementes).

---

# Geração

Geralmente para gerar números pseudo aleatórios, é necessário de uma semente (seed) e também uma fonte geradora de número, que baseia em entropia e desordem, como aparelhos eletrônicos.

![[Pasted image 20241011085920.png]]
