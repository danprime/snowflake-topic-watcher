
CREATE TABLE documents (
    document_id VARCHAR NOT NULL PRIMARY KEY,
    title VARCHAR,
    source_url VARCHAR,
    document_type VARCHAR,
    content TEXT,
    created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE document_chunks (
    chunk_id VARCHAR NOT NULL PRIMARY KEY,
    document_id VARCHAR REFERENCES documents(document_id),
    chunk_text TEXT,
    chunk_embedding ARRAY,
    created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE knowledge_state (
    chunk_id VARCHAR NOT NULL PRIMARY KEY REFERENCES document_chunks(chunk_id),
    knowledge_state VARCHAR,
    confidence_score FLOAT,
    last_assessed TIMESTAMP_NTZ,
    created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);
