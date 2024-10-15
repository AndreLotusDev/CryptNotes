---
aliases: 
tags: 
date created: terça-feira, outubro 15º 2024, 7:08:09 pm
date modified: terça-feira, outubro 15º 2024, 7:20:18 pm
---
JWT é uma estrutura JSON. Ele é composto por três partes: cabeçalho, payload e assinatura. Que é assinado com HMAC.

O header em vermelho, o payload em roxo, a assinatura em azul. (imagem abaixo).

![[Pasted image 20241015191130.png]]

Atualmente o JWT virou sinonimo de autenticação em SPA.

JWT é o acronimo de JSON Web Token, que é um padrão aberto (RFC 7519) que define uma maneira compacta e auto-contida para transmitir informações entre duas partes.

![[Pasted image 20241015190910.png]]

---

Algumas anotações sobre segurança: 

- **Evite localStorage e sessionStorage:** Esses locais são vulneráveis a ataques XSS (Cross-Site Scripting).
- **Prefira Cookies Seguros:** Armazene o JWT em cookies com as flags `HttpOnly`, `Secure` e `SameSite` ativadas. Isso reduz o risco de acesso via scripts maliciosos.