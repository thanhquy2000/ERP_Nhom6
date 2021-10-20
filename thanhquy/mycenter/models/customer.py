# -*- coding: utf-8 -*-
from odoo import models, fields


class CentralCustomer(models.Model):
    _name = "central.customer"
    _description = "Central Customer"

    name = fields.Char(string='Name', required=True)
    middle_name = fields.Char(string='Middle Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    description = fields.Text('Customer Description')
    image = fields.Binary("Customer Image", attachment=True, help="Customer Image")
    age = fields.Integer(string='Age')
    dob = fields.Date(string="Date of Birth", required=True)
    company_id = fields.Many2one('res.company', string='Company', required=True)
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    ], string='Gender')
    id_card = fields.Char(string='ID Card', required=True)
    phone_number = fields.Char(string='Phone Number', required=True)
