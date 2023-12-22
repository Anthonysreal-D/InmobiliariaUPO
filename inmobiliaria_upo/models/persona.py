from odoo import models, fields, api
from odoo.exceptions import ValidationError


class persona(models.Model):
    _name = 'inmobiliaria_upo.persona'
    _inherit = 'hr.employee'

    category_ids = fields.Many2many(relation=False)#No es ninguna variable de nuestro programa, no se utiliza simplemente necesito poner su relation como falsa para poder heredar de hr.employee correctamente
    name = fields.Char(string="DNI", size=10)
    phone = fields.Char(string="Teléfono", size=9)
    work_email = fields.Char(string="Correo Electrónico")
    
    nombre = fields.Char(string="Nombre", required=True)
    apellidoUno = fields.Char(string="Primer apellido", required=True, size=255)
    apellidoDos = fields.Char(string="Segundo Apellido", size=255)
    edad = fields.Integer(string="Edad", size=255)

    @api.constrains('edad')
    def _validar_edad(self):
        if self.edad < 0:
            raise ValidationError("La edad no puede ser negativa")
        
    @api.constrains('phone')
    def _validar_phone(self):
        try:
            int(self.phone)
            if len(self.phone) < 9:
                raise ValidationError("El número de teléfono tiene que tener 9 dígitos")
            elif int(self.phone) < 0:
                raise ValidationError("El número de teléfono no puede ser negativo")
        except ValueError:
            raise ValidationError("El número de teléfono tiene que ser un número")
        