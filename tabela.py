import pandas as pd
from IPython.display import display


class Tabela():
    # carregando o xlsx na memória
    dados = pd.read_excel(r"dados/owid-covid-data.xlsx")

    # mantendo apenas as colunas desejadas
    dados = dados[['date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'new_cases_per_million', 'total_deaths_per_million', 'new_deaths_per_million',
                   'total_tests_per_thousand', 'people_fully_vaccinated', 'people_fully_vaccinated_per_hundred', 'stringency_index']]

    # deletando todas as colunas que tem todos os valores nulos
    dados = dados.dropna(how='all', axis=1)

    # deletando todas as linhas que tem todos os valores nulos
    dados = dados.dropna(how='all', axis=0)

    display(dados.info())
    print("\n")

    # removendo os traços da coluna date
    dados['date'] = dados['date'].str.replace(r'-', '')

    # convertendo a coluna 'date' de string (object) para datetime
    dados['date'] = pd.to_datetime(
        dados['date'], format='%Y%m%d', errors='coerce')

    # trocando as virgulas por pontos, para poder converter para float
    dados['stringency_index'] = dados['stringency_index'].str.replace(
        r',', '.')

    dados['people_fully_vaccinated_per_hundred'] = dados['people_fully_vaccinated_per_hundred'].str.replace(
        r',', '.')

    dados['total_tests_per_thousand'] = dados['total_tests_per_thousand'].str.replace(
        r',', '.')

    dados['new_deaths_per_million'] = dados['new_deaths_per_million'].str.replace(
        r',', '.')

    dados['total_deaths_per_million'] = dados['total_deaths_per_million'].str.replace(
        r',', '.')

    dados['new_cases_per_million'] = dados['new_cases_per_million'].str.replace(
        r',', '.')

    # convertendo as strings (object) para float
    dados['stringency_index'] = pd.to_numeric(dados['stringency_index'])

    dados['people_fully_vaccinated_per_hundred'] = pd.to_numeric(
        dados['people_fully_vaccinated_per_hundred'])

    dados['total_tests_per_thousand'] = pd.to_numeric(
        dados['total_tests_per_thousand'])

    dados['new_deaths_per_million'] = pd.to_numeric(
        dados['new_deaths_per_million'])

    dados['total_deaths_per_million'] = pd.to_numeric(
        dados['total_deaths_per_million'])

    dados['new_cases_per_million'] = pd.to_numeric(
        dados['new_cases_per_million'])

    # substituindo os valores NaN por 0
    dados['new_deaths'] = dados['new_deaths'].fillna(0)

    dados['total_deaths'] = dados['total_deaths'].fillna(0)

    dados['total_deaths'] = dados['total_deaths'].fillna(0)

    # convertendo de float para int
    dados['new_deaths'] = dados['new_deaths'].apply(int)

    dados['total_deaths'] = dados['total_deaths'].apply(int)

    dados['people_fully_vaccinated'] = dados['people_fully_vaccinated'].fillna(
        0)
    dados['people_fully_vaccinated'] = dados['people_fully_vaccinated'].apply(
        int)

    display(dados.info())
