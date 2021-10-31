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
        'hr'
        ],
    'data': [
        'views/product.xml',
        'views/sale.xml',
        'views/hr.xml'
        ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}