# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolTranscript(models.Model):
    _name = 'ibschool.school_transcript'
    _description = 'SchoolTranscript model'

    name = fields.Char(string='Name', required=True)
