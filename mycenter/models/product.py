# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ProductTemplateInherit(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    date_test = fields.Datetime(string="Test Date", required=True)
    name_teacher = fields.Char(string='Teacher Name', required=True)