# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LmsSubmission(models.Model):
    _name = 'ibschool.lms_submission'
    _description = 'LmsSubmission model'

    name = fields.Char(string='Name', required=True)
