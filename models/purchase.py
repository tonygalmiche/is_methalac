# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    is_adresse_livraison_id = fields.Many2one('res.partner', "Adresse de livraison")
    is_client_final_id      = fields.Many2one('res.partner', "Client final")
    is_contact_client_id    = fields.Many2one('res.partner', "Contact Client")
    is_contact_monteur_id   = fields.Many2one('res.partner', "Contact Monteur")
