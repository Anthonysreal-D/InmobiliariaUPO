# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subasta(models.Model):
     _name = 'inmobiliaria_upo.subasta'
     _description = 'Subasta'
     
     #El NAME es el ID de nuestra subasta
     name = fields.Char(string="ID Subasta", size=6, required=True, help="ID de la subasta")
    
     valorInicial = fields.Integer(string="Valor de inicio", required=True, help="Importe con el que se inicia la subasta")
     valorFinal = fields.Integer(string="Ultimo valor", required=True, help="Ultimo importe pujado y con el que finalizaria la subasta")
     fecha = fields.Date(string="Fecha de la subasta", required=True, help="Fecha en la que se inicia la subasta")

     ids_Pujas = fields.One2many("inmobiliaria_upo.puja",'ids_Subastas','Pujas')
     
     _sql_constraints = [('subasta_id_unique','UNIQUE (name)','El ID de la subasta debe ser único')]

     @api.onchange('ids_Pujas.puja')
     def onchange_ids_pujas_puja(self):
        if self.ids_Pujas:
            max_puja = max(self.ids_Pujas.mapped('puja'))
            if max_puja > self.valorFinal:
                self.valorFinal = max_puja