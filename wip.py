from sqlalchemy import create_engine

engine = create_engine( # Padrão de projeto Factory
    #'sqlite://'
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db', echo=True
)

con = engine.connect()

#aqui a magia acotence 


con.close()