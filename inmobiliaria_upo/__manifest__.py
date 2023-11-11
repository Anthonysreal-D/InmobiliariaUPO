# -*- coding: utf-8 -*-
{
    'name': "InmobiliariaUPO",

    'summary': """Gestion del modulo inmobiliariaUPO""",

    'description': """Gestion de venta, compra y alquiler de inmuebles.""",

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'sale',
                'purchase'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/venta_view.xml',
        'views/compra_view.xml',
        'views/seguro_view.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}