import pandas as pd
from IPython.display import display


class Tabela():
    # carregando o xlsx na memória
    dados = pd.read_excel(r"dados/owid-covid-data.xlsx")

    display(dados.info())
    print("\n")

    # deletando todas as colunas que tem todos os valores nulos
    dados = dados.dropna(how='all', axis=1)

    display(dados.info())
    print("\n")

    # armazenando as colunas a serem removidas em um array
    drop = ['iso_code', 'continent', 'location', 'new_cases_smoothed', 'new_deaths_smoothed', 'new_cases_smoothed_per_million', 'new_deaths_smoothed_per_million',
            'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units', 'total_vaccinations', 'people_vaccinated', 'population', 'population_density',
            'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
            'male_smokers', 'hospital_beds_per_thousand', 'life_expectancy', 'human_development_index', 'new_vaccinations_smoothed', 'total_vaccinations_per_hundred',
            'people_vaccinated_per_hundred', 'new_vaccinations_smoothed_per_million']

    # removendo da tabela as colunas armazenadas no array
    dados = dados.drop(columns=drop)

    display(dados.info())
    print("\n")

    # removendo os traços da coluna date
    dados['date'] = dados['date'].str.replace(r'-', '')

    # convertendo a coluna 'date' de string (object) para datetime
    dados['date'] = pd.to_datetime(
        dados['date'], format='%Y%m%d', errors='coerce')
    display(dados)
    display(dados.info())
