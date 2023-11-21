# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import operacion, seguro

class venta(models.Model):
    
    _inherit = ["sale.order", "inmobiliaria_upo.operacion"]
    _name = "inmobiliaria_upo.venta"
    _description = "InmobiliariaUPO Venta"

    partner_id = fields.Many2one(required=False)
    
    partner_invoice_id = fields.Many2one(required=False)
    
    partner_shipping_id = fields.Many2one(required=False)
    
    pricelist_id = fields.Many2one(required=False)
    
    transaction_ids = fields.Many2many(relation=False)
    
    tag_ids = fields.Many2many(relation=False)
    
    amount_total = fields.Monetary(compute = False, required=True)
    amount_tax = fields.Monetary(compute='_comision')
    state = fields.Selection(
        selection=[
            ('En venta', "Disponible"),
            ('Comprado', "No disponible"),
        ], 
        default="En venta")
    idSeguro = fields.Many2one("inmobiliaria_upo.seguro",string="seguro")
    
    @api.depends('amount_total')
    def _comision(self):
        for record in self:
            if record.amount_total > 0:
                record.amount_tax = record.amount_total/100*10
            else:
                record.amount_tax = 0
        
    
