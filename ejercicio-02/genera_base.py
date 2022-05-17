from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Paises(Base):
    __tablename__ = 'paises'
    
    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_id = Column(String)
    itu = Column(String)
    languajes = Column(String)
    es_independiente = Column(String)

    def __repr__(self):
        return "Paises: nombre_pais =%s capital =%s continente = %s dial =%s geoname_id =%s itu =%s languajes =%s es_independiente =%s" %(
            self.nombre_pais,
            self.capital,
            self.continente,
            self.dial,
            self.geoname_id,
            self.itu,
            self.languajes,
            self.es_independiente
        ) 
Base.metadata.create_all(engine)

