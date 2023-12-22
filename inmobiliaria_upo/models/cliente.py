from odoo import models, fields, api
from . import persona


class cliente(models.Model):
    _name = 'inmobiliaria_upo.cliente'
    _inherit = "inmobiliaria_upo.persona"
    
    idCliente = fields.Char(string="ID Cliente", required=True)
    country_id = fields.Many2one('res.country', 'País', groups="hr.group_hr_user", tracking=True)

    ciudad = fields.Char(string="Ciudad", size=255) 
    
    idOperacion = fields.One2many("inmobiliaria_upo.operacion","idCliente","Operacion")
    ids_Visitas = fields.One2many("inmobiliaria_upo.visita", 'ids_Clientes', 'Visitas')

    _sql_constraints = [('cliente_name_unique','UNIQUE (name)','El DNI debe ser único')]
    _sql_constraints = [('cliente_idCliente_unique','UNIQUE (idCliente)','El Id del Cliente debe ser único')]
