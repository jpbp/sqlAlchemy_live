import sqlalchemy as sa


metadata = sa.MetaData()

t = sa.Table(
    'comments',
    metadata,
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('name',sa.String(),nullable=False),
    sa.Column('comment',sa.String(),nullable=False),
    sa.Column('live',sa.String(),nullable=False),
    sa.Column('created_at',sa.DateTime(),nullable=False),
    sa.PrimaryKeyConstraint('id'),
    
)

engine = sa.create_engine( # Padrão de projeto Factory
    'sqlite:///database.db', echo=True
    #'postgresql+psycopg://app_user:app_password@localhost:5432/app_db', echo=True
)

metadata.create_all(engine)

# with  engine.connect() as con:
#     #aqui a magia acotence, com begin conseguimos garantir a ACID, se der ruim faz rollback
#     with engine.begin():
#         sql = text('SELECT id, name, comment FROM public.comments;')
#         result = con.execute(sql)
#         print(result.fetchall())
# con.close()