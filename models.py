# Importar bibliotecas
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, ForeignKey, Date, func
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, scoped_session

# Base de Dados - Endereço
engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/taskflow')

# Configurar as sessões
db_session = scoped_session (sessionmaker(bind=engine))

Base = declarative_base()

class Pessoa (Base):
    __tablename__= 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    papel = Column(String(50), default='usuario', nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Pessoa {self.nome}'

class Recurso (Base):
    __tablename__= 'recursos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(20), nullable=False)
    descricao = Column(String(255), nullable=False)
    responsavel = Column(String(20), nullable=False)
    data_retirda = Column(Date, nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Recurso {self.nome}'

class Categoria (Base):
    __tablename__= 'categorias'
    id = Column(Integer, primary_key=True)
    nome = Column(String(20), nullable=False)
    descricao = Column(String(255), nullable=False)
    responsavel = Column(String(20), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Categoria {self.nome}'

class Tarefa (Base):
    __tablename__= 'tarefas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(20), nullable=False)
    data = Column(Date, nullable=False)
    responsavel = Column(String(20), nullable=False)
    prioridade = Column(String(20), nullable=False)
    descricao = Column(String(255), nullable=False)
    tipo = Column(String(20), nullable=False)
    recurso = Column(Integer, nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Tarefa {self.nome}'

