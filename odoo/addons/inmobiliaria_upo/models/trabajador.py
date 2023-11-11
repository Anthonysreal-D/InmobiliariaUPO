# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Trabajador(models.Model):
     _name = 'inmobiliaria_upo.trabajador'
     _description = 'Trabajador'

     name = fields.Char(string="Nombre", required=True, help="Nombre del trabajador")
     idTrabajador = fields.Char(string="ID trabajador", required=True, help="ID asignado al trabajdor")
     cif = fields.Char(string="CIF de la empresa", required=True, help="CIF de la empresa del trabajador")
     sueldo = fields.Char(string="Sueldo", required=True, help="Sueldo del trabajdor")
    #El trabajador tendra mas campos que heredara del modelo persona
    
     ids_Empresas = fields.Many2one("inmobiliaria_upo.empresa", string="Empresas")