from src.app import ma
from src.models import Role

class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        fields = ('id', 'name')