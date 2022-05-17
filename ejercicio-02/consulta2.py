from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_base import Paises


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de
# la entidad docentes

paises_Asia = session.query(Paises).filter(Paises.nombre_pais == "Asia").order_by(Paises.dial).all()


print(paises_Asia)
