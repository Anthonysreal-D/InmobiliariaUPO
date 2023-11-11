# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import operacion

class venta(models.Model):
    
    _inherit = ["sale.order", "inmobiliaria_upo.operacion"]
    _name = "inmobiliaria_upo.venta"
    _descripcion = "InmobiliariaUPO Venta"

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
    
    
    #def _comision(self):
    #    return amount_total/100*10
        
    
    #_description = 'InmobiliariaUPO venta'
    
    #precio = fields.Float(string = "Precio")
    #fecha = fields.Datetime(string = "Fecha")
    #comision = fields.Integer(string = "Comision")