import socket
import subprocess
import platform
from datetime import datetime
import json
import os

ALVOS = ["8.8.8.8", "1.1.1.1", "8.8.4.4"]
PORTAS_TCP = [53, 80, 443]

def obter_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def testar_ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    comando = ["ping", param, "1", host]
    try:
        resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=3)
        return resultado.returncode == 0
    except subprocess.TimeoutExpired:
        return False

def testar_porta_tcp(host, porta, timeout=2):
    try:
        with socket.create_connection((host, porta), timeout=timeout):
            return True
    except (socket.timeout, socket.error):
        return False

def executar_diagnostico():
    timestamp_atual = obter_timestamp()
    print(f"[{timestamp_atual}] A iniciar diagnóstico de rede Linux/NetOps...\n")
    
    dados_relatorio = {
        "timestamp": timestamp_atual,
        "pings": {},
        "portas_tcp": {}
    }
    
    for alvo in ALVOS:
        ativo = testar_ping(alvo)
        status_ping = "SUCESSO (Online)" if ativo else "FALHA (Incontactável)"
        dados_relatorio["pings"][alvo] = status_ping
        print(f"-> Ping para {alvo}: {status_ping}")
        
    print("\n--- A testar Portas TCP Críticas ---")
    host_teste = "8.8.8.8"
    dados_relatorio["portas_tcp"][host_teste] = {}
    
    for porta in PORTAS_TCP:
        aberta = testar_porta_tcp(host_teste, porta)
        status_txt = "Aberta" if aberta else "Fechada/Filtrada"
        dados_relatorio["portas_tcp"][host_teste][str(porta)] = status_txt
        print(f"-> TCP {host_teste}:{porta} -> {status_txt}")
        
    # Guardar relatório em formato JSON
    nome_ficheiro = "relatorio_diagnostico.json"
    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        json.dump(dados_relatorio, f, indent=4, ensure_ascii=False)
        
    print(f"\n[+] Relatório exportado com sucesso para '{nome_ficheiro}'")

if __name__ == "__main__":
    executar_diagnostico()