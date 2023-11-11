# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Puja(models.Model):
     _name = 'inmobiliaria_upo.puja'
     _description = 'Puja'

     #El NAME es el ID de nuestra puja
     name = fields.Char(string="ID Puja", required=True, help="Cif de la empresa")
    
     puja = fields.Char(string="Importe de la puja", required=True, help="Dinero pujado")
     idSubasta = fields.Char(string="ID Subasta", required=True, help="ID de la subasta asignada")

     ids_Subastas = fields.Many2one("inmobiliaria_upo.subasta", string="Subasta")