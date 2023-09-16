import pandas as pd
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

if __name__ == '__main__':

    client = MongoClient(
        "mongodb+srv://victor:****@cluster0.pp6scwg.mongodb.net/?retryWrites=true&w=majority")

    db = client.get_database('Cluster0')
    collection = db.mycollection

    dados_pacientes = list(collection.find());

    # Converter a lista de dicionários em um DataFrame pandas
    data = pd.DataFrame(dados_pacientes)

    # Selecionar recursos (campos) e rótulo (classe)
    features = ['Idade', 'Sexo', 'Pressao_Sanguinea', 'Colesterol', 'Açúcar_no_Sangue_em_Jejum', 'Frequencia_Cardiaca_Maxima', 'Angina_Induzida_por_Exercício']
    label = 'Resultado'

    X = data[features]
    y = data[label]

    # Pré-processamento dos dados (tratamento de variáveis categóricas)
    X = pd.get_dummies(X, columns=['Sexo'], drop_first=True)

    # Dividir o conjunto de dados em treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Criar um classificador de Árvore de Decisão
    classifier = DecisionTreeClassifier()

    # Treinar o classificador
    classifier.fit(X_train, y_train)

    # Fazer previsões no conjunto de teste
    y_pred = classifier.predict(X_test)

    # Calcular a precisão do modelo
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Acurácia do modelo: {accuracy:.2f}')

    novo_paciente = {
        'Idade': 55,
        'Sexo': 'Masculino',
        'Pressao_Sanguinea': 140,
        'Colesterol': 200,
        'Açúcar_no_Sangue_em_Jejum': 1,
        'Eletrocardiograma': 0,
        'Frequencia_Cardiaca_Maxima': 160,
        'Angina_Induzida_por_Exercício': 0,
    }
