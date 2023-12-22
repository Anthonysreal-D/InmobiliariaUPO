# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Alquiler(models.Model):
     _name = 'inmobiliaria_upo.alquiler'
     _description = 'Alquiler'
     _inherit= 'inmobiliaria_upo.operacion'

     name = fields.Char(string="ID Alquiler", size=8, required=True)
     fechaInicio = fields.Char('Fecha de inicio', required=True)
     fechaFin = fields.Char('Fecha de fin', required=True)
     precio = fields.Integer('Precio', required=True)

     #ids_Alquiler = fields.One2many("inmobiliaria_upo.alquiler", string="Alquileres")
     #Alquiler se puede realquilar asi mismo pero no hemos podido encontrar el fallo
     ids_Alquileres = fields.One2many("inmobiliaria_upo.alquiler", "ids_ReAlquileres","Alquileres")
     ids_ReAlquileres = fields.Many2one("inmobiliaria_upo.alquiler", string="Re-alquiler")

     _sql_constraints = [('alquiler_name_unique','UNIQUE (name)','El ID debe ser único')]

     @api.onchange('precio')
     def onchange_alquiler(self):
          resultado = {}
          if self.capacity < 0:
               resultado = {
                    'value': {'precio':0},
                    'warning': {
                         'title':'Valores incorrectos',
                         'message':'El precio debe ser un valor positivo'
                    }
               }
               return resultado

