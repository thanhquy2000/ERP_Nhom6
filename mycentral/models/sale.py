# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleExam(models.Model):
    _inherit = "sale.order"
    state = fields.Selection(selection_add=[('disable', 'Disabled')],
                             string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    PhoneNumber = fields.Char(string='Phone Number', required=False)

    def action_disable(self):
        self.state = 'disable'