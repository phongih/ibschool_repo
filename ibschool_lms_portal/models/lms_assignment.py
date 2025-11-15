# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LmsAssignment(models.Model):
    _name = 'ibschool.lms_assignment'
    _description = 'LmsAssignment model'

    name = fields.Char(string='Name', required=True)
