# Importar bibliotecas
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Base de Dados - Endereço
engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/taskflow')

# Configurar as sessões
local_session = sessionmaker(bind=engine)

Base = declarative_base()

class Pessoa (Base):
    __tablename__= 'pessoas'
