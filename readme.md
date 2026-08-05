# API Connect

## Objetivo da API

A API Connect é uma aplicação back-end desenvolvida como um MVP (Minimum Viable Product) com o objetivo de disponibilizar uma API REST para gerenciamento de usuários.

O sistema permite realizar operações de criação, consulta, atualização e remoção de usuários através de requisições HTTP, facilitando a comunicação entre aplicações.

A aplicação foi desenvolvida seguindo boas práticas de organização de código, separando responsabilidades entre componentes da aplicação para facilitar manutenção, leitura e evolução do projeto.

---

## Tecnologias utilizadas

* Python
* Flask
* API REST
* JSON para armazenamento dos dados
* Git para versionamento
* GitHub para hospedagem do projeto

---

## Estrutura do projeto

```
API-Connect/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── app/
    ├── controllers/
    ├── routes/
    └── data/
```

---

## Como executar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/zPauloz/api-connect-paulo-pereira.git
```

### 2. Acessar a pasta do projeto

```bash
cd api-connect-paulo-pereira
```

### 3. Criar um ambiente virtual

No Windows:

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a aplicação

```bash
python main.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

# Endpoints da API

## Criar usuário

**Método:** POST

**Endpoint:**

```
/users
```

**Descrição:**

Cria um novo usuário no sistema.

**Exemplo de requisição:**

```json
{
    "nome": "Paulo Pereira",
    "email": "paulo@email.com",
    "idade": 20
}
```

---

## Listar usuários

**Método:** GET

**Endpoint:**

```
/users
```

**Descrição:**

Retorna todos os usuários cadastrados.

---

## Buscar usuário por ID

**Método:** GET

**Endpoint:**

```
/users/<id>
```

**Descrição:**

Retorna um usuário específico através do seu identificador.

**Exemplo:**

```
GET /users/1
```

---

## Atualizar usuário

**Método:** PUT

**Endpoint:**

```
/users/<id>
```

**Descrição:**

Atualiza as informações de um usuário existente.

**Exemplo de requisição:**

```json
{
    "nome": "Paulo Silva",
    "email": "paulo.silva@email.com",
    "idade": 21
}
```

---

## Remover usuário

**Método:** DELETE

**Endpoint:**

```
/users/<id>
```

**Descrição:**

Remove um usuário cadastrado na API.

**Exemplo:**

```
DELETE /users/1
```

---

## Considerações finais

A API Connect representa uma solução back-end organizada, documentada e versionada utilizando ferramentas profissionais de desenvolvimento.

O projeto permite futuras melhorias, como integração com banco de dados, autenticação de usuários, testes automatizados e publicação em ambiente de produção.
