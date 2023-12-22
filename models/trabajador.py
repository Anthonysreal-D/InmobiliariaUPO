# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Trabajador(models.Model):

    
     _name = 'inmobiliaria_upo.trabajador'
     _description = 'Trabajador'
     _inherit = 'inmobiliaria_upo.persona'

     name = fields.Char(string="ID trabajador", size = 5, required=True, help="ID asignado al trabajdor")
     sueldo = fields.Integer(string="Sueldo", required=True, help="Sueldo del trabajdor, debe ser una cifra entre 1 y 9.999")
    
     ids_Empresas = fields.Many2one("inmobiliaria_upo.empresa", string="Empresas")
     idOperacion = fields.One2many("inmobiliaria_upo.operacion","idTrabajador","Operacion")
     
     _sql_constraints = [('trabajador_id_unique','UNIQUE (name)','El ID del trabajadordebe ser único')]
     
     #Impide introducir un ID de trabajador incorrecto.
     @api.constrains('name')
     def _check_cif(self):
          if len(self.name) != 5:
               raise ValidationError('El ID es incorrecto.')
          if not self.name[:1].isalpha() or not self.name[1:].isdigit():
               raise ValidationError('El primer caracter debe ser la letra y los siguientes cuatro deben ser dígitos.')
           
     #Impide que el sueldo salga del rango establecido.
     @api.constrains('sueldo')
     def _check_telefono(self):
          if self.sueldo < 1 or self.sueldo > 9999:
               raise ValidationError('El sueldo esta fuera del rango')
