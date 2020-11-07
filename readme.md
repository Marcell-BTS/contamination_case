# Como executar o código do case

É necessário ter instalado Anaconda no sistema operacional, tal qual pode ser feito seguindo os passos do site oficial https://www.anaconda.com/products/individual 

Uma vez que o usuário Anaconda instalado e consiga criar arquivos .ipynb, seguir os passos abaixo.


## Instalação

### Instalação Global
- Abra o terminal, navegue até a pasta do projeto usando comando **cd** e execute o seguinte comando: **pip install -r requirements.txt** para instalação global.

### Instalação em Virtual Environment

Para uma instalação dentro de um virtual environment:
- Execute o comando **python3 -m pip install --user --upgrade pip** para a versão mais atualizada do pip.
- Executar o comando **python3 -m pip install --user virtualenv** para instalação do virtualenv através do pip.
- Criar um virtual environment dentro da pasta do projeto usando **python3 -m venv <nome>** com nome a escolha do usuário.
- Executar **source <nome>/bin/activate** para ativar o environment.
- Executar **pip install -r requirements.txt** para ter acesso as dependências necessárias para executar o código.

O arquivo também está disponível em HTML para consulta.

## Rodando o código
De posse do terminal (ou anaconda prompt instalado com Anaconda), navegar até a pasta do case onde está o arquivo **neoway_case.ipynb**. Executar o comando **jupyter notebook** pelo terminal.
Ou executando **Anaconda Navigador** e clicando em **Launch** no quadrante do Jupyter Notebook. Após a ação, navegar até a pasta do case e executar **neoway_case.ipynb**.