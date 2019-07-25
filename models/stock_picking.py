# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import Warning


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def action_confirm(self):
        for obj in self:
            if obj.location_dest_id.id==obj.location_id.id:
                raise Warning(u"Emplacement source = Emplacement de destination")
            for move in obj.move_ids_without_package:
                move.location_id=obj.location_id.id
                move.location_dest_id=obj.location_dest_id.id
        self.mapped('package_level_ids').filtered(lambda pl: pl.state == 'draft' and not pl.move_ids)._generate_moves()
        # call `_action_confirm` on every draft move
        self.mapped('move_lines')\
            .filtered(lambda move: move.state == 'draft')\
            ._action_confirm()
        # call `_action_assign` on every confirmed move which location_id bypasses the reservation
        self.filtered(lambda picking: picking.location_id.usage in ('supplier', 'inventory', 'production') and picking.state == 'confirmed')\
            .mapped('move_lines')._action_assign()
        return True

