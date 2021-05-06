# © 2021 FactorLibre - Carlos del Valle <carlos.delvalle@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Record Store",
    "depends": [
        'base',
    ],
    "version": "14.0.1.0.0",
    "author": "FactorLibre",
    "application": False,
    "installable": True,
    "data": [
        'security/record_store_security.xml',
        'security/ir.model.access.csv',
        'views/record_store_menu.xml',
        'views/record_artist_view.xml',
        'views/musical_gender_view.xml',
        'views/record_record_view.xml',
        'views/record_song_view.xml',
        'views/record_reservation_view.xml',
        'data/reservation_sequence.xml',
    ],
    "category": ""
}

# Indicaremos los siguientes campos:
# - name= nombre del modulo 
# - depends= dependecias que de momento seran la base
# - version= version 
# - author= autor del modulo
# - application= pondremos siempre False
# - installable= se suele poner para que al subir el codigo a produccion no aparezca y no se pueda instalar el modulo 
# - data= sera para las vistas, security... Los intalaremos en orden, primero security y luego xml  
# - category=