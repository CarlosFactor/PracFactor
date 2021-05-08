# © 2021 FactorLibre - Carlos del Valle<carlos.delvalle@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Gestion Taller",
    "depends": [
        'base',
    ],
    "version": "14.0.1.0.0",
    "author": "FactorLibre",
    "application": False,
    "installable": True,
    'data': [
        'security/ir.model.access.csv',
        "views/vehiculo_view.xml",
    ],
    'category': 'Gestion Vehiculo',
}
