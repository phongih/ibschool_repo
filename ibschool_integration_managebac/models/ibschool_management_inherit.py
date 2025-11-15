# -*- coding: utf-8 -*-
from odoo import models, fields, api

class IbschoolManagementInherit(models.Model):
    _name = 'ibschool.ibschool_management_inherit'
    _description = 'IbschoolManagementInherit model'

    name = fields.Char(string='Name', required=True)
