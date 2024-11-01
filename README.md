# 🔐 FernetHasher: Secure Encryption & Key Archiving in Python

## Overview
FernetHasher é uma classe Python projetada para simplificar a criptografia e descriptografia de dados usando o poderoso algoritmo **Fernet** do módulo `cryptography`. Com a geração de chaves, armazenamento seguro e criptografia robusta, esta classe é sua aliada para manter informações seguras. Utiliza `SHA-256` para hashar uma string gerada aleatoriamente e codifica em Base64 para gerar chaves seguras. Além disso, oferece o armazenamento automático da chave em um arquivo opcional, para facilitar a recuperação e a consistência.

## 🔧 Funcionalidades
- **Geração de Chaves Seguras**: Use strings aleatórias e hash SHA-256 para criar uma chave segura.
- **Armazenamento de Chaves**: As chaves podem ser arquivadas automaticamente, garantindo que você sempre tenha uma cópia segura.
- **Criptografia e Descriptografia**: Facilite a proteção de dados confidenciais com métodos fáceis de criptografia e descriptografia.
- **Controle e Flexibilidade**: Suporta tanto `bytes` quanto `strings`, permitindo que você insira e recupere dados de forma conveniente.

## 📁 Estrutura do Projeto
A estrutura do projeto é simples e modular:
```plaintext
project-root
│
├── keys/               # Diretório onde as chaves são armazenadas
├── main.py             # Arquivo principal de execução
└── README.md           # Documentação do projeto
````

🚀 Instalação:

Clone o repositório e instale as dependências necessárias:
git clone https://github.com/sdouglasilva/gerenciador_de_senhas/
cd fernethasher
pip install -r requirements.txt

🛠️ Uso:
Gere uma chave segura:

from main import FernetHasher
key, key_path = FernetHasher.create_key(archive=True)
print(f"Chave gerada: {key}")
if key_path:
    print(f"Chave armazenada em: {key_path}")

Crie um objeto FernetHasher para criptografar e descriptografar:

fernet_hasher = FernetHasher(key)
encrypted = fernet_hasher.encrypt("Mensagem secreta")
decrypted = fernet_hasher.decrypt(encrypted)
print(f"Criptografado: {encrypted}")
print(f"Descriptografado: {decrypted}")

Armazene a chave (opcional, habilite archive=True em create_key para armazená-la automaticamente)

🤖 Métodos Principais
FernetHasher.create_key(archive=False): Cria uma nova chave segura. O parâmetro archive permite armazenar a chave.
FernetHasher.encrypt(value): Criptografa uma string ou bytes.
FernetHasher.decrypt(value): Descriptografa um valor criptografado.
📝 Notas
Certifique-se de ter o diretório keys criado antes de usar a função archive_key.
Segurança da Chave: Proteja sua chave. Compartilhar ou perder sua chave pode comprometer a segurança dos dados criptografados.
🔗 Dependências
cryptography
pathlib

Divita-se!
