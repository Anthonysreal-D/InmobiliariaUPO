# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subasta(models.Model):
     _name = 'inmobiliaria_upo.subasta'
     _description = 'Subasta'
     
     idSubasta = fields.Char(string="ID Subasta", required=True, help="ID de la subasta")
     valorInicial = fields.Char(string="Valor de inicio", required=True, help="Importe con el que se inicia la subasta")
     valorFinal = fields.Char(string="Ultimo valor", required=True, help="Ultimo importe pujado y con el que finalizaria la subasta")
     fecha = fields.Char(string="Fecha de la subasta", required=True, help="Fecha en la que se inicia la subasta")
