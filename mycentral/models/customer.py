from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age <= 5:
                raise ValidationError(('The age must be greater than 5'))

    id_card = fields.Char(string='ID card', required=True)
    age = fields.Integer(string='Age', track_visibility='always')
    mark = fields.Float(string='Mark', required=True)