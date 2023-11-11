# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import operacion

class compra(models.Model):
    _inherit=["purchase.order","inmobiliaria_upo.operacion"]
    _name="inmobiliaria_upo.compra"
    _description="InmobiliariaUPO Compra"
    
    partner_id = fields.Many2one(required=False)