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
        'sale',
        'document',
        'product',
        'purchase',
        'purchase_stock',
    ],
    'data' : [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/res_partner_views.xml',
        'views/res_company_views.xml',
        'views/product_views.xml',
        'views/purchase_views.xml',
        'views/report_templates.xml',
        'views/report_invoice.xml',
        'views/stock_quant_views.xml',
        'views/stock_picking_views.xml',
        'views/menu.xml',
        'report/purchase_order_templates.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}

