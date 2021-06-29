FROM neo4j:latest

ENV NEO4J_AUTH=neo4j/password
ENV NEO4J_dbms_memory_pagecache_size=1G
ENV NEO4J_dbms.memory.heap.initial_size=1G
ENV NEO4J_dbms_memory_heap_max__size=1G
ENV NEO4J_dbms_security_procedures_unrestricted=gds.*
ENV NEO4J_dbms_security_procedures_allowlist=gds.*
ENV NEO4j_dbms.default_listen_address=0.0.0.0.
# RUN curl --fail --output /tmp/movies.cypher https://raw.githubusercontent.com/neo4j-graph-examples/movies/8508a527d8aa1c261b0978d1d5b3156d4ac8328e/scripts/import.cypher

# RUN neo4j-e2e cypher-shell -u neo4j -p abcde --file /movies/movies.cypher
COPY ./neo4j-graph-data-science-1.6.1.jar /var/lib/neo4j/plugins/