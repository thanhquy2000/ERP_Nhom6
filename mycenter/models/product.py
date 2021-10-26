# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleExam(models.Model):
    _inherit = "product.template"
    day = fields.Datetime(string="Test Date")



