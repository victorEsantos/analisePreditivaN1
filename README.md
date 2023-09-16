Alunos: Alexandre Grawe e Victor Santos

1.Banco de Dados NoSQL(5,0).

a)Justificar a escolha do modelo NoSQL

Utilizamos um banco de dados NoSql por se tratar de um banco com boa capacidade de disponibilidade, sem locks, ao contrário do que em bancos ACID, a consistência eventual dos dados não é um problema.


b)   Disponibilizar para AP, Data Warehouse ou Data Lake ou Data Lakehouse.

Nossa base de dados está hospedada via mongoDB Atlas

OBS.: O projeto não irá rodar normalmente se nao colocar a senha correta na url de acesso ao mongo


EXEMPLO DO FORMATO DOS DADOS:

```
{
   "_id":{
      "$oid":"6506161af12ebf30add30e0f"
   },
   "Nome":"******",
   "Sobrenome":"******",
   "Idade":{
      "$numberInt":"64"
   },
   "Sexo":"Feminino",
   "Pressao_Sanguinea":{
      "$numberInt":"125"
   },
   "Colesterol":{
      "$numberInt":"216"
   },
   "Açúcar_no_Sangue_em_Jejum":{
      "$numberInt":"1"
   },
   "Eletrocardiograma":{
      "$numberInt":"2"
   },
   "Frequencia_Cardiaca_Maxima":{
      "$numberInt":"107"
   },
   "Angina_Induzida_por_Exercício":{
      "$numberInt":"1"
   },
   "Resultado":{
      "$numberInt":"0"
   },
   "Time_Futebol":"Flamengo",
   "Estado_Civil":"Casado",
   "Escolaridade":"Ensino Fundamental",
   "Cor_Cabelo":"Loiro"
}
```
