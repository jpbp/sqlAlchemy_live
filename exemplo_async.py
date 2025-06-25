from sqlalchemy import create_engine, text
from asyncio import run
from sqlalchemy.ext.asyncio import create_async_engine


engine = create_async_engine( # Padrão de projeto Factory
    #'sqlite://'
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db', echo=True
)

async def main():
    async with engine.connect() as con:
        sql = text('SELECT id, name, comment FROM public.comments;')
        result = await con.execute(sql)
        print(result.fetchall())
    
run(main())