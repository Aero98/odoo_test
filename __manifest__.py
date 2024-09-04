{
    'name': 'Material Registration',
    'version': '1.0',
    'summary': '',
    'description': """
       For Odoo Test Purpose Only
    """,
    'author': 'Fikri Anda',
    'website': '',
    'category': 'Inventory',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/material_views.xml',
        'views/supplier_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
