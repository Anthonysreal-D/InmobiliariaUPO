# -*- coding: utf-8 -*-
{
    'name': "inmobiliaria_upo",

    'summary': """Gestion del modulo inmobiliariaUPO""",

    'description': """
        El modulo permitira gestionar y manejar por parte de una empresa
        la compra/venta, alquiler y subatacion de diferentes inmuebles
    """,

    'author': "Antonio Real TSI_G1",
    'website': "https://twitter.com/anthonysreal",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
