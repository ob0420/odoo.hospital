# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _
from odoo.exceptions import ValidationError

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string='Name')

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name'

    patient_name = fields.Char(string='Name', required=True,  track_visibility="always")
    patient_age = fields.Integer('Age', track_visibility="always")
    notes = fields.Text(string="Registration Note")
    image = fields.Binary(string="Image", attachment=True)
    name = fields.Char(string="Test")
    name_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result