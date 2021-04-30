# © 2021 FactorLibre - Carlos del Valle <carlos.delvalle@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models                     # Importamos los campos y los modelos 


# Creamos la clase Disco 
class RecordRecord(models.Model):                   
    _name = 'record.record'      
    _rec_name = "title"     


    title = fields.Char("Titulo", required=True)    
    artist_ids = fields.Many2many("record.artist",string='Artists')
    genre_ids = fields.Many2many("musical.gender",string='Genre_ids')
    songs_ids = fields.Many2many("record.song",string= 'Songs_ids')
    image = fields.Binary("Image") 
    date = fields.Date()
    description = fields.Text("Description")        
    price = fields.Float()