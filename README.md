# 🐧 LinuxNetOps-Diagnostics: Automated Network & System Diagnostics Suite

Repositório de engenharia desenvolvido para automatizar diagnósticos de rede e validação de infraestruturas em ambientes Linux e Cloud, utilizando Python e bibliotecas nativas para auditoria rápida e exportação de dados estruturados.

## 🚀 Arquitetura e Funcionalidades

Este projeto implementa ferramentas essenciais de diagnóstico para SysAdmins e Engenheiros de Redes, destacando-se pelas seguintes capacidades:

* **Conectividade Multi-Endpoint Dinâmica:** Execução automatizada de testes de ping adaptados ao sistema operativo (compatível com Linux `-c` e Windows `-n`) para validação de gateways e DNS públicos.
* **Auditoria de Portas TCP Críticas:** Verificação de socket em portas essenciais (como DNS `53`, HTTP `80`, e HTTPS `443`) com tratamento robusto de exceções e timeouts.
* **Exportação de Relatórios Estruturados (JSON):** Registo automático das métricas de diagnóstico com *timestamps* detalhados, facilitando a integração com pipelines de monitorização ou ferramentas de análise de logs.

---

## 📂 Estrutura do Projeto

```text
LinuxNetOps-Diagnostics/
│
├── diagnostico_rede.py          # Script principal de automação e testes
└── relatorio_diagnostico.json   # Relatório estruturado gerado pelo script
⚙️ Pré-requisitos e Execução
Para executar este script no teu ambiente local:

Certifica-te de que tens o Python instalado.

Clona o repositório ou descarrega o script para a tua máquina.

Executa o script através do terminal:

Bash
python diagnostico_rede.py
Projeto desenvolvido no âmbito da automação de redes e administração de sistemas Linux / Cloud.
