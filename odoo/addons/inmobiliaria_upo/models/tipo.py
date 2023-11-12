# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tipo(models.Model):
     _name = 'inmobiliaria_upo.tipo'
     _description = 'Tipo'

     idPropiedad = fields.Char(string="ID Propiedad", size=8, required=True)
     tipoInmueble = fields.Char('Tipo de inmueble', required=True)
     estado = fields.Char('Estado', required=True)

      #ids_Propiedades = fields.One2many("inmobiliaria_upo.propiedad",'ids_Tipos','Propiedades')
