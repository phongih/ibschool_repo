# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolOrganization(models.Model):
    _name = 'ibschool.school_organization'
    _description = 'SchoolOrganization model'

    name = fields.Char(string='Name', required=True)
