from odoo import models, fields, api
from . import persona


class propietario(models.Model):
    _name = 'inmobiliaria_upo.propietario'
    _inherit = "inmobiliaria_upo.persona"
    
    idPropietario = fields.Char(string="ID Propietario", required=True)
    valoracion = fields.Char(string="Valoración", size=2500)
    
    ids_Propiedades = fields.One2many('inmobiliaria_upo.propiedad',"ids_Propietarios", "Propiedades")

    _sql_constraints = [('cliente_name_unique','UNIQUE (name)','El DNI debe ser único')]
    _sql_constraints = [('cliente_idPropietario_unique','UNIQUE (idPropietario)','El Id del Propietario debe ser único')]
