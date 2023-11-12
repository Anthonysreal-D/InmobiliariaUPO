# -*- coding: utf-8 -*-
{
    'name': "InmobiliariaUPO",

    'summary': """Gestión del modulo de InmobiliariaUPO""",

    'description': """Gestión de personas, clientes, propietarios, operaciones como la compra, venta, alquiler y subasta, esta última con sus pujas, trabajadores, emrpesa, tipos de propiedades, visitas, propiedades y seguros""",

    'author': "Grupo 1-TSI-UPO",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/cliente_view.xml',
        'views/propietario_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}
