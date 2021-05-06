# © 2021 FactorLibre - Carlos del Valle <carlos.delvalle@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models, _                     # Importamos los campos y los modelos 

class RecordArtist(models.Model):                   # Creamos la clase de los artistas 
    _name = 'record.artist'                         # Le damos nombre al ser una clase nueva. El guion del name es para que cambie dentro del modulo el punto
                                                    # por un guion bajo. 
    _description = "Artist"
    
    name = fields.Char("Name", required=True)       # Campo name que sera de tipo char, el nombre con el que aparecera y que será requerido 
    description = fields.Text("Description")        # Campo description que sera de tipo texto y el nombre con el que aparecera
    image = fields.Binary("Image")                  # Campo image que sera una imagen de tipo binario que luego desde la vista le diremos que es una imagen.
    
    record_ids = fields.Many2many("record.record",string='Record')


    # Esto es para que el nombre del artista sea unico y no se puedan repetir
    _sql_constraints = [                            
        (
            "name_uniq", 
            "unique(name)", 
            "There's allready created the artist name"
        )
    ]




