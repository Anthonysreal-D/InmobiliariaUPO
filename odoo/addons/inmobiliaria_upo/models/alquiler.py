# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Alquiler(models.Model):
     _name = 'inmobiliaria_upo.alquiler'
     _description = 'Alquiler'

     idAlquiler = fields.Char(string="ID Alquiler", size=8, required=True)
     fechaInicio = fields.Char('Fecha de inicio', required=True)
     fechaFin = fields.Char('Fecha de fin', required=True)
     precio = fields.Integer('Precio', required=True)

