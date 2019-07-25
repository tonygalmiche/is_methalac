# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    is_adresse_livraison_id = fields.Many2one('res.partner', "Adresse de livraison")
    is_client_final_id      = fields.Many2one('res.partner', "Client final")
    is_contact_client_id    = fields.Many2one('res.partner', "Contact Client")
    is_contact_monteur_id   = fields.Many2one('res.partner', "Contact Monteur")
    is_location_dest_id     = fields.Many2one('stock.location', "Emplacement de destination", domain=[('usage','=','internal')])


    @api.multi
    def _create_picking(self):
        """Permet de définir l'emplacement de destination à partir de celui indiqué sur la commande"""

        StockPicking = self.env['stock.picking']
        for order in self:
            if any([ptype in ['product', 'consu'] for ptype in order.order_line.mapped('product_id.type')]):
                pickings = order.picking_ids.filtered(lambda x: x.state not in ('done', 'cancel'))
                if not pickings:
                    res = order._prepare_picking()
                    if order.is_location_dest_id:
                        res['location_dest_id'] = order.is_location_dest_id.id
                    picking = StockPicking.create(res)
                else:
                    picking = pickings[0]
                moves = order.order_line._create_stock_moves(picking)
                if order.is_location_dest_id:
                    print(moves)
                    for move in moves:
                        print(move,move.location_dest_id)
                        move.location_dest_id = order.is_location_dest_id.id
                moves = moves.filtered(lambda x: x.state not in ('done', 'cancel'))._action_confirm()
                seq = 0
                for move in sorted(moves, key=lambda move: move.date_expected):
                    seq += 5
                    move.sequence = seq
                moves._action_assign()
                picking.message_post_with_view('mail.message_origin_link',
                    values={'self': picking, 'origin': order},
                    subtype_id=self.env.ref('mail.mt_note').id)
        return True

