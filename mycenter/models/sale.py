# -*- coding: utf-8 -*-
from odoo import fields, models

class SaleExam(models.Model):
    _inherit = "sale.order"

    PhoneNumber =fields.Char(string='Phone Number', required=False)
    dob = fields.Date(string="Date of Birth", required=False)
    id_card = fields.Char(string="ID card", required=False)