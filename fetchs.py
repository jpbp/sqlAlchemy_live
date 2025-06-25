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
        print(result.fetchone(),'pega o primeiro')
        
    with engine.begin():
        sql = text('SELECT id, name, comment FROM public.comments;')
        result = con.execute(sql)
        print(result.fetchmany(3),'pega alguns valores')
        print(result.partitions(3),'pega alguns valores')
        
    with engine.begin():
        sql = text('SELECT id, name, comment FROM public.comments;')
        result = con.execute(sql)
        print(result.fetchall(),'pega todos os valores')
        print(result.all(),'pega todos os valores')
        
    with engine.begin():
        sql = text('SELECT id, name, comment FROM public.comments;')
        result = con.execute(sql)
        print(result.first(),'pega 1, mas nao dá erro se nao conseguir')
con.close()