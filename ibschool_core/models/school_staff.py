# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolStaff(models.Model):
    _name = 'ibschool.school_staff'
    _description = 'SchoolStaff model'

    name = fields.Char(string='Name', required=True)
