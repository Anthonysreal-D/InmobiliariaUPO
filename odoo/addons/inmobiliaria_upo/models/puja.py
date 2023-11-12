# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Puja(models.Model):
     _name = 'inmobiliaria_upo.puja'
     _description = 'Puja'
     #_inherit = 'inmobiliaria_upo.operacion'
     
     #El modelo trabajador deberia heredar los campos del modulo Operacion
     #Pero debido a que lo realiza otro compañero no lo tengo disponible asi pues
     #lo dejo marcado

     #El NAME es el ID de nuestra puja
     name = fields.Char(string="ID Puja", size=10, required=True, help="Cif de la empresa")
     puja = fields.Integer(string="Importe de la puja", required=True, help="Dinero pujado")

     ids_Subastas = fields.Many2one("inmobiliaria_upo.subasta", string="Subasta")