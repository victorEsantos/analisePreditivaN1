from pymongo import MongoClient
import random

def gerar_dados_ficticios():
    idade = random.randint(30, 80)
    sexo = random.choice(['Masculino', 'Feminino'])
    pressao_sanguinea = random.randint(90, 200)
    colesterol = random.randint(150, 350)
    acucar_no_sangue = random.choice([0, 1])
    eletrocardiograma = random.choice([0, 1, 2])
    frequencia_cardiaca_maxima = random.randint(100, 220)
    resultado = random.choice([0, 1])
    time_futebol = random.choice(['Flamengo', 'Palmeiras', 'São Paulo', 'Corinthians', 'Grêmio'])
    estado_civil = random.choice(['Solteiro', 'Casado', 'Divorciado', 'Viúvo'])
    escolaridade = random.choice(['Ensino Fundamental', 'Ensino Médio', 'Graduação', 'Pós-graduação'])
    cor_cabelo = random.choice(['Preto', 'Castanho', 'Loiro', 'Ruivo'])
    nome = "******"
    sobrenome = "******"

    if resultado == 1:
        angina_induzida_por_exercicio = random.choices([0, 1], weights=[30, 70])[0]
    else:
        angina_induzida_por_exercicio = random.choice([0, 1])

    dados = {
        'Nome': nome,
        'Sobrenome': sobrenome,
        'Idade': idade,
        'Sexo': sexo,
        'Pressao_Sanguinea': pressao_sanguinea,
        'Colesterol': colesterol,
        'Açúcar_no_Sangue_em_Jejum': acucar_no_sangue,
        'Eletrocardiograma': eletrocardiograma,
        'Frequencia_Cardiaca_Maxima': frequencia_cardiaca_maxima,
        'Angina_Induzida_por_Exercício': angina_induzida_por_exercicio,
        'Resultado': resultado,
        'Time_Futebol': time_futebol,
        'Estado_Civil': estado_civil,
        'Escolaridade': escolaridade,
        'Cor_Cabelo': cor_cabelo
    }

    return dados

if __name__ == '__main__':
    client = MongoClient(
        "mongodb+srv://victor:*****@cluster0.pp6scwg.mongodb.net/?retryWrites=true&w=majority")

    db = client.get_database('Cluster0')
    collection = db.mycollection

    num_registros = 500

    # Lista para armazenar os registros de pacientes
    data_to_insert = []

    # Gerar registros aleatórios usando um loop for
    for i in range(num_registros):
        paciente = gerar_dados_ficticios()
        data_to_insert.append(paciente)


    # Inserir dados na coleção
    inserted_data = collection.insert_many(data_to_insert)

    # Verificar se a inserção foi bem-sucedida
    if inserted_data.acknowledged:
        print("Dados inseridos com sucesso. ID:", inserted_data)
    else:
        print("Falha ao inserir dados.")

    # Fechar a conexão com o MongoDB

    print(list(collection.find()))

    client.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
