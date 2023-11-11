from odoo import models, fields, api
from . import persona


class cliente(models.Model):
    _name = 'inmobiliaria_upo.cliente'
    _inherit = "inmobiliaria_upo.persona"
    
    sIdCliente = fields.Char(string="ID Cliente", required=True, size=5)
    sPais = fields.Many2one('res.country', string='Pais')
    sCiudad = fields.Char(string="Ciudad")  