# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
    name = fields.Char(string="Seguro Id", default=lambda self: self.env.user.id)
    importe = fields.Monetary(string="Importe")
    