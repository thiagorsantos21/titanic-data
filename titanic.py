import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic-data-6.csv")
#Limpando os dados

# Prenchendo valores faltantes com a média, neste caso das idades
am = df['Age'].mean()
df['Age'].fillna(am,inplace=True)

#Ajustando cabines que estão nulas para N/I
df['Cabin'].fillna('N/I',inplace=True)

#Assumimos que embarques que não estejam marcados, aconteceram em Southampton
df['Embarked'].fillna('S',inplace=True)

#Não há dados duplicados


"""
    Função que calcula Média

    INPUT:
    df: dataframe que será utilizada
    column: str. Nome da coluna que será realizada query
    result_col: str. Nome da coluna a qual a média será calculada
    parameter: str. Parâmetro que será utilizado na condição da query

    OUTPUT:
    Imprimi a média da coluna solicitada de acordo com o parametro informado
"""
def calcula_media(df, column, result_col, parameter):
    return round(df.query("{} == {}".format(column,parameter))[result_col].mean(),2)


idade_media_sobreviventes = calcula_media(df,"Survived","Age",1)
idade_media_nao_sobreviventes = calcula_media(df,"Survived","Age",0)


print("Estudo sobre Titanic")

total_passageiros = df["PassengerId"].count()
sobreviventes = df.query("Survived == '1'")["PassengerId"].count()
nao_sobreviventes = df.query("Survived == '0'")["PassengerId"].count()


print("Para o estudo possuímos dados de {} passageiros".format(total_passageiros))
print("Destes {} sobreviveram e {} não sobreviveram o acidente".format(sobreviventes,nao_sobreviventes))

#Gráfico de barras
locations = [1, 2]
heights = [sobreviventes, nao_sobreviventes]
labels = ['Sobreviventes', 'Não Sobreviventes']
plt.bar(locations, heights, tick_label=labels)
plt.title('Estudo de Dados sobre Titanic')
plt.show(block=True)

print("A idade média dos sobreviventes é de {}".format(idade_media_sobreviventes))
print("A idade média dos não sobreviventes é de {}".format(idade_media_nao_sobreviventes))

df_survivals = df.query("Survived == 1")

df_survivals.groupby(['Pclass'])['PassengerId'].plot(kind="bar", title="Sobreviventes por Classe");

#Gráfico de barras com quantidade de sobreviventes por classes
