from odoo import models, fields, api
from . import persona


class propietario(models.Model):
    _name = 'inmobiliaria_upo.propietario'
    _inherit = "inmobiliaria_upo.persona"
    
    idPropietario = fields.Char(string="ID Propietario", required=True)
    valoracion = fields.Char(string="Valoración", size=2500)
    
    ids_Propiedades = fields.One2many('inmobiliaria_upo.propiedad',"ids_Propietarios", "Propiedades")
