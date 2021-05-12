# © 2021 FactorLibre - Carlos del Valle<carlos.delvalle@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class Vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Gestion Vehiculos Odoo'

    name = fields.Char(
        string="Name",
        help="Introduce el nombre",
        size=20,
        default="Nuevo")
    active = fields.Boolean(string="Active")
    matricula = fields.Char(string="Placa")
