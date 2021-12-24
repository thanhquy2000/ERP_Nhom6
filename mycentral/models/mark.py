# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.addons.test_convert.tests.test_env import record


class Mark(models.Model):
    _name = "mark"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Customer Mark"

    partner = fields.Many2one('sale.order', string='ID', required=True)
    name = fields.Many2one(related='partner.partner_id', string='Customer Name')
    image = fields.Binary(related='name.image_1920', readonly=False, related_sudo=False, string='Customer Image')
    exam_board = fields.Char(string='The Exam Board of members', required=True)
    DateOfBirth = fields.Date(string='Date Of Birth', related='partner.DateOfBirth')
    id_card = fields.Char(string='ID card', related='partner.id_card')
    exam_name = fields.Many2one('sale.order.line', string='Exam Name')
    date_test = fields.Datetime(related='exam_name.product_test_date', readonly=False, related_sudo=False,
                                string='Test Date')
    mark_reading = fields.Float(string='Mark of Reading', required=True)
    mark_listening = fields.Float(string='Mark of Listening', required=True)
    mark_writing = fields.Float(string='Mark of Writing', required=True)
    mark_speaking = fields.Float(string='Mark of Speaking', required=True)
    total_score = fields.Float(string='Total Score', compute='_compute_total_score')

    @api.depends('mark_reading', 'mark_listening', 'mark_writing', 'mark_speaking')
    def _compute_total_score(self):
        for record in self:
            record.total_score = record.mark_reading + record.mark_listening + record.mark_writing + record.mark_speaking

    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('mark') or ('New')
        res = super(Mark, self).create(vals)
        return res