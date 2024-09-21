# SCRAPING DO LINKEDIN

## Sobre o projeto

Este repositório possui códigos python de web scraping da página de vagas do Linkedin. O objetivo é obter a descrição de vagas conforme o cargo desejado, no meu caso é Engenheiro de Dados. O framework foi Scrapy,

## Começando

### Instalação e configuração

1. Clone o repositório:

```bash
git clone https://github.com/hugoadventist/lkdn-scraping-with-scrapy.git
cd lkdn-scraping-with-scrapy
```

2. Configure a versão correto do Python com *pyenv*:

```bash
pyenv install 3.10.14
pyenv local 3.10.14
```

3. Configurar o poetry para a versão **3.10.14** e ative o ambiente virtual:

```bash
poetry env use 3.10.14
poetry shell
```

4. Instale as dependências

```bash
poetry install
```

5. Execute os testes para garantir que tudo está como esperado

```bash
task test
```

6. Execute o comando de execução da pipeline para realizar o ETL

```bash
task run
```

7. Verifique se o arquivo foi gerado corretamente.

## Contato

Para dúvidas, sugestões e feedbacks me contate:

- Hugo Riviere - eu.hugo.moraes@outlook.com