import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.model_selection import cross_val_score

import warnings
warnings.filterwarnings('ignore')

def rename_category(df, columns, sufix):   
    """ 
    Inclui o sufixo desejado nas variáveis categóricas.
    
    df: Dataframe para modificação.
    columns: Colunas para serem binarizadas. 
    sufix: Sufixo para ser incluido nas variáveis categórias. Precisa ser uma string. 
    """
    df = df.dropna() # Exclui quaisquer nan's

    for column in columns:
        column_values = df[column].unique() # Resgata as categorias de cada variável categórica.

        for values in column_values:
            df[column] = df[column].replace(values, values+sufix) # Aplica o sufixo desejado.
            
    return df
    

    
def one_hot_encoder(df, columns):
    """
    Retorna Dataframe com as variáveis categóricas binarizadas.
    
    df: Dataframe para alteração.
    columns: Colunas para serem binarizadas.
    """

    for column in columns:
        df = pd.concat([df, pd.get_dummies(df[column])], axis=1) # Concatena o dataframe com variáveis binarizadas.
        df.drop(column, axis=1, inplace=True) # Exclui a variável original.
    
    return df
    
    

    
def plotting_categories(df, column):
    """
    Exibe as distribuições de cada categoria da variável de interesse em relação ao target "prob_V1_V2".
    df: Dataframe de interesse.
    column: Variável de interesse.
    """
    categories = df[column].unique()
    
    for category in categories:
        series_to_plot = df[df[column]==category]['prob_V1_V2']
        sns.distplot(series_to_plot, hist=False, label=category)
    
    
    
def rmse_cv(model, cv):
    
    """
    Retorna o RMSE dos Dataset de teste e treino.
    
    model: Objeto do modelo treinado.
    cv: Número 'k' de K-Fold Cross-Validation
    """
    
    scorer = make_scorer(mean_squared_error, greater_is_better = False)     
    rmse_train = np.sqrt(-cross_val_score(model, X_train,
                                          y_train, scoring = scorer, cv = cv)) # Calcula o RMSE do dataset de treino.    
    rmse_test = np.sqrt(-cross_val_score(model, X_test,
                                         y_test, scoring = scorer, cv = cv)) # Calcula o RMSE do dataset de teste.
    
    return(print("RMSE do Dataset de Treino :", rmse_train.mean(),"\n" "RMSE do Dataset de Teste :", rmse_test.mean()))