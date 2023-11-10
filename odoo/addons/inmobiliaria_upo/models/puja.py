# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Puja(models.Model):
     _name = 'inmobiliaria_upo.puja'
     _description = 'Puja'

     id = fields.Char(string="ID Puja", required=True, help="Cif de la empresa")
     puja = fields.Char(string="Importe de la puja", required=True, help="Dinero pujado")
     idSubasta = fields.Char(string="ID Subasta", required=True, help="ID de la subasta asignada")
