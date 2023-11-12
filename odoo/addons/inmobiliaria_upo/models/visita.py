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


