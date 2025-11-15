# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolSubject(models.Model):
    _name = 'ibschool.school_subject'
    _description = 'SchoolSubject model'

    name = fields.Char(string='Name', required=True)
