# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleExam(models.Model):
    _inherit = "sale.order"
    id_card = fields.Char(string='ID card', related='partner_id.id_card')
    gender = fields.Selection([('M', 'Male'),
                               ('F', 'Female'),
                               ('O', 'Other')],
                              string='Gender', related='partner_id.gender')
    DateOfBirth = fields.Date(string='Date of Birth', related='partner_id.DateOfBirth')
    phone = fields.Char(string='Phone', related='partner_id.phone')
    email = fields.Char(string='Email', related='partner_id.email')
    function = fields.Char(string='Job position', related='partner_id.function')
    purpose = fields.Selection([('test', 'Test level'),
                                ('abroad ', 'Study abroad'),
                                ('apply', 'Apply for a job'),
                                ('other', 'Others')],
                               string='Purpose of attending')
    TookExam = fields.Selection([('no', 'Not Yet'),
                                ('b1 ', 'B1'),
                                ('toeic', 'Toeic'),
                                ('ielts', 'Ielts')],
                                string='Took the English exam')

    class SaleOrderLine(models.Model):
        _inherit = 'sale.order.line'
        product_test_date = fields.Datetime(string="Test Date", related='product_id.date_test', store=True)



