import sqlalchemy

# Criar Conexão com Banco SQLITE
# caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///GESOFT.db")
connection = engine.connect()


# Criar tabela
connection.execute("""CREATE TABLE IF NOT EXISTS ENTREGA (
                        SHIPID int not null,
                        SHIPPEDDATE date);
                    """)

connection.execute("""CREATE TABLE IF NOT EXISTS STATUS(
                        IDSTATUS tinyint not null,
                        STATUS varchar(45) not null)
                    """)

connection.execute("""CREATE TABLE IF NOT EXISTS COMPONESTES(
                        COMPONENTID int not null,
                        DESCRIPTION varchar(100),
                        REFERNENCE varchar(100))
                    """)
 
connection.execute("""CREATE TABLE IF NOT EXISTS PLACA(
                        CODE int not null,
                        CATEGORY varchar(30),
                        DESCRIPTION varchar(100),
                        COMPONENTS int)
                    """)