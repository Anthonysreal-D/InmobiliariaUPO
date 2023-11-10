# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tipo(models.Model):
     _name = 'inmobiliaria_upo.tipo'
     _description = 'Tipo'

     tipoInmueble = fields.Char(string="Tipo", size=60, required=True, help="Tipo de inmueble")
     estado = fields.Char('Estado', size=9, required=True, help="Estado del inmueble")
