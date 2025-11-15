# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AdmissionLead(models.Model):
    _name = 'ibschool.admission_lead'
    _description = 'AdmissionLead model'

    name = fields.Char(string='Name', required=True)
