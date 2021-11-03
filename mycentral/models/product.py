# -*- coding: utf-8 -*-

from odoo import fields,models

class ProductTemplateInherit(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    
    date_test = fields.Datetime(string="Test Date",required=True)