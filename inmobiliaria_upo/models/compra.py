# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import operacion, seguro

class compra(models.Model):
    _inherit=["purchase.order","inmobiliaria_upo.operacion"]
    _name="inmobiliaria_upo.compra"
    _description="InmobiliariaUPO Compra"
    
    partner_id = fields.Many2one(required=False)
    
    amount_total = fields.Monetary(compute=False, required=True, readonly=False)
    amount_tax = fields.Monetary(compute=False)
    mensualidades = fields.Integer(string="Nº mensualidades", default=1)
    precioMensual = fields.Monetary(string="Importe mensual", compute='_compute_mensualidades')
    idSeguro = fields.Many2one("inmobiliaria_upo.seguro", string="seguro")
    
    #def _compute_mensualidades(self):
    #    if self.amount_total > 0:
    #        self.precioMensual = self.amount_total/self.mensualidades
    #    else:
    #        self.precioMensual = 0