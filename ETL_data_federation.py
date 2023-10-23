from pymongo import MongoClient

if __name__ == '__main__':

    # Pega os dados do cluster0 + cluster1 com data federation, os dois clusters foram aglutinados
    client_federation = MongoClient(
        "mongodb://victor:********@federateddatabaseinstance0-8emaq.a.query.mongodb.net/?ssl=true&authSource=admin")

    db_federation = client_federation.get_database('VirtualDatabase0')
    collection = db_federation.VirtualCollection0

    dados_pacientes = list(collection.find())

    #Realizar ETL tratativa dos dados brutos

    for paciente in dados_pacientes:
        paciente['Nome'] = '*******'
        paciente['Sobrenome'] = '*******'
        del paciente['Time_Futebol']
        del paciente['Estado_Civil']
        del paciente['Escolaridade']
        del paciente['Cor_Cabelo']

    #Inserir dados após o ETL feito
    client = MongoClient(
        "mongodb+srv://victor:*******@cluster1.8emaq.mongodb.net/?retryWrites=true&w=majority")

    db = client.get_database('Cluster1')
    collection = db.mycollectionFeitoETL

    collection.insert_many(dados_pacientes)