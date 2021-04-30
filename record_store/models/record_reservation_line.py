# © 2021 FactorLibre - Carlos del Valle <carlos.delvalle@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, _                     # Importamos los campos y los modelos 


# Creamos la clase Cancion 
class RecordReservationLine(models.Model):                   
    _name = 'record.reservation.line'      
    _rec_name = "name_reservation_line"

    name_reservation_line = fields.Char("Description", required=True,related="record.title")
    record = fields.Many2one("record.record", "Record")
    artist_id = fields.Many2many("record.artist", "Artist")
    price = fields.Float("Price Record", related="record.price")
    reservation_unit = fields.Integer("Reserved Units", default = "1")
    client = fields.Many2one("res.partner", "Client")
    total_price = fields.Float("Total Price", compute="_compute_total_reservation")

    @api.onchange("reservation_unit")
    def _compute_total_reservation(self):
        for record in self: 
            record.total_price += record.price * record.reservation_unit

    # Esto podemos quitarlo por el uso del related en los campos 
    @api.onchange("record")
    def _onchange_record(self):
        if self.record:
            # self.name_reservation_line = self.record.title
            self.artist_id = self.record.artist_ids
            # self.price = self.record.price