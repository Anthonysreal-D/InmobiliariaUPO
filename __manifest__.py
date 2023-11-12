# -*- coding: utf-8 -*-
{
    'name': "Inmobiliaria UPO",

    'summary': "Gestion del modulo InmobiliariaUPO",

    'description': "El modulo permitira gestionar y manejar por parte de una empresa la compra/venta, alquiler y subatacion de diferentes inmuebles",

    'author': "Antonio Real TSI_G1",
    'website': "https://twitter.com/anthonysreal",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Gestion',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/empresa_views.xml',
        'views/subasta_views.xml',
        'views/puja_views.xml',
        'views/trabajador_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/inmobiliaria_upo.empresa.csv',
        'demo/inmobiliaria_upo.trabajador.csv',
        'demo/inmobiliaria_upo.subasta.csv',
        'demo/inmobiliaria_upo.puja.csv',

    ],
    'application': True,
}
