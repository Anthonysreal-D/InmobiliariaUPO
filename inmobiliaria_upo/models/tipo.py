# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tipo(models.Model):
     _name = 'inmobiliaria_upo.tipo'
     _description = 'Tipo'

     idPropiedad = fields.Char(string="ID Propiedad", size=8, required=True)
     name = fields.Char(string="Tipo de inmueble", size=50, required=True)
     estado = fields.Selection([('estado1','Estado1'),
                                     ('estado2','Estado2'),
                                     ('estado3','Estado3'),
                                     ('estado4','Estado4'),],
                                     'Tipo de estado')

     ids_Propiedades = fields.One2many("inmobiliaria_upo.propiedad",'ids_Tipos','Propiedades')

     def btn_submit_to_estado1(self):
          self.write({'estado':'estado1'})

     def btn_submit_to_estado2(self):
          self.write({'estado':'estado2'})

     def btn_submit_to_estado3(self):
          self.write({'estado':'estado3'})

     def btn_submit_to_estado4(self):
          self.write({'estado':'estado4'})