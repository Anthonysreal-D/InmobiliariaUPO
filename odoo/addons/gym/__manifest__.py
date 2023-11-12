# -*- coding: utf-8 -*-
{
    'name': "gym",

    'summary': """Gestion del modulo gym""",

    'description': """Gestion de clases, usuarios, material, etc.""",

    'author': "TSI - UPO",
    'website': "https://www.upo.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/classes_views.xml',
        'views/users_view.xml',
        'views/instructores_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/gym.users.csv',
        'demo/gym.instructores.csv',
        'demo/gym.classes.csv',        
    ],
    'application': True,
}