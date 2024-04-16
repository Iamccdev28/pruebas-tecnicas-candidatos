from sqlalchemy import Column, Float, Integer, String, text
from sqlalchemy_serializer import SerializerMixin
from extensions import db

class Packages(db.Model, SerializerMixin):
    __tablename__ = 'paquetes'

    idpaquete = Column(Integer, primary_key=True)
    nombrepaquete = Column(String(45))
    descripcion = Column(String(45))
    foto = Column(String(45))
    estatus = Column(Integer)
    idcategorias = Column(Integer)
    promocion = Column(Integer)
    fechainicial = Column(String(45))
    fechafinal = Column(String(45))
    aplicardirecto = Column(Integer)
    cantidad = Column(String(45))
    considerar = Column(String(45))
    definirfecha = Column(Integer)
    servicio = Column(Integer)
    lunes = Column(Integer)
    martes = Column(Integer)
    miercoles = Column(Integer)
    jueves = Column(Integer)
    viernes = Column(Integer)
    sabado = Column(Integer)
    domingo = Column(Integer)
    repetitivo = Column(Integer)
    preciofijo = Column(Float)
    horainicialpromo = Column(String(45))
    horafinalpromo = Column(String(45))
    orden = Column(Integer)
    activarcomentario = Column(Integer)
    mensaje = Column(String(45))
    siniva = Column(Integer)
    iva = Column(String(45))
    solomostrador = Column(Integer)
    visualizarcarrusel = Column(Integer)
    intervaloservicio = Column(String(45))
    idcategoriapaquete = Column(Integer)
    inventario = Column(Integer, server_default=text("'0'"))
    mostrarenapp = Column(Integer, server_default=text("'0'"))
    sku = Column(String(255))
    preciosugerido = Column(Float(12), server_default=text("'0.00'"))