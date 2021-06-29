------检查gds的安装情况-----

RETURN gds.version()

CALL gds.list()

----neovis初始化----


LOAD CSV WITH HEADERS FROM "https://raw.hee.ink/mathbeveridge/asoiaf/master/data/asoiaf-all-edges.csv" AS row
MERGE (src:Character {name: row.Source})
MERGE (tgt:Character {name: row.Target})
MERGE (src)-[r:INTERACTS]->(tgt) ON CREATE SET r.weight = toInteger(row.weight)

---PageRank算法执行---


