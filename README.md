# Mini Projetos em Python

Repositório com pequenos projetos desenvolvidos para praticar lógica de programação e construir meu portfólio no GitHub.

Cada exercício aborda um problema simples e apresenta, de forma incremental, conceitos importantes da linguagem Python. O repositório também inclui exemplos com Docker e uma aplicação web com Flask e SQLite.

## Projetos

| Projeto | Descrição | Conceitos praticados |
| --- | --- | --- |
| [Exercício 01 - Temperatura](exercicio-01-temperatura.py) | Classifica uma temperatura em Celsius como fria, agradável ou quente. | Entrada de dados, conversão de tipos e estruturas condicionais |
| [Exercício 02 - Tempo](exercicio-02-tempo.py) | Calcula a média de cinco tempos e conta quantos ultrapassaram 100 milissegundos. | Laços de repetição, acumuladores, condicionais e f-strings |
| [Exercício 03 - Função](exercicio-03-funcao.py) | Calcula a duração de um conteúdo de acordo com sua velocidade de reprodução. | Funções, parâmetros, retorno de múltiplos valores e formatação numérica |
| [Minha Prática 01 - Divisão](minha-pratica-01.py) | Realiza uma divisão inteira entre dois números e exibe o quociente e o resto. | Entrada de dados, conversão de tipos, `divmod()` e acesso a tuplas |
| [Exercício 04 - Verificador de Senha](exercicio-04-verifica-senha.py) | Verifica se uma senha possui pelo menos oito caracteres, uma letra maiúscula e um número. | Laços de repetição, condicionais, valores booleanos e métodos de string |
| [Exercício 05 - Verifica Compra](exercicio-05-verfica-compra.py) | Calcula o valor final de uma compra com desconto por faixa de valor e desconto adicional no Pix. | Condicionais, porcentagens, operações aritméticas e métodos de string |
| [Exercício 06 - Cadastro de Despesas](exercicio-06-while-cadastro-despesas.py) | Registra despesas até receber zero e exibe a quantidade, o maior valor e o total cadastrado. | Laço `while`, `break`, contadores, acumuladores e condicionais |
| [Exercício 07 - Cálculo de Viagem](exercicio-07-calculo-viagem.py) | Calcula os litros de combustível necessários e o custo do combustível para uma viagem. | Funções, parâmetros, retorno de múltiplos valores, operações aritméticas e formatação numérica |
| [Exercício 08 - Listas e Estoque](exercicio-08-listas.py) | Soma as unidades em estoque e identifica as posições dos produtos com menos de cinco unidades para reposição. | Listas, `enumerate()`, `append()`, `len()`, laço `for` e acumuladores |
| [Aplicações com Docker](Docker/) | Executa duas aplicações Python simples dentro de um contêiner. | Dockerfile, imagens, contêineres, `ENTRYPOINT` e `CMD` |
| [Atividade Docker - Cadastro de Itens](Atividade-Docker/) | Aplicação web para adicionar e listar itens armazenados em SQLite. | Flask, rotas GET/POST, formulários, SQLite, variáveis de ambiente e volumes Docker |

## Como executar

### Pré-requisitos

- Python 3 instalado
- Um terminal ou editor de código
- Git instalado (para clonar o repositório)
- Docker instalado e em execução (para os exemplos em contêineres)

Os exercícios da raiz usam apenas a biblioteca padrão do Python. A aplicação da pasta `Atividade-Docker` depende do Flask.

Clone este repositório e acesse a pasta:

```bash
git clone <URL_DO_REPOSITORIO>
cd 10-MINI-PROJETOS
```

Execute qualquer projeto com o comando:

```bash
python exercicio-01-temperatura.py
python exercicio-02-tempo.py
python exercicio-03-funcao.py
python minha-pratica-01.py
python exercicio-04-verifica-senha.py
python exercicio-05-verfica-compra.py
python exercicio-06-while-cadastro-despesas.py
python exercicio-07-calculo-viagem.py
python exercicio-08-listas.py
```

A maioria dos exercícios solicita os dados diretamente pelo terminal. Os exercícios 03 e 08 usam valores definidos nos próprios arquivos: o exercício 03 calcula a duração de 120 minutos com velocidade de reprodução de 2 vezes; o exercício 08 analisa o estoque `[12, 3, 0, 8, 2]`.

No exercício 05, compras a partir de R$ 300 recebem 10% de desconto; compras a partir de R$ 150 e abaixo de R$ 300 recebem 5%. Abaixo de R$ 150, não há desconto por valor. O pagamento por Pix aplica mais 2% sobre o total já descontado.

No exercício 06, digite `0` para encerrar o cadastro e exibir o resumo das despesas. Esse valor não entra na contagem.

No exercício 07, informe a distância em quilômetros, o consumo em km/l e o preço do combustível por litro. O consumo deve ser maior que zero. O custo calculado considera apenas o combustível.

No exercício 08, as posições dos produtos começam em 1. Com o estoque do exemplo, o resultado é de 25 unidades no total e três produtos para reposição, nas posições `[2, 3, 5]`.

### Executar com Docker

Crie a imagem a partir da raiz do repositório:

```bash
docker build -t mini-projetos-python ./Docker
```

Execute a aplicação padrão (`app.py`):

```bash
docker run --rm mini-projetos-python
```

Para executar a segunda aplicação (`app2.py`), substitua o argumento padrão:

```bash
docker run --rm mini-projetos-python app2.py
```

### Executar a atividade com Flask e SQLite

Na raiz do repositório, crie a imagem e execute o contêiner:

```bash
docker build -t atividade-docker ./Atividade-Docker
docker run --rm -p 3000:3000 -v atividade-dados:/data atividade-docker
```

Acesse [http://localhost:3000](http://localhost:3000) no navegador para adicionar e listar itens. O banco fica em `/data/app.db`, conforme a variável `DB_PATH` definida no Dockerfile. O volume `atividade-dados` mantém os registros entre execuções do contêiner.

Para executar localmente, sem Docker:

```bash
cd Atividade-Docker
python -m pip install -r requirements.txt
python app.py
```

A aplicação também fica disponível em [http://localhost:3000](http://localhost:3000). Sem configurar `DB_PATH`, o banco é criado em `data/app.db`, relativo à pasta de execução. Use `Ctrl+C` no terminal para encerrar a aplicação.

## Objetivos

- Praticar os fundamentos da programação com Python.
- Desenvolver o raciocínio lógico por meio de problemas pequenos.
- Registrar minha evolução em programação.
- Organizar projetos para compor meu portfólio profissional.

## Próximos passos

Este repositório será atualizado com novos mini projetos, explorando temas como:

- Modularização e reaproveitamento de código;
- Aprofundamento em listas, dicionários e outras estruturas de dados;
- Tratamento de erros;
- Leitura e gravação de arquivos;
- Projetos com interfaces e integração com APIs;
- Aprofundamento em Docker e conteinerização.

## Autor

Desenvolvido por **Aender** como parte da minha jornada de aprendizado em programação.
