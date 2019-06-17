# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    is_capital                          = fields.Char("Capital")
    is_courriel_facturation_fournisseur = fields.Char("Courriel facturation fournisseur")

