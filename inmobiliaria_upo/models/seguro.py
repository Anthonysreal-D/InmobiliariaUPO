# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import venta, compra

class seguro(models.Model):
    _name = "inmobiliaria_upo.seguro"
    _description = "InmobiliariaUPO Seguro"
    
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                string="Company",
                                default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                 related='company_id.currency_id',
                                 default=lambda
                                 self: self.env.user.company_id.currency_id.id)
    name = fields.Char(string="Seguro Id",required=True, copy=False)
    importe = fields.Monetary(string="Importe", required=True)
    idVenta = fields.Many2one("inmobiliaria_upo.venta", 'Venta')
    idCompra = fields.Many2one("inmobiliaria_upo.compra", 'Compra')
    