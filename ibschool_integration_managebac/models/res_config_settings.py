# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResConfigSettings(models.Model):
    _name = 'ibschool.res_config_settings'
    _description = 'ResConfigSettings model'

    name = fields.Char(string='Name', required=True)
