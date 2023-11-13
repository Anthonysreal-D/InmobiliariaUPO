# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Trabajador(models.Model):

    
     _name = 'inmobiliaria_upo.trabajador'
     _description = 'Trabajador'
     _inherit = 'inmobiliaria_upo.persona'

     name = fields.Char(string="ID trabajador", size = 5, required=True, help="ID asignado al trabajdor")
     sueldo = fields.Integer(string="Sueldo", required=True, help="Sueldo del trabajdor")
    
     ids_Empresas = fields.Many2one("inmobiliaria_upo.empresa", string="Empresas")
     idOperacion = fields.One2many("inmobiliaria_upo.operacion","idTrabajador","Operacion") 