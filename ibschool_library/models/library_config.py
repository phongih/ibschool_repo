# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LibraryConfig(models.Model):
    _name = 'ibschool.library_config'
    _description = 'LibraryConfig model'

    name = fields.Char(string='Name', required=True)
