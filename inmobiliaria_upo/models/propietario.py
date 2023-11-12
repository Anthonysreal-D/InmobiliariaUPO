from odoo import models, fields, api
from . import persona


class propietario(models.Model):
    _name = 'inmobiliaria_upo.propietario'
    _inherit = "inmobiliaria_upo.persona"
    
    sIdPropietario = fields.Char(string="ID Propietario", required=True, size=5)
    sValoracion = fields.Char(string="Valoración", size=2500)