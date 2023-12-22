# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Empresa(models.Model):
    _name = 'inmobiliaria_upo.empresa'
    _description = 'Empresa'

    name = fields.Char(string="CIF", size=9, required=True, help="Cif de la empresa")
    nombre = fields.Char(string="Nombre", required=True, help="Nombre de la empresa")
    telefono = fields.Char(string="Telefono", required=True, help="Número de teléfono de la empresa")
    email = fields.Char(string="Email", required=True, help="Email de la empresa")

    ids_Trabajadores = fields.One2many("inmobiliaria_upo.trabajador", 'ids_Empresas', 'Trabajadores')
    
    _sql_constraints = [('empresa_cif_unique','UNIQUE (name)','Ya hay una empresa con este CIF resgistrada')]
    
    #Impide introducir un CIF incorrecto.
    @api.constrains('name')
    def _check_cif(self):
        if len(self.name) != 9:
                raise ValidationError('El CIF es incorrecto.')
        if not self.name[:1].isalpha() or not self.name[1:].isdigit():
                raise ValidationError('El primer caracter debe ser la letra y los siguientes ocho deben ser dígitos.')
       
    #Impide que el numero de telefono introducido (ESP) sea distinto de 9 digitos.
    @api.constrains('telefono')
    def _check_telefono(self):
        if not self.telefono.isdigit() or len(self.telefono) != 9:
            raise ValidationError('El telefono debe tener exactamente 9 dígitos.')
