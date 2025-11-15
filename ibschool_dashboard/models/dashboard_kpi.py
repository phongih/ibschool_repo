# -*- coding: utf-8 -*-
from odoo import models, fields, api

class DashboardKpi(models.Model):
    _name = 'ibschool.dashboard_kpi'
    _description = 'DashboardKpi model'

    name = fields.Char(string='Name', required=True)
