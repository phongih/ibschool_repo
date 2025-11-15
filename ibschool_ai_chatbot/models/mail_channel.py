# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MailChannel(models.Model):
    _name = 'ibschool.mail_channel'
    _description = 'MailChannel model'

    name = fields.Char(string='Name', required=True)
