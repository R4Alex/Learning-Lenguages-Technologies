# -*- coding: utf-8 -*-
{
    'name': "Odootycoon",

    'summary': """
        Create a fun business Tycoon Game using Odoo's Framework""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Modoole Tech",
    'website': "https://www.modoole.com",

    'category': 'Uncategorized',
    'version': '12.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}