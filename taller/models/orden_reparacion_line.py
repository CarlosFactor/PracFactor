# © 2021 FactorLibre - Carlos del Valle<carlos.delvalle@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class OrdenReparacionLine(models.Model):
    _name = 'taller.orden.reparacion.line'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(
        string="Name",
        help="Introduce el nombre",
        default="Nueva Orden Reparacion")

    reparacion_id = fields.Many2one(
        comodel_name="taller.orden.reparacion")

    vehiculo_id = fields.Many2one(
        comodel_name="taller.vehiculo", string="Vehiculo")
