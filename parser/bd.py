from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
# localhost
SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:my-secret-pw@localhost:3306/test'
engine = create_engine('mysql+mysqlconnector://root:my-secret-pw@localhost:3306/test', echo=True,)  # подключились к mysql

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(engine)

