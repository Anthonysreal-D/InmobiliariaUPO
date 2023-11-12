# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Propiedad(models.Model):
     _name = 'inmobiliaria_upo.propiedad'
     _description = 'Propiedad'

     idPropietario = fields.Char(string="ID Propietario", size=9, required=True)
     municipio = fields.Char('Municipio', required=True)
     name = fields.Char(string="ID Propiedad", size=8, required=True)
     nombre = fields.Char(string="Nombre", size=50, required=True)
     calle = fields.Char(string="Calle", required=True)
     codigoPostal = fields.Char(string="Codigo Postal", size=5, required=True)

     ids_Tipos = fields.Many2one("inmobiliaria_upo.tipo",string="Tipos")
     ids_Visitas = fields.One2many("inmobiliaria_upo.visita",'ids_Propiedades','Visitas')