# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Empresa(models.Model):
     _name = 'inmobiliaria_upo.empresa'
     _description = 'Empresa'

     name = fields.Char(string="Title", required=True, help="Titulo de fihca de la empresa")
     cif = fields.Char(string="CIF", required=True, help="Cif de la empresa")
     nombre = fields.Char(string="Nombre", required=True, help="Nombre de la empresa")
     telefono = fields.Char(string="Telefono", required=True, help="Telefono de la empresa")
     email = fields.Char(string="Email", required=True, help="Email de la empresa")

