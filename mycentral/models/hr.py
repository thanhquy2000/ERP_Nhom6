# -*- coding: utf-8 -*-
from odoo import fields, models, api



class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    vaccination = fields.Selection([('No', 'No Vaccination'),
                                    ('one', '1 dose'),
                                    ('full', 'Fully vaccinated')],
                                   string='COVID-19 Vaccination')



