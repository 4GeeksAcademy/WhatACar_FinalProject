from flask_sqlalchemy import SQLAlchemy

from enum import Enum

db = SQLAlchemy()

class IdDocument(Enum):
    DNI = 'DNI'
    CIF = 'CIF'

class UserRole(Enum): #Solo se pueden usar los roles que pongamos aquí
    BUYER = 'buyer'
    SELLER = 'seller'
    GARAGE = 'garage'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    id_document = db.Column(db.Enum(IdDocument), nullable=False, default=IdDocument.DNI)
    id_number = db.Column(db.String(10), unique=True, nullable=False)
    address = db.Column(db.String(120), nullable=False) #Tal vez no debería de ser obigatorio en el registro, sino al hacer una compra
    role = db.Column(db.Enum(UserRole), nullable=False, default=UserRole.BUYER)
    phone = db.Column(db.Integer, nullable=False) #Podría ser único
    dark_mode = db.Column(db.Boolean(), default=False)
    #is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "id_type": self.id_type.value,
            "id_number": self.id_number,
            "address": self.address, 
            "role": self.role,
            "phone": self.phone
            
            # do not serialize the password, its a security breach
        }
    



class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __repr__(self):
        return f'<Favorite {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id
        }
    


class ProductState(Enum):
    NUEVO = 'nuevo'
    SEMINUEVO = 'seminuevo'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    state = db.Column(db.Enum(ProductState), nullable=False)
    #price = db.Column(db.Integer, nullable=False) #Preguntar por si es str o int (str por el €) BUSCAR tipo de dato
    description = db.Column(db.String(2000))
    images = db.Column(db.String(400)) #Preguntar cómo almacenar imagenes insertadas
    year = db.Column(db.Integer)
    km = db.Column(db.Integer)
    fuel = db.Column(db.Integer)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    # model_id = db.Column(db.Integer, db.ForeignKey('model.id'))

    def __repr__(self):
        return f'<Products {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "state": self.state,
            "price": self.price,
            "description": self.description,
            "images": self.images,
            "year": self.year,
            "km": self.km,
            "fuel": self.fuel,
            "user_id": self.user_id,
            "brand_id": self.brand_id,
            "model_id": self.model_id
        }

