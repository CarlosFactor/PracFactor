# © 2021 FactorLibre - Carlos del Valle<carlos.delvalle@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, fields


class OrdenReparacion(models.Model):
    _name = 'taller.orden.reparacion'
    _description = 'Gestion Ordenes Reparacion'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(
        string="Name",
        help="Introduce el nombre",
        default="Nueva Orden Reparacion")

    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Cliente")

    @api.model
    def create(self, vals):
        new_seq_name = vals['name'] = self.env['ir.sequence'].next_by_code(
            'orden.reparacion') or 'New'
        vals.update(name=new_seq_name)
        res = super(OrdenReparacion, self).create(vals)
        return res

    reparacion_line_ids = fields.One2many(
        comodel_name="taller.orden.reparacion.line",
        inverse_name="reparacion_id",
        string="lineas Reparacion"
    )
