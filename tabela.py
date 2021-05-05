import pandas as pd
from IPython.display import display


class Tabela():
    # carregando o xlsx na memória
    dados = pd.read_excel(r"dados/owid-covid-data_IT.xlsx")
    mobi = pd.read_csv(r"dados/2020_IT_Region_Mobility_Report.csv")

    # mantendo apenas as colunas desejadas
    dados = dados[['date', 'new_cases_per_million', 'total_deaths_per_million',
                   'people_fully_vaccinated_per_hundred', 'stringency_index', 'reproduction_rate']]

    mobi = mobi[['date', 'parks_percent_change_from_baseline', 'grocery_and_pharmacy_percent_change_from_baseline',
                 'workplaces_percent_change_from_baseline']]

    # deletando todas as colunas onde todos os valores são nulos
    dados = dados.dropna(how='all', axis=1)
    mobi = mobi.dropna(how='all', axis=1)

    # deletando todas as linhas onde todos os valores são nulos
    dados = dados.dropna(how='all', axis=0)
    mobi = mobi.dropna(how='all', axis=0)

    # removendo os traços da coluna date
    dados['date'] = dados['date'].str.replace(r'-', '')
    mobi['date'] = mobi['date'].str.replace(r'-', '')

    # convertendo a coluna 'date' de string (object) para datetime
    dados['date'] = pd.to_datetime(
        dados['date'], format='%Y%m%d', errors='coerce')
    mobi['date'] = pd.to_datetime(
        mobi['date'], format='%Y%m%d', errors='coerce')

    # trocando as virgulas por pontos, para poder converter de string para float
    dados['stringency_index'] = dados['stringency_index'].str.replace(
        r',', '.')

    dados['people_fully_vaccinated_per_hundred'] = dados['people_fully_vaccinated_per_hundred'].str.replace(
        r',', '.')

    dados['total_deaths_per_million'] = dados['total_deaths_per_million'].str.replace(
        r',', '.')

    dados['new_cases_per_million'] = dados['new_cases_per_million'].str.replace(
        r',', '.')

    dados['reproduction_rate'] = dados['reproduction_rate'].str.replace(
        r',', '.')

    # convertendo as strings para float
    dados['stringency_index'] = pd.to_numeric(dados['stringency_index'])

    dados['people_fully_vaccinated_per_hundred'] = pd.to_numeric(
        dados['people_fully_vaccinated_per_hundred'])

    dados['total_deaths_per_million'] = pd.to_numeric(
        dados['total_deaths_per_million'])

    dados['new_cases_per_million'] = pd.to_numeric(
        dados['new_cases_per_million'])

    dados['reproduction_rate'] = pd.to_numeric(
        dados['reproduction_rate'])

    # substituindo os valores nulos por 0 em todas as colunas
    dados = dados.fillna(0)
