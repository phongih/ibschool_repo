# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolEnrollment(models.Model):
    _name = 'ibschool.school_enrollment'
    _description = 'SchoolEnrollment model'

    name = fields.Char(string='Name', required=True)
