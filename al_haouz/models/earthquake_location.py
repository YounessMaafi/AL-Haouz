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


class EarthquakeLocation(models.Model):
    _name = 'earthquake.location'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Locations affected by earthquake'

    name = fields.Char('Location Name in Arabic', required=True)
    name2 = fields.Char('Location Name (FR)')
    display_name = fields.Char(string='Full Name', compute='_compute_display_name', store=True)
    is_accessible = fields.Boolean('Accessible ?')
    city = fields.Char('Nearest City')
    commune_state = fields.Char('Commune/State')
    description = fields.Text('More Details')
    intensity = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string='Humanitarian Intensity')
    shipment_ids = fields.One2many(
        string='Shipments',
        comodel_name='earthquake.shipment',
        inverse_name='destination_location_id',
    )
    help_type_ids = fields.Many2many(
        string='Help Needed ( Multi )',
        comodel_name='earthquake.help.type',
        relation='earthquake_location_help_type',
        column1='help_type_id',
        column2='location_id',
    )
    hospital_helper_ids = fields.Many2many(
        string='Nearest Hospital/Help',
        comodel_name='hospital.helper',
        relation='earthquake_location_hospital_helper',
        column1='hospital_helper_id',
        column2='location_id',
    )

    the_point = fields.Char("Coordinate")
    total_shipments = fields.Float("Total Shipments", index=True, readonly=True)
    overall_percent_shipments = fields.Float("Overall % Shipments", index=True, readonly=True)



    import_filename = fields.Char(
        string='Import File Name',
        tracking=True,
    )
    import_file = fields.Binary(
        string='Import File',
        tracking=True,
    )

    @api.depends('name', 'name2')
    def _compute_display_name(self):
        for record in self:
            if record.name2:
                record.display_name = f"{record.name} - {record.name2}"
            else:
                record.display_name = f"{record.name}"

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = ['|', ('name', operator, name), ('name2', operator, name)]
        records = self.search(domain + args, limit=limit)
        return records.name_get()

    @api.model
    def _compute_shipments_data(self):
        # Update the logic to compute total_shipments and overall_percent_shipments
        locations = self.search([])
        shipments_count = self.env['earthquake.shipment'].search_count([])
        for location in locations:
            location.total_shipments = len(location.shipment_ids)
            location.overall_percent_shipments = (location.total_shipments / shipments_count) * 100
