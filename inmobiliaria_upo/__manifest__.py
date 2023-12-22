# -*- coding: utf-8 -*-
{
    'name': "Inmobiliaria UPO",

    'summary': "Gestion del modulo InmobiliariaUPO",

    'description': "El modulo permitira gestionar y manejar por parte de una empresa la compra/venta, alquiler y subatacion de diferentes inmuebles",

    'author': "TSI_G1",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Gestion',
    'version': '0.9',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'sale',
                'purchase'],


    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/reports.xml',
        'reports/seguro_report.xml',
        'reports/compra_report.xml',
        'reports/venta_report.xml',
        'views/cliente_view.xml',
        'views/propietario_view.xml',
        'views/empresa_views.xml',
        'views/subasta_views.xml',
        'views/puja_views.xml',
        'views/trabajador_views.xml',
        'views/venta_view.xml',
        'views/compra_view.xml',
        'views/seguro_view.xml',
        'views/alquiler_view.xml',
        'views/propiedad_view.xml',
        'views/tipo_view.xml',
        'views/visita_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        

    ],
    'assets':{
    	'web.assets_backend': [
            'inmobiliaria_upo/static/src/components/*/*.js',
            'inmobiliaria_upo/static/src/components/*/*.xml',
            'inmobiliaria_upo/static/src/components/*/*.scss',
    	],
    },
    'application': True,
    
}
