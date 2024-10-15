---
aliases: 
tags: 
date created: terça-feira, outubro 15º 2024, 6:24:05 pm
date modified: terça-feira, outubro 15º 2024, 6:32:51 pm
---
Geralmente usamos hash para senha em vez de criptografar, pois se o atacante adquire a chave ele terá portanto acesso a todas as senhas.

A chave se torna ponto único de falha.

Não é possível rotacionar a chave..

---

Hashear uma mensagem "A" sempre irá produzir a mesma saida, facilitando assim o armazenamento segura das senhas.

---

Todo sistema de autenticação utiliza hash para armazenar as senhas.

SHA- são algoritmos rápidos.

Para senha deve ser lento.
	Portanto sempre use: Argon2, Bcrypt, Scrypt, PBKDF2 com 310.000 iteracoes e HMAC-SHA-256.
