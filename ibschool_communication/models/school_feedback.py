# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolFeedback(models.Model):
    _name = 'ibschool.school_feedback'
    _description = 'SchoolFeedback model'

    name = fields.Char(string='Name', required=True)
