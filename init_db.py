from datetime import datetime
from app import db

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100))
    estado = db.Column(db.String(50))
    fecha_recepcion = db.Column(db.DateTime, default=datetime.now)  
