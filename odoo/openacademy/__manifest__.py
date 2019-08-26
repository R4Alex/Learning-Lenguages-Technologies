# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Alejandro Santillan Modoole Tech",
    'website': "https://modoole.com",


    'category': 'Uncategorized',
    'version': '12.0.0.1',

    'application': 'True',
    
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'board',
    ],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/partner.xml',
        'views/session_board.xml',
        'reports/reports.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}