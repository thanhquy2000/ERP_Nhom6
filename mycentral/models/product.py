# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ProductTemplateInherit(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    date_test = fields.Datetime(string="Test Date", required=True)
    Exam_ID = fields.Char(string="Exam ID", required=True)
    exam_type = fields.Selection([('B1', 'B1'),
                                  ('Toeic', 'Toeic'),
                                  ('Toelf', 'Toelf'),
                                  ('Ielts', 'Ielts')],
                                 string='Exam Type')


