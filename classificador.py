import pandas as pd
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt


if __name__ == '__main__':

    client = MongoClient(
        "mongodb+srv://victor:AAAAAAA@cluster0.4m70ehm.mongodb.net/?retryWrites=true&w=majority")

    db = client.get_database('Cluster0')
    collection = db.mycollection2

    dados_pacientes = list(collection.find())

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
    print(f'01) Acurácia do modelo: {accuracy:.2f}')

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

    # Referencias:
    # https://www.flai.com.br/juscudilio/como-calcular-as-metricas-de-validacao-dos-modelos-de-machine-learning-em-python/

    conf_matrix = confusion_matrix(y_test, y_pred)
    print("")
    print("02) Matriz de Confusão:")
    print("TP FP")
    print("FN TN")
    print(conf_matrix)

    # Calcular as probabilidades das previsões para calcular a Curva ROC
    y_probs = classifier.predict_proba(X_test)[:, 1]

    # Calcular a Curva ROC
    fpr, tpr, thresholds = roc_curve(y_test, y_probs)

    # Calcular a área sob a curva ROC (AUC)
    roc_auc = roc_auc_score(y_test, y_probs)
    print("")
    print(f"03) Curva ROC: {roc_auc:.2f}")

    # Plotar grafico
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
    plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label='Aleatório')
    plt.xlabel('Taxa de Falsos Positivos')
    plt.ylabel('Taxa de Verdadeiros Positivos')
    plt.title('Curva ROC')
    plt.legend()
    plt.show()
