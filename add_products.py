import requests
import random
import json

API_URL = "http://127.0.0.1:8000/produtos/"

NOMES = [
    "Notebook Gamer", "Smartphone", "Monitor UltraWide", "Mouse Gamer", "Teclado Mecânico",
    "Fone de Ouvido Bluetooth", "Cadeira Gamer", "Webcam Full HD", "SSD NVMe 1TB", "Placa de Vídeo RTX 3060",
    "Impressora Multifuncional", "Roteador Wi-Fi 6", "Smart TV 4K", "HD Externo 2TB", "Gabinete Gamer",
    "Cooler para Processador", "Memória RAM 16GB DDR4", "Processador Ryzen 5", "Placa-Mãe AM4", "Headset Gamer",
    "Ventilador", "Ar Condicionado", "Lâmpada Inteligente", "Alexa Echo Dot", "Carregador Turbo", "Caixa de Som JBL",
    "Monitor Curvo", "Notebook Ultrafino", "Câmera de Segurança", "Controle Xbox", "Joystick USB"
]

DESCRICOES = [
    "Produto de alta qualidade", "Última geração", "Ideal para gamers", "Ótima performance",
    "Design moderno e ergonômico", "Durável e confiável", "Alta resolução", "Conexão rápida",
    "Som imersivo", "Excelente custo-benefício"
]

HEADERS = {
    "Content-Type": "application/json"
}

for i in range(1, 301):
    name = f"{random.choice(NOMES)} {i}"
    description = random.choice(DESCRICOES)
    price = round(random.uniform(50, 5000), 2)

    product = {
        "name": name,
        "description": description,
        "price": price
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, data=json.dumps(product))
        response.raise_for_status()
        print(f"✔ Produto {i} adicionado com sucesso!")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao adicionar o produto {i}: {e}")

print("✅ Todos os produtos foram enviados!")
