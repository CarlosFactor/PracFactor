# © 2021 FactorLibre - Carlos del Valle <carlos.delvalle@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models                     # Importamos los campos y los modelos 


# Creamos la clase Cancion 
class RecordSong(models.Model):                   
    _name = 'record.song'      


    name = fields.Char("Name", required=True)
    artist_ids = fields.Many2many("record.artist", string="Artist_ids")
    duration = fields.Float("Duration")