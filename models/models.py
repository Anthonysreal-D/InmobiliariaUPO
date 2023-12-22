# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class inmobiliaria_upo(models.Model):
#     _name = 'inmobiliaria_upo.inmobiliaria_upo'
#     _description = 'inmobiliaria_upo.inmobiliaria_upo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
