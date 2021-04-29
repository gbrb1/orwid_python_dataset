import pyautogui as auto
import pandas as pd
import openpyxl
from IPython.display import display


def main():
    # carregando o xlsx na memória
    data = pd.read_excel(r"dados/owid-covid-data.xlsx")

    display(data.info())
    print("\n")

    # deletando todas as colunas que tem todos os valores nulos
    data = data.dropna(how='all', axis=1)

    display(data.info())
    print("\n")

    # armazenando as colunas a serem removidas em um array
    drop = ['iso_code', 'continent', 'location', 'new_cases_smoothed', 'new_deaths_smoothed', 'new_cases_smoothed_per_million', 'new_deaths_smoothed_per_million',
            'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units', 'total_vaccinations', 'people_vaccinated', 'population', 'population_density',
            'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
            'male_smokers', 'hospital_beds_per_thousand', 'life_expectancy', 'human_development_index', 'new_vaccinations_smoothed', 'total_vaccinations_per_hundred',
            'people_vaccinated_per_hundred', 'new_vaccinations_smoothed_per_million']

    # removendo da tabela as colunas armazenadas no array
    data = data.drop(columns=drop)

    display(data.info())
    print("\n")
    # toDo(converter strings para int/float)


if __name__ == "__main__":
    main()
