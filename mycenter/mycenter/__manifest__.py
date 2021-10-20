# -*- coding: utf-8 -*-
{
    'name': 'Central Management',
    'version': '1.0',
    'summary': 'Central Management Software',
    'author': 'group6.info',
    'sequence': -100,
    'description': """Central Management Software""",
    'category': 'Productivity',
    'website': 'https://www.group6.info',
    'license': 'LGPL-3',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer.xml',
        'views/sale.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
