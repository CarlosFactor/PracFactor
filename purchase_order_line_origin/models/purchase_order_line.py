# © 2021 FactorLibre - Carlos del Valle<carlos.delvalle@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    origin = fields.Char(string="Origin")


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_type = fields.Selection(
        string="Vendor Type",
        selection=[
            ('type', 'Type1'),
            ('type2', 'Type2'),
        ]
    )
