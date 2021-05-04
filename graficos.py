from tabela import *
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns


class Graficos():
    dados = Tabela().dados
    mobi = Tabela().mobi

    # renomeando labels
    dados = dados.rename(
        {'people_fully_vaccinated_per_hundred': 'vac_100', 'new_cases_per_million': 'novos_casos_milhao',
         'total_deaths_per_million': 'mortes_milhao', 'stringency_index': 'contingencia', 'reproduction_rate': 'reprod_virus'}, axis='columns')

    mobi = mobi.rename(
        {'parks_percent_change_from_baseline': 'parques', 'grocery_and_pharmacy_percent_change_from_baseline': 'mercado_e_farmacias',
         'workplaces_percent_change_from_baseline': 'trabalho'}, axis='columns')

    # plotando histogramas de mobilidade

    dados['contingencia'].plot(kind='hist', subplots=True, sharex=True,
                               sharey=True, title='Índice de Contingência')
    plt.show()

    mobi['parques'].plot(kind='hist', subplots=True, sharex=True,
                         sharey=True, title='Mobilidade Parques')
    plt.show()

    mobi['mercado_e_farmacias'].plot(kind='hist', subplots=True, sharex=True,
                                     sharey=True, title='Mobilidade Mercado e Farmácias ')
    plt.show()

    mobi['trabalho'].plot(kind='hist', subplots=True, sharex=True,
                          sharey=True, title='Mobilidade Trabalho')
    plt.show()

    # gráficos de dispersão

    sns.scatterplot(data=dados, x=dados['vac_100'],
                    y="novos_casos_milhao", palette="deep", sizes=(20, 200))
    plt.show()

    sns.scatterplot(data=dados, x=dados['vac_100'],
                    y="mortes_milhao", palette="deep", sizes=(20, 200))
    plt.show()

    sns.scatterplot(data=dados, x=dados['vac_100'],
                    y="reprod_virus", palette="deep", sizes=(20, 200))
    plt.show()

    # plotando mapa de calor

    sns.heatmap(dados.corr(), cmap='Wistia', annot=True)
    plt.show()

    # preparação do modelo para o treinamento

    y = dados['vac_100']
    X = dados[['reprod_virus']]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)

    # regressão linear

    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)

    # regressão floresta aleatória

    rf_reg = RandomForestRegressor()
    rf_reg.fit(X_train, y_train)

    test_pred_lin = lin_reg.predict(X_test)
    test_pred_rf = rf_reg.predict(X_test)

    r2_lin = metrics.r2_score(y_test, test_pred_lin)
    mse_lin = metrics.mean_squared_error(y_test, test_pred_lin)
    display(f"R² da Regressão Linear: {r2_lin}")
    display(f"MSE da Regressão Linear: {mse_lin}")
    r2_rf = metrics.r2_score(y_test, test_pred_rf)
    mse_rf = metrics.mean_squared_error(y_test, test_pred_rf)
    display(f"R² do Random Forest: {r2_rf}")
    display(f"MSE do Random Forest: {mse_rf}")

    LinearRegression(copy_X=True, fit_intercept=True,
                     n_jobs=None, normalize=False)
    display('R² real = {}'.format(lin_reg.score(X_train, y_train)))

    # exibindo as previsões

    dados_resultado = pd.DataFrame()
    dados_resultado['Dados reais de teste'] = y_test
    dados_resultado['Previsão floresta aleatória'] = test_pred_rf
    dados_resultado['Previsão da regressão linear'] = test_pred_lin
    dados_resultado = dados_resultado.reset_index(drop=True)

    plt.figure(figsize=(15, 5))
    sns.lineplot(data=dados_resultado)
    plt.show()
