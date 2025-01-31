# 🛍️ FastSearch - Busca Rápida com FastAPI e Elasticsearch 🚀

O objetivo é criar um sistema de **busca full-text e autocomplete** otimizado para e-commerce e aplicações que exigem **pesquisas rápidas e escaláveis**. Ele utiliza **FastAPI** e **Elasticsearch**, seguindo a **Arquitetura Limpa (Clean Architecture)**.

---

## 📌 Tecnologias Utilizadas
- **FastAPI** - Framework assíncrono para APIs rápidas 🚀
- **Elasticsearch** - Motor de busca escalável ⚡
- **Poetry** - Gerenciador de dependências 🧐
- **Docker** - Para rodar a API e Elasticsearch 🐳
- **Python 3.10+** - Linguagem principal 🐍

---

## 📌 Arquitetura do Projeto
O FastSearch segue a **Arquitetura Limpa**, garantindo modularidade e manutenibilidade.

```
FastSearch/
│── app/
│   ├── domain/          # Camada de Domínio (Modelos e Interfaces)
│   │   ├── entities/    # Modelos de Produto (Entidades)
│   │   │   ├── products.py
│   │   ├── interfaces/  # Interfaces dos Repositórios
│   │   │   ├── i_products.py
│   │
│   ├── application/     # Camada de Aplicação (Casos de Uso)
│   │   ├── product_use_case.py # Regras de Negócio
│   │
│   ├── infrastructure/  # Camada de Infraestrutura (Bancos, Elasticsearch)
│   │   ├── elasticsearch.py  # Conexão com Elasticsearch
│   │   ├── repositories.py   # Implementação do Repositório com Elasticsearch
│   │
│   ├── presentation/   # Camada de Apresentação (Controllers e API)
│   │   ├── routes.py   # Rotas da API (FastAPI)
│   
│── add_products.py  # Script para inserir produtos
│── poetry.lock
│── pyproject.toml
│── Dockerfile
│── docker-compose.yml
│── README.md
```

---

## 📌 Instalação e Configuração
### **1️⃣ Clonar o Repositório**
```sh
git clone https://github.com/seu-usuario/FastSearch.git
cd FastSearch
```

### **2️⃣ Instalar o Poetry**
Se ainda não tiver o Poetry instalado, execute:
```sh
pip install poetry
```

### **3️⃣ Instalar Dependências**
```sh
poetry install
```

### **4️⃣ Subir o Elasticsearch com Docker**
```sh
docker-compose up --build -d
```
Isso iniciará os containers **FastAPI e Elasticsearch**.

### **5️⃣ Testar se a API Está Rodando**
Abra no navegador:
🔗 **http://127.0.0.1:8000/docs**  
Se a API estiver rodando, você verá a **documentação interativa**.


✅ Após o container subir, script de inserção de produtos irá começar!

### **3️⃣ Verificar se os Produtos Foram Inseridos**
Agora, saia do container e teste se os produtos estão no Elasticsearch.

Saia do container:
```sh
exit
```

Agora, faça uma requisição para buscar produtos:
```sh
curl -X GET "http://127.0.0.1:8000/produtos/busca/?q=Laptop"
curl -X GET "http://127.0.0.1:8000/produtos/autocomplete/?q=Smar"
curl -X GET "http://127.0.0.1:8000/produtos/busca/?q=Laptop&price_min=1000&price_max=3000"

```
Se os produtos foram inseridos corretamente, a API **retornará a lista de produtos cadastrados**. 🚀


