Existem dois tipos de criptografia:

- Criptografia Simétrica (Chave privada)
- Criptografia Assimétrica (Chave pública)
- Hashing

---

- A criptografia assimétrica é bem mais devagar que a criptografia simétrica, portanto utilizamos dependendo do contexto formas diferentes de criptografia e misturadas para ajudar na situação.

- A diferença entre criptografia simétrica e assimétrica se da por que a simétrica se usa a mesma chave na ida e na volta, enquanto a assimétrica se usa uma para ir e uma para voltar, e a assimétrica é uma das bases por que a internet é possível, e HTTPS é realmente seguro e se faz possível trafegar dados sensíveis (cartão de crédito e etc).

- A criptografia de hashing existem diferentes formatos, o mais usado atualmente é o sha256 e atualmente é muito seguro, todavia com os aumentos da performance do computador pode ser necessário futuramente adotar outras metodologias.

- Um exemplo disso é o MD5, ele atualmente era bom para o hash, com o advento de aumento de performance dos computadores, ele não é mais útil, inclusive é recomendável migrar para o sha256. Há também a possibilidade de usar MD5 com SALT para continuar usando MD5 por um tempo.
    - Para se ter ideia, existem projetos que contem todos os dados possívels hasheados com md5 

---
