# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_format_note = fields.Selection([
            ('normal'   , 'Normal'),
            ('gras'  , 'Gras'),
            ('rouge-gras', 'Rouge gras'),
        ], u"Format note",help=u"Article spécial utilisé pour les commandes fournisseur pour mettre une note entre les lignes des articles")


