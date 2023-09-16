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


class EarthquakeShipment(models.Model):
    _name = 'earthquake.shipment'
    _rec_name = 'shipment_date'
    _description = 'Shipments made to locations'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    shipment_date = fields.Datetime('Shipment Date', required=True)
    # source_location_id = fields.Many2one('earthquake.location', string='Source Location', ondelete='set Numm')
    destination_location_id = fields.Many2one('earthquake.location', string='Destination Location', required=True, ondelete='cascade')
    vehicle_plate = fields.Char('Vehicle Plate Number')
    help_type_ids = fields.Many2many(
        string='Help Provided',
        comodel_name='earthquake.help.type',
        relation='earthquake_shipment_2_help_type',
        column1='help_type_id',
        column2='shipment_id',
    )
