# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolAnnouncement(models.Model):
    _name = 'ibschool.school_announcement'
    _description = 'SchoolAnnouncement model'

    name = fields.Char(string='Name', required=True)
