# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo 12 pour Methalac',
    'version'  : '0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',
    'description': """
InfoSaône - Module Odoo 12 pour Methalac
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'document',
        'product',
        'purchase',
    ],
    'data' : [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}

