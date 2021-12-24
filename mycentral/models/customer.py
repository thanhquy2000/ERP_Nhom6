from odoo import fields, models


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    id_card = fields.Char(string='ID card', required='True')
    DateOfIssue = fields.Date(string='Date Of Issue', required='True')
    PlaceOfIssue = fields.Char(string='Place Of Issue', required='True')
    DateOfBirth = fields.Date(string='Date of Birth', required='True')
    gender = fields.Selection([('M', 'Male'),
                               ('F', 'Female'),
                               ('O', 'Other')],
                              string='Gender', required='True')
    vaccination_cus = fields.Selection([('No', 'No Vaccination'),
                                        ('one', '1 dose'),
                                        ('full', 'Fully vaccinated')],
                                    string='COVID-19 Vaccination')
