# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Puja(models.Model):
     _name = 'inmobiliaria_upo.puja'
     _description = 'Puja'
     _inherit = 'inmobiliaria_upo.operacion'
     
     #El NAME es el ID de nuestra puja
     name = fields.Char(string="ID Puja", size=10, required=True, help="Cif de la empresa")
     puja = fields.Integer(string="Importe de la puja", required=True, help="Dinero pujado")

     ids_Subastas = fields.Many2one("inmobiliaria_upo.subasta", string="Subasta")
     
     _sql_constraints = [('puja_id_unique','UNIQUE (name)','El ID de la puja debe ser único')]

     
     @api.constrains('puja')
     def _check_puja_greater_than_valor_final(self):
        for puja in self:
            if puja.puja <= puja.ids_Subastas.valorFinal:
                raise exceptions.ValidationError('La puja debe ser mayor que el valor final de la subasta.')