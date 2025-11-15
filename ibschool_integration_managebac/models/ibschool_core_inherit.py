# -*- coding: utf-8 -*-
from odoo import models, fields, api

class IbschoolCoreInherit(models.Model):
    _name = 'ibschool.ibschool_core_inherit'
    _description = 'IbschoolCoreInherit model'

    name = fields.Char(string='Name', required=True)
