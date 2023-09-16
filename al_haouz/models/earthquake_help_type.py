# -*- coding: utf-8 -*-

import datetime
import base64
import io
import openpyxl
import re
from random import randint
import pyproj
import psycopg2

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo import models, fields


class EarthquakeHelpType(models.Model):
    _name = 'earthquake.help.type'
    _description = 'Help Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _default_color(self):
        return randint(1, 100)

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    color = fields.Integer('Color Index')
