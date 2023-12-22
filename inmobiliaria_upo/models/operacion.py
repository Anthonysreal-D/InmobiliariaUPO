# -*- coding: utf-8 -*-

from odoo import models, fields, api


class operacion(models.Model):
    _name = 'inmobiliaria_upo.operacion'
    _description = 'InmobiliariaUPO Operacion'
    
    idOperacion = fields.Char(string="Id Operacion")
    idPropiedad = fields.Many2one("inmobiliaria_upo.propiedad",'Propiedad', required=True)
    idCliente = fields.Many2one("inmobiliaria_upo.cliente",'Cliente', required=True)
    idTrabajador = fields.Many2one("inmobiliaria_upo.trabajador",'Trabajador', required=True)

    _sql_constraints = [('operacion_idOperacion_unique','UNIQUE (idOperacion)','El id de la operacion debe ser único')]
    