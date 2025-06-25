from sqlalchemy import create_engine, text

engine = create_engine( # Padrão de projeto Factory
    #'sqlite://'
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db', echo=True
)

with  engine.connect() as con:
    #aqui a magia acotence, com begin conseguimos garantir a ACID, se der ruim faz rollback
    with engine.begin():
        sql = text('SELECT id, name, comment FROM public.comments;')
        result = con.execute(sql)
        print(result.fetchall())
con.close()