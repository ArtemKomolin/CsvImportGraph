import json
from neo4j import GraphDatabase


#подключаемся к базе Neo4j
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("data_test", "data1234"))


#Считываем данные в нужном формате
def get_related_objects(name):
    with driver.session() as session:
        result = session.run(f"MATCH (n)-[r]->(m) WHERE n.name = {name} RETURN n, r, m", name=name)
        objects = []
        for row in result:
            objects.append({'id события': row["r"]["id"], 'ФИО участника события 1': row["n"]["name"], 'ФИО участника события 2': row["m"]["name"]})
        return objects

name = get_related_objects("'Ахромеева Алина Ивановна'")

#Создаем json файл
with open("data_j.json", "w", encoding="utf_8_sig") as f:
    json.dump(name, f, indent=4, ensure_ascii=False)