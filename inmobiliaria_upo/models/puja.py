# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Puja(models.Model):
     _name = 'inmobiliaria_upo.puja'
     _description = 'Puja'
     _inherit = 'inmobiliaria_upo.operacion'
     
     #El NAME es el ID de nuestra puja
     name = fields.Char(string="ID Puja", size=10, required=True, help="Cif de la empresa")
     puja = fields.Integer(string="Importe de la puja", required=True, help="Dinero pujado")

     ids_Subastas = fields.Many2one("inmobiliaria_upo.subasta", string="Subasta")
     
     _sql_constraints = [('puja_id_unique','UNIQUE (name)','El ID de la puja debe ser único')]

     
     @api.constrains('puja','ids_Subastas')
     def _check_puja(self):
            if self.puja <= self.ids_Subastas.valorFinal:
                raise ValidationError('La puja debe ser mayor que el valor final de la subasta.')