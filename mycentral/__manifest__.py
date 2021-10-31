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
        'product'
                ],
    'data': [
        'views/product.xml',
        'views/sale.xml'
        ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}