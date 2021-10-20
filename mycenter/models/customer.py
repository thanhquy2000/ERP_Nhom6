from odoo import models, fields
from odoo.exceptions import UserError, ValidationError
import string

class CentralCustomer(models.Model):
    _name = "central.customer"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Central Customer"
    
    name = fields.Char(string ='Name', required = True)
    middle_name = fields.Char(string = 'Middle Name', required = True)
    last_name = fields.Char(string ='Last Name', required = True)
    description = fields.Text('Customer Description')
    image = fields.Binary("Customer Image", attachment = True, help = "Customer Image") 
    age = fields.Integer(string = 'Age')
    dob = fields.Date(string = "Date of Birth", required = True)
    company_id = fields.Many2one('res.company', string='Company', required= True)
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string ='Gender')
    id_card = fields.Char(string = 'ID Card', required = True)
    phone_number = fields.Char(string = 'Phone Number', required = True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default = 'draft', string = 'Status')
    
    
    def action_confirm(self):
        self.state = 'confirm'
        
    def action_done(self):
        self.state = 'done'
        
    def action_draft(self):
        self.state = 'draft'
        
    def action_cancel(self):
        self.state = 'cancel'
    
