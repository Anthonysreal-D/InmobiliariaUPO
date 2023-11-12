from odoo import models, fields, api


class persona(models.Model):
    _name = 'inmobiliaria_upo.persona'
    
    name = fields.Char(string="DNI", required=True, size=10)
    sNombre = fields.Char(string="Nombre", required=True)
    sApellidoUno = fields.Char(string="Primer apellido", required=True)
    sApellidoDos = fields.Char(string="Segundo Apellido")
    iEdad = fields.Integer("Edad")
    sEmail = fields.Char("Email")
    iTelefono = fields.Integer("Telefono", size=9)