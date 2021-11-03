# -*- coding: utf-8 -*-
from odoo import fields,models, api

class Mark(models.Model):
    _name = "mark"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Customer Mark"


    name = fields.Many2one('res.partner', string ='Name', required = True)
    image = fields.Binary(related='name.image_1920', readonly=False, related_sudo=False)
    exam_name = fields.Many2one('sale.order.line', string ='Exam Name')
    total_score = fields.Float(related='name.mark', readonly=False, related_sudo=False, string='Total Score', compute='_get_sum')
    mark_reading = fields.Float(string = 'Mark of Reading', required=True)
    mark_listening = fields.Float(string = 'Mark of Listening', required=True)
    mark_writing = fields.Float(string = 'Mark of Writing', required=True)
    mark_speaking = fields.Float(string = 'Mark of Speaking', required=True)
    
@api.depends('mark_reading', 'mark_listening', 'mark_writing', 'mark_speaking')
def _get_sum(self):
    for rec in self:
        rec.update({
            'total_score': rec.mark_reading+rec.mark_listening+rec.mark_writing+rec.mark_speaking,
            })
    