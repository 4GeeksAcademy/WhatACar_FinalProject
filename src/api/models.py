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
    address = db.Column(db.String(120), nullable=True) 
    role = db.Column(db.Enum(UserRole), nullable=False, default=UserRole.BUYER)
    phone = db.Column(db.Integer, nullable=False) #Podría ser único
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
    price = db.Column(db.Float, nullable=False) #Estuve leyendo y cuando no quieres un número de decimales exactos el FLOAT es buena opción
    description = db.Column(db.String(2000))
    image_Id = db.Column(db.Integer, db.ForeignKey('image.id')) 
    year = db.Column(db.Integer)
    km = db.Column(db.Integer)
    fuel = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))

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

class Garage (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    web = db.Column(db.String(150), nullable=True)
    image_Id = db.Column(db.Integer, db.ForeignKey('image.id')) 
    product_Id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_Id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Garages {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "web" : self.web,
            "image_Id": self.image_Id,
            "product_Id": self.product_Id,
            "user_Id": self.user_Id
        }
    
class Image (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_Id = db.Column(db.Integer, db.ForeignKey('user.id'))
    image = db.Column(db.String(200), nullable=False)
    product_Id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __repr__(self):
        return f'<Images {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_Id": self.user_Id,
            "image": self.image,
            "product_Id": self.product_Id
        }
    
class Service (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    image_Id = db.Column(db.Integer, db.Foreignkey('image.id'))
    garage_Id = db.Column(db.Integer, db.Foreignkey('garage.id'))

    def __repr__(self):
        return f'<Services {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "image_Id": self.image_Id,
            "garage_Id": self.garage_Id
        }
    
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_Id = db.Column(db.Integer, db.Foreignkey('user.id'))
    product_Id = db.Column(db.Integer, db.Foreignkey('product.id'))
    stars = db.Column(db.Integer(5), nullable=False) #ALEX, aquí no se si debería darle un fijo como las tablas que has tenido que crear para que solo puedan elegir un valor...
    comment = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f'<Reviews {self.id}>'
    
    def serialize(self):
        return{
            "id": self.id,
            "user_Id": self.user_Id,
            "product_Id": self.product_Id,
            "stars": self.stars,
            "comment": self.comment
        }
    
class sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_Id = db.Column(db.Integer, db.Foreignkey('user.id'))
    product_Id = db.Column(db.Integer, db.Foreignkey('product.id'))
    taller_Id = db.Column(db.Integer, db.Foreignkey('taller.id'))
    fecha = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Sales {self.id}>'
    
    def serialize(self):
        return{
            "id": self.id,
            "user_Id": self.user_Id,
            "product_Id": self.product_Id,
            "taller_Id": self.taller_Id,
            "fecha": self.fecha
        }
    
class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Brands {self.id}>'
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name
        }
    
class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    brand_Id = db.Column(db.Integer, db.Foreignkey('brand.id'))

    def __repr__(self):
        return f'<Models {self.id}>'
    
    def serialize(self):
        return{
            "id": self.id,
            "model": self.model,
            "type": self.type,
            "brand_Id": self.brand_Id
        }