# -*- coding: utf-8 -*-
{
    'name': "Central Management",
    'summary': """Central Management Software""",
    'description': """Central Management""",
    'author': "group6",
    'website': "https://group6.com",
    'category': 'Productivity',
    'version': '1.0',
    'depends': [
        'sale',
        'product',
        'hr',
        'base', 'mail',
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/mark.xml',
        'views/product.xml',
        'views/sale.xml',
        'views/hr.xml',
        'views/customer.xml',
        'reports/reports.xml',

    ],
    'demo': [],
    'qweb': ['static/src/xml/customer.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}