# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from . import operacion, seguro

class compra(models.Model):
    _inherit=["purchase.order","inmobiliaria_upo.operacion"]
    _name="inmobiliaria_upo.compra"
    _description="InmobiliariaUPO Compra"
    
    partner_id = fields.Many2one(required=False)
    
    amount_total = fields.Monetary(compute=False, required=True, readonly=False)
    amount_tax = fields.Monetary(compute='_comision')
    mensualidades = fields.Integer(string="Nº mensualidades", default=1)
    precioMensual = fields.Monetary(string="Importe mensual", compute='_compute_precioMensual')
    idSeguro = fields.Many2one("inmobiliaria_upo.seguro", string="seguro")
    
    @api.depends('mensualidades', 'amount_total')
    def _compute_precioMensual(self):
        for record in self:
            if record.amount_total > 0:
                record.precioMensual = record.amount_total/record.mensualidades
            else:
                record.precioMensual = 0
    
    @api.depends('amount_total')
    def _comision(self):
        for record in self:
            if record.amount_total > 0:
                record.amount_tax = record.amount_total/100*10
            else:
                record.amount_tax = 0

    @api.constrains('mensualidades')
    def _validar_mensualidades(self):
        if self.mensualidades < 1 or self.mensualidades > 12:
            raise ValidationError("El numero de mensualidades debe estra entre 1 y 12 incluidos")