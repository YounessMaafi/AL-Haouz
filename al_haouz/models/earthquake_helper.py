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


class HospitalHelper(models.Model):
    _name = 'hospital.helper'
    _description = 'Hospital/Helper'
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    def _default_color(self):
        return randint(1, 100)

    name = fields.Char('Name', required=True)
    phone = fields.Char('Phone')
    address = fields.Char('Address')
    description = fields.Text('Description')
    color = fields.Integer('Color Index')
