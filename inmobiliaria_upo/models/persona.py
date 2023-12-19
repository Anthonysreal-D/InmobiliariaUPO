from odoo import models, fields, api


class persona(models.Model):
    _name = 'inmobiliaria_upo.persona'
    _inherit = 'hr.employee'

    category_ids = fields.Many2many(relation=False)
    name = fields.Char(string="DNI", size=10)
    phone = fields.Char(string="Teléfono")
    work_email = fields.Char(string="Correo Electrónico")
    
    nombre = fields.Char(string="Nombre", required=True)
    apellidoUno = fields.Char(string="Primer apellido", required=True, size=255)
    apellidoDos = fields.Char(string="Segundo Apellido", size=255)
    edad = fields.Integer(string="Edad", size=255)