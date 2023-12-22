# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visita(models.Model):
     _name = 'inmobiliaria_upo.visita'
     _description = 'Visita'

     name = fields.Char(string="ID Visita", size=8, required=True)
     fecha = fields.Char('Fecha', required=True)
     hora = fields.Char('Hora', required=True)
     idCliente = fields.Char(string="ID Cliente", size=9, required=True)
     valoracion = fields.Char('Valoracion', required=True)
     interes = fields.Char('Interes', required=True)
     idPropiedad = fields.Char(string="ID Propiedad", size=8, required=True)

     ids_Propiedades = fields.Many2one("inmobiliaria_upo.propiedad",string="Propiedades")
     ids_Clientes = fields.Many2one("inmobiliaria_upo.cliente", string="Clientes")
     
     _sql_constraints = [('visita_name_unique','UNIQUE (name)','El ID debe ser único')]

     numClientes = fields.Integer(compute='_clientesTotal',string='Numero de clientes',store=True)

     @api.depends('ids_Clientes')
     def _clientesTotal(self): 
          for record in self:
               record.numClientes = len(record.ids_Clientes)

