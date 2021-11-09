# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Mark(models.Model):
    _name = "mark"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Customer Mark"

    name = fields.Many2one('res.partner', string='Name', required=True)
    image = fields.Binary(related='name.image_1920', readonly=False, related_sudo=False)
    exam_board = fields.Char(string='The Exam Board of members', required=True)
    age = fields.Integer(related='name.age', readonly=False, related_sudo=False, string='Age')
    exam_name = fields.Many2one('sale.order.line', string='Exam Name')
    mark_reading = fields.Float(string='Mark of Reading', required=True)
    mark_listening = fields.Float(string='Mark of Listening', required=True)
    mark_writing = fields.Float(string='Mark of Writing', required=True)
    mark_speaking = fields.Float(string='Mark of Speaking', required=True)
    total_score = fields.Float(string='Total Score', compute='_compute_total_score')

    @api.depends('mark_reading', 'mark_listening', 'mark_writing', 'mark_speaking')
    def _compute_total_score(self):
        for record in self:
            record.total_score = record.mark_reading + record.mark_listening + record.mark_writing + record.mark_speaking

