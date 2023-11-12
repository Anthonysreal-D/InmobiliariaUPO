# -*- coding: utf-8 -*-
# from odoo import http


# class InmobiliariaUpo(http.Controller):
#     @http.route('/inmobiliaria_upo/inmobiliaria_upo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inmobiliaria_upo/inmobiliaria_upo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inmobiliaria_upo.listing', {
#             'root': '/inmobiliaria_upo/inmobiliaria_upo',
#             'objects': http.request.env['inmobiliaria_upo.inmobiliaria_upo'].search([]),
#         })

#     @http.route('/inmobiliaria_upo/inmobiliaria_upo/objects/<model("inmobiliaria_upo.inmobiliaria_upo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inmobiliaria_upo.object', {
#             'object': obj
#         })
