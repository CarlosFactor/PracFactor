# © 2021 FactorLibre - Carlos del Valle <carlos.delvalle@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, _                     


# Creamos la clase Cancion 
class RecordReservation(models.Model):                   
    _name = 'record.reservation'  
    _description = "Reservation"    
    _rec_name = "name_reservation"

    @api.model
    def _get_default_user(self):
        return self.env.user

    name_reservation = fields.Char("Name Reservation", default="New",readonly=True)
    client= fields.Many2one("res.partner", "Client", store=True)
    reservation_date= fields.Datetime("Reservation Date")
    reservation_line_ids = fields.Many2many("record.reservation.line", string= "Reservation line")
    user_id = fields.Many2one("res.users", "Employee", default=_get_default_user)

    state = fields.Selection(
        [
            ("draft","Draft"),
            ("complete","Complete"),
            ("canceled","Canceled"),
        ],
        "Reservation Status",
        default="draft",
    )

    total_reservation = fields.Float("Total reservation", compute="_compute_total_reservation")

    @api.onchange("reservation_line_ids")
    def _compute_total_reservation(self):
        total= 0
        for record in self:
            for line in record.reservation_line_ids:
                total += line.total_price
            record.total_reservation = total

    @api.model
    def create(self, vals):
        if vals.get('name_reservation', 'New') == 'New':
            vals['name_reservation'] = self.env['ir.sequence'].next_by_code('record.reservation') or 'New'
        result = super(RecordReservation, self).create(vals)
        return result
