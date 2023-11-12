# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Empresa(models.Model):
     _name = 'inmobiliaria_upo.empresa'
     _description = 'Empresa'

     name = fields.Char(string="CIF", size = 8, required=True, help="Cif de la empresa")
     nombre = fields.Char(string="Nombre", required=True, help="Nombre de la empresa")
     telefono = fields.Integer("Telefono")
     email = fields.Char(string="Email", required=True, help="Email de la empresa")

     ids_Trabajadores = fields.One2many("inmobiliaria_upo.trabajador",'ids_Empresas','Trabajadores')
     

     #@api.constrains('telefono')
     #def _check_telefono(self):
     #    if self.telefono > 9:
     #          raise models.ValidationError('El telefono debe tener 9 digitos.')
     