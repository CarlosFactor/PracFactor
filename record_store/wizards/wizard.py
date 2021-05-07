from odoo import models, fields,api


class Wizard(models.TransientModel):
    _name = "wizard"

    artist = fields.Many2one(
        comodel_name='record.artist', string='artist', required = True)
