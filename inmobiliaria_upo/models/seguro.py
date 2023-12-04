# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
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
    
    @api.constrains('idVenta','idCompra')
    def _validar_relacion(self):
        if self.idVenta.exists() and self.idCompra.exists():
            raise ValidationError("El seguro no puede pertenecer a una compra y una venta a la vez.")
        elif not self.idVenta.exists() and not self.idCompra.exists():
            raise ValidationError("El seguro debe pertenecer a una compra o una venta.")
    
    @api.comstrains('importe')
    def _validar_importe(self):
        if self.importe < 0:
            raise ValidationError("El importe no puede ser negativo.")