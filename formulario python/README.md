# Sistema de Pontos de Acupuntura

Este é um sistema para gerenciar pontos de acupuntura, permitindo carregar, editar e salvar dados em formato JSON.

## Requisitos

- Python 3.x
- ttkbootstrap
- Pillow

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Instale as dependências:
    ```sh
    pip install ttkbootstrap Pillow
    ```

## Uso

1. Execute o arquivo `app.py` para iniciar a aplicação:
    ```sh
    python app.py
    ```

2. Use a interface gráfica para carregar um arquivo JSON, adicionar novos pontos de acupuntura, editar pontos existentes e salvar os dados.

## Estrutura do Projeto

- `app.py`: Ponto de entrada da aplicação.
- `gui.py`: Contém a classe principal da interface gráfica.
- `menu.py`: Define o menu da aplicação.
- `janela_edicao.py`: Contém a janela de edição/adicionar ponto.
- `utils.py`: Funções utilitárias para carregar e salvar dados JSON.
- `abas.py`: Funções para manipular a interface de resultados.

## Estrutura do JSON

O arquivo JSON deve seguir a estrutura abaixo:

```json
{
    "pontos_acupuntura": {
        "regiao": [
            {
                "nome": "Nome do Ponto",
                "codigo": "Código do Ponto",
                "localizacao": "Localização do Ponto",
                "funcoes": ["Função 1", "Função 2"],
                "precaucoes": ["Precaução 1"],
                "imagem": "caminho/para/imagem.png",
                "regiao": "regiao"
            }
        ]
    }
}
```

## Testes

Cada módulo contém uma seção de testes que pode ser executada individualmente para verificar o funcionamento das funções.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.