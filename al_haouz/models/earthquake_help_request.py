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


class EarthquakeHelpRequest(models.Model):
    _name = 'earthquake.help.request'
    _description = 'Help Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title')
    description = fields.Text(string='Description')
    location_id = fields.Many2one('earthquake.location', string='Location', required=True, ondelete='cascade')
