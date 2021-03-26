from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:my-secret-pw@mysql-container:3306/test'
engine = create_engine('mysql+mysqlconnector://root:my-secret-pw@mysql-container:3306/test', echo=True,)  # подключились к mysql

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
