import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def get_env_var(var_name: str) -> str:
    # Exemplo: usando os.environ para ler variáveis de ambiente
    import os
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Variável de ambiente '{var_name}' não encontrada.")
    return value

