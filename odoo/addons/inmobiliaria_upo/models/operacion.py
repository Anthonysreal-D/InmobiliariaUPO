# -*- coding: utf-8 -*-

from odoo import models, fields, api


class operacion(models.Model):
    _name = 'inmobiliaria_upo.operacion'
    _description = 'InmobiliariaUPO Operacion'

    idCliente = fields.Char(String='Cliente', required=True)
    idPropiedad = fields.Char(String='Propiedad', required=True)

    
    