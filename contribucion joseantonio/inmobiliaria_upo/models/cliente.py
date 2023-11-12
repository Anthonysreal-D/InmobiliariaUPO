from odoo import models, fields, api
from . import persona


class cliente(models.Model):
    _name = 'inmobiliaria_upo.cliente'
    _inherit = "inmobiliaria_upo.persona"
    
    sIdCliente = fields.Char(string="ID Cliente", required=True)
    country_id = fields.Many2one('res.country', 'País', groups="hr.group_hr_user", tracking=True)

    sCiudad = fields.Char(string="Ciudad", size=255)
    #idOperacion = fields.One2many('inmobiliaria_upo.operacion', string="ID Operacion")
    #idVisita = fields.One2many('inmobiliaria_upo.visita', string="ID Visita")