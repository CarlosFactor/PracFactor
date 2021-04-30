# © 2021 FactorLibre - Carlos del Valle <carlos.delvalle@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class RecordMusicalGenre(models.Model):
    _name = 'record.musical.genre'
    _rec_name = "genre"

    genre = fields.Char("genre")
