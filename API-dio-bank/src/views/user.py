from src.app import ma 
from src.models import User
from src.views.role import RoleSchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ('id', 'username', 'role')
        include_fk = True

    role = ma.Nested(RoleSchema)

class CreateUserSchema(ma.Schema):
    username = ma.String(required=True)
    password = ma.String(required=True, load_only=True)
    role_id = ma.Integer(required=True)
    
    