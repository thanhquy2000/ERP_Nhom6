from odoo import models, fields
from odoo.exceptions import UserError, ValidationError

class CentralCustomer(models.Model):
    _name = "central.teacher"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Central Teacher"
    
    name = fields.Char(string ='Name', required = True)
    middle_name = fields.Char(string = 'Middle Name', required = True)
    last_name = fields.Char(string ='Last Name', required = True)
    description = fields.Text('Teacher Description')
    image = fields.Binary("Teacher Image", attachment = True, help = "Teacher Image") 
    age = fields.Integer(string = 'Age')
    dob = fields.Date(string = "Date of Birth", required = True)
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string ='Gender')
    phone_number = fields.Char(string = 'Phone Number', required = True)
