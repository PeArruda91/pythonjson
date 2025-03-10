import json
from ttkbootstrap.dialogs import Messagebox

def carregar_dados(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            if 'pontos_acupuntura' not in dados:
                Messagebox.show_error("Erro", "Estrutura do JSON inválida!")
                return None
            return dados
    except FileNotFoundError:
        Messagebox.show_error("Erro", "Arquivo não encontrado!")
        return None
    except json.JSONDecodeError:
        Messagebox.show_error("Erro", "Formato JSON inválido!")
        return None
    except Exception as e:
        Messagebox.show_error("Erro", f"Erro inesperado: {str(e)}")
        return None

def salvar_dados(caminho, dados):
    try:
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
    except Exception as e:
        Messagebox.show_error("Erro", f"Erro ao salvar dados: {str(e)}")

# Testes
if __name__ == "__main__":
    dados_teste = {
        "pontos_acupuntura": {
            "cabeca": [
                {
                    "nome": "Ponto 1",
                    "codigo": "P1",
                    "localizacao": "Cabeça",
                    "funcoes": ["Função 1", "Função 2"],
                    "precaucoes": ["Precaução 1"],
                    "imagem": "caminho/para/imagem.png",
                    "regiao": "cabeca"
                }
            ]
        }
    }
    
    caminho_teste = "dados_teste.json"
    salvar_dados(caminho_teste, dados_teste)
    dados_carregados = carregar_dados(caminho_teste)
    
    assert dados_carregados == dados_teste, "Dados carregados não correspondem aos dados salvos"
    print("Teste de carregar_dados e salvar_dados passou!")
