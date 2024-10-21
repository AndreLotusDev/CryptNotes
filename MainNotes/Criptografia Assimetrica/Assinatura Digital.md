---
aliases: 
tags: 
date created: terça-feira, outubro 15º 2024, 8:29:57 pm
date modified: terça-feira, outubro 15º 2024, 8:59:17 pm
---
A assinatura digital vem com o intuito de resolver o problema de adulteração de conteúdo na internet.

![[Pasted image 20241015205059.png]]

Aqui um pseudo codigo onde validamos um documento usando hashing

```python
# Pseudo-código em Python para validar um documento entre comunicadores A, B e C

# Função para simular a geração de um par de chaves (pública e privada)
def gerar_par_de_chaves():
    chave_privada = "chave_privada_de_A"
    chave_publica = "chave_publica_de_A"
    return chave_privada, chave_publica

# Função para assinar o documento usando a chave privada de A
def assinar_documento(documento, chave_privada):
    # Simula a criação de uma assinatura digital
    assinatura = hash(documento + chave_privada)
    return assinatura

# Função para verificar a assinatura do documento usando a chave pública de A
def verificar_assinatura(documento, assinatura, chave_publica):
    # Simula a verificação da assinatura digital
    assinatura_verificada = hash(documento + "chave_privada_de_A")
    return assinatura == assinatura_verificada

# Comunicador A gera seu par de chaves
chave_privada_A, chave_publica_A = gerar_par_de_chaves()

# A cria um documento
documento = "Este é um documento confidencial."

# A assina o documento
assinatura = assinar_documento(documento, chave_privada_A)

# A envia o documento e a assinatura para B

# B recebe o documento e a assinatura
documento_recebido = documento
assinatura_recebida = assinatura

# B verifica a assinatura
if verificar_assinatura(documento_recebido, assinatura_recebida, chave_publica_A):
    print("B: Documento válido e autêntico de A.")
else:
    print("B: Documento inválido ou não é de A.")

# Comunicador C tenta fraudar o documento
documento_falsificado = "Este é um documento falsificado."
# C não possui a chave privada de A, então não pode criar uma assinatura válida
# C tenta criar uma assinatura falsa
assinatura_falsa = assinar_documento(documento_falsificado, "chave_privada_de_C")

# B recebe o documento falsificado e a assinatura falsa
documento_recebido = documento_falsificado
assinatura_recebida = assinatura_falsa

# B verifica a assinatura
if verificar_assinatura(documento_recebido, assinatura_recebida, chave_publica_A):
    print("B: Documento válido e autêntico de A.")
else:
    print("B: Documento inválido ou não é de A.")
```

Agora usando chave publica e privada

```python
# Pseudo-código em Python para criptografia e descriptografia usando chaves públicas e privadas
# Cenário: Comunicador A envia um documento criptografado para B. C tenta interceptar ou fraudar o documento, mas não consegue.

# Importações simuladas para funções criptográficas
def gerar_par_de_chaves():
    # Simula a geração de um par de chaves pública e privada
    chave_privada = "chave_privada"
    chave_publica = "chave_publica"
    return chave_privada, chave_publica

def criptografar_mensagem(mensagem, chave_publica_destinatario):
    # Simula a criptografia da mensagem com a chave pública do destinatário
    mensagem_criptografada = f"encrypted({mensagem})_with_{chave_publica_destinatario}"
    return mensagem_criptografada

def descriptografar_mensagem(mensagem_criptografada, chave_privada_destinatario):
    # Simula a descriptografia da mensagem com a chave privada do destinatário
    mensagem = mensagem_criptografada.replace(f"encrypted(", "").split(")_with_")[0]
    return mensagem

def assinar_mensagem(mensagem, chave_privada_remetente):
    # Simula a assinatura digital da mensagem com a chave privada do remetente
    assinatura = f"signature_of({mensagem})_with_{chave_privada_remetente}"
    return assinatura

def verificar_assinatura(mensagem, assinatura, chave_publica_remetente):
    # Simula a verificação da assinatura com a chave pública do remetente
    assinatura_correta = f"signature_of({mensagem})_with_chave_privada"
    return assinatura == assinatura_correta

# Comunicador A gera seu par de chaves
chave_privada_A, chave_publica_A = gerar_par_de_chaves()

# Comunicador B gera seu par de chaves
chave_privada_B, chave_publica_B = gerar_par_de_chaves()

# A cria um documento
documento = "Este é um documento confidencial."

# A assina o documento com sua chave privada
assinatura = assinar_mensagem(documento, chave_privada_A)

# A criptografa o documento e a assinatura com a chave pública de B
conteudo_para_enviar = documento + "|" + assinatura
conteudo_criptografado = criptografar_mensagem(conteudo_para_enviar, chave_publica_B)

# A envia o conteúdo criptografado para B

# C tenta interceptar e fraudar o conteúdo
# C não pode descriptografar o conteúdo sem a chave privada de B
# C também não pode assinar um novo documento como se fosse A

# B recebe o conteúdo criptografado
conteudo_recebido = conteudo_criptografado

# B descriptografa o conteúdo com sua chave privada
conteudo_descriptografado = descriptografar_mensagem(conteudo_recebido, chave_privada_B)
documento_recebido, assinatura_recebida = conteudo_descriptografado.split("|")

# B verifica a assinatura com a chave pública de A
if verificar_assinatura(documento_recebido, assinatura_recebida, chave_publica_A):
    print("B: Documento válido e autêntico de A.")
    print("Conteúdo do documento:", documento_recebido)
else:
    print("B: Documento inválido ou assinatura incorreta.")

# C tenta enviar um documento falsificado para B
documento_falso = "Este é um documento falsificado."
assinatura_falsa = assinar_mensagem(documento_falso, "chave_privada_de_C")
conteudo_falso = documento_falso + "|" + assinatura_falsa
conteudo_falso_criptografado = criptografar_mensagem(conteudo_falso, chave_publica_B)

# B recebe o conteúdo falso criptografado
conteudo_recebido = conteudo_falso_criptografado

# B descriptografa o conteúdo com sua chave privada
conteudo_descriptografado = descriptografar_mensagem(conteudo_recebido, chave_privada_B)
documento_recebido, assinatura_recebida = conteudo_descriptografado.split("|")

# B verifica a assinatura com a chave pública de A
if verificar_assinatura(documento_recebido, assinatura_recebida, chave_publica_A):
    print("B: Documento válido e autêntico de A.")
    print("Conteúdo do documento:", documento_recebido)
else:
    print("B: Documento inválido ou assinatura incorreta.")

```