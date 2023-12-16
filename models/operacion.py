# -*- coding: utf-8 -*-

from odoo import models, fields, api


class operacion(models.Model):
    _name = 'inmobiliaria_upo.operacion'
    _description = 'InmobiliariaUPO Operacion'
    
    idPropiedad = fields.Many2one("inmobiliaria_upo.propiedad",'Propiedad', required=True)
    idCliente = fields.Many2one("inmobiliaria_upo.cliente",'Cliente', required=True)
    idTrabajador = fields.Many2one("inmobiliaria_upo.trabajador",'Trabajador', required=True)

    
    