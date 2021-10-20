# -*- coding: utf-8 -*-
{
    'name': "Central Management",
    'summary': """Central Management Software""",
    'description': """Central Management Software""",
    'author': "group6.info",
    'website': "https://group6.info",
    'category': 'Productivity',
    'version': '1.0',
    'depends': ['sale',
                'mail'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/customer.xml',
        'views/sale.xml',
        ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}