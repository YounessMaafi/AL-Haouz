# -*- coding: utf-8 -*-

{
    'name': 'AL Haouz',
    'version': '1.0',
    'description': """
AL Haouz - First Aid Priorities
=======================================
AL Haouz - First Aid Priorities
    """,
    'website': 'https://al-haouz.org',
    'depends': [
        # Odoo Standard Edition
        'base',
        'mail',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        'security/haouz_security.xml',
        # Views
        'views/earthquake_help_request.xml',
        'views/earthquake_help_type.xml',
        'views/earthquake_helper.xml',
        'views/earthquake_location.xml',
        'views/earthquake_shipment.xml',
        # Crons
        'data/ir_cron.xml',

    ],
    'installable': True,
}
