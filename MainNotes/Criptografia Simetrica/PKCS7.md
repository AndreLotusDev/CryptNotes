---
aliases: 
tags: 
date created: sexta-feira, outubro 11º 2024, 6:03:25 pm
date modified: sexta-feira, outubro 11º 2024, 6:07:38 pm
---
## PKCS#7: Uma Sintaxe Padrão para Mensagens Criptografadas

**PKCS#7** (ou CMS, Cryptographic Message Syntax) é um padrão que define uma estrutura comum para armazenar dados que foram criptografados ou assinados digitalmente. Essencialmente, ele serve como um "envelope" que contém os dados originais, juntamente com informações sobre a criptografia aplicada, como o algoritmo utilizado e a chave pública do destinatário.

### A Relação entre PKCS#7 e Padding

PKCS#7 define um padrão para a sintaxe de mensagens criptografadas, incluindo a forma como o padding deve ser aplicado. Ele especifica um método simples e eficiente para adicionar padding a um bloco de dados:

- **Valor de padding:** O valor de cada byte adicionado ao bloco é igual ao número total de bytes de padding.
- **Detecção do padding:** Ao descriptografar a mensagem, o valor do último byte indica o número de bytes de padding que devem ser removidos.

**Exemplo:**

Se um bloco de dados tem 16 bytes e a mensagem original ocupa apenas 11 bytes, 5 bytes de padding serão adicionados. Cada um desses 5 bytes terá o valor 5 (hexadecimal 0x05). Ao descriptografar, o receptor verifica o último byte (0x05) e remove os 5 bytes anteriores.