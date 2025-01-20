import os
import json

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)

def generate_project_structure():
    # Project root
    root = "rag-knowledge-tracker"
    create_directory(root)

    # Root level files
    gitignore_content = """
# Python
__pycache__/
*.py[cod]
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Node
node_modules/
npm-debug.log
yarn-debug.log
yarn-error.log

# Environment
.env
.venv
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.idea/
.vscode/
*.swp
*.swo

# Operating System
.DS_Store
Thumbs.db
"""

    requirements_content = """
fastapi==0.109.1
uvicorn==0.27.0
python-multipart==0.0.6
sqlalchemy==2.0.25
alembic==1.13.1
snowflake-connector-python==3.6.0
python-jose==3.3.0
passlib==1.7.4
pydantic==2.6.0
python-dotenv==1.0.0
"""

    docker_compose_content = """
version: '3.8'

services:
  backend:
    build:
      context: .
      dockerfile: deploy/docker/backend.Dockerfile
    ports:
      - "8000:8000"
    environment:
      - SNOWFLAKE_ACCOUNT=${SNOWFLAKE_ACCOUNT}
      - SNOWFLAKE_USER=${SNOWFLAKE_USER}
      - SNOWFLAKE_PASSWORD=${SNOWFLAKE_PASSWORD}
    volumes:
      - ./backend:/app/backend

  frontend:
    build:
      context: .
      dockerfile: deploy/docker/frontend.Dockerfile
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app/frontend
    depends_on:
      - backend
"""

    files = {
        f"{root}/.gitignore": gitignore_content,
        f"{root}/README.md": "# RAG Knowledge Tracker\n\nDocument tracking and knowledge management system using RAG.",
        f"{root}/requirements.txt": requirements_content,
        f"{root}/docker-compose.yml": docker_compose_content
    }

    for file_path, content in files.items():
        create_file(file_path, content)

    # Backend structure
    backend_dirs = [
        f"{root}/backend/app/api/routes",
        f"{root}/backend/app/api/models",
        f"{root}/backend/app/services",
        f"{root}/backend/app/utils",
        f"{root}/backend/tests",
        f"{root}/backend/alembic/versions",
    ]

    for dir_path in backend_dirs:
        create_directory(dir_path)

    # Backend files
    backend_files = {
        f"{root}/backend/app/main.py": """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "RAG Knowledge Tracker API"}
""",
        f"{root}/backend/app/config.py": """
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    snowflake_account: str
    snowflake_user: str
    snowflake_password: str
    
    class Config:
        env_file = ".env"

settings = Settings()
"""
    }

    for file_path, content in backend_files.items():
        create_file(file_path, content)

    # Frontend structure
    frontend_dirs = [
        f"{root}/frontend/src/components",
        f"{root}/frontend/src/hooks",
        f"{root}/frontend/src/services",
        f"{root}/frontend/src/utils",
        f"{root}/frontend/public",
    ]

    for dir_path in frontend_dirs:
        create_directory(dir_path)

    # Package.json
    package_json = {
        "name": "rag-knowledge-tracker",
        "version": "0.1.0",
        "private": True,
        "dependencies": {
            "react": "^18.2.0",
            "react-dom": "^18.2.0",
            "@tanstack/react-query": "^5.17.9",
            "axios": "^1.6.5",
            "lucide-react": "^0.263.1",
            "tailwindcss": "^3.4.1",
            "@radix-ui/react-slot": "^1.0.2"
        },
        "scripts": {
            "dev": "vite",
            "build": "vite build",
            "preview": "vite preview"
        },
        "devDependencies": {
            "@vitejs/plugin-react": "^4.2.1",
            "vite": "^5.0.12"
        }
    }

    create_file(f"{root}/frontend/package.json", json.dumps(package_json, indent=2))

    # Frontend files
    frontend_files = {
        f"{root}/frontend/src/App.jsx": """
import React from 'react';
import DocumentUpload from './components/DocumentUpload';
import KnowledgeAssessment from './components/KnowledgeAssessment';
import NovelInformation from './components/NovelInformation';
import KnownInformation from './components/KnownInformation';
import DeepDive from './components/DeepDive';
import TopicTracking from './components/TopicTracking';

function App() {
  return (
    <div className="container mx-auto px-4">
      <h1 className="text-3xl font-bold my-8">RAG Knowledge Tracker</h1>
      <DocumentUpload />
      <KnowledgeAssessment />
      <NovelInformation />
      <KnownInformation />
      <TopicTracking />
    </div>
  );
}

export default App;
""",
        f"{root}/frontend/src/main.jsx": """
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
"""
    }

    for file_path, content in frontend_files.items():
        create_file(file_path, content)

    # Snowflake structure
    snowflake_dirs = [
        f"{root}/snowflake/init",
        f"{root}/snowflake/procedures",
    ]

    for dir_path in snowflake_dirs:
        create_directory(dir_path)

    # Create main SQL files
    snowflake_files = {
        f"{root}/snowflake/init/01_create_tables.sql": """
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
""",
        f"{root}/snowflake/procedures/vector_search.sql": """
CREATE OR REPLACE FUNCTION vector_similarity(v1 ARRAY, v2 ARRAY)
RETURNS FLOAT
AS 'SELECT CAST(DOT_PRODUCT(v1, v2) / (SQRT(DOT_PRODUCT(v1, v1)) * SQRT(DOT_PRODUCT(v2, v2))) AS FLOAT)';
"""
    }

    for file_path, content in snowflake_files.items():
        create_file(file_path, content)

    # Deployment structure
    deploy_dirs = [
        f"{root}/deploy/docker",
        f"{root}/deploy/k8s",
    ]

    for dir_path in deploy_dirs:
        create_directory(dir_path)

    # Create Dockerfiles
    dockerfile_backend = """
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ backend/

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

    dockerfile_frontend = """
FROM node:18-alpine

WORKDIR /app

COPY frontend/package*.json ./

RUN npm install

COPY frontend/ .

CMD ["npm", "run", "dev"]
"""

    create_file(f"{root}/deploy/docker/backend.Dockerfile", dockerfile_backend)
    create_file(f"{root}/deploy/docker/frontend.Dockerfile", dockerfile_frontend)

    print(f"Project structure created in directory: {root}")

if __name__ == "__main__":
    generate_project_structure()
