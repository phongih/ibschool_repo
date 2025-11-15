# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResUsers(models.Model):
    _name = 'ibschool.res_users'
    _description = 'ResUsers model'

    name = fields.Char(string='Name', required=True)
