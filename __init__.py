# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AlBA
                                 A QGIS plugin
 Buchauskunft ALKIS Flurstücke
                             -------------------
        begin                : 2016-02-08
        copyright            : (C) 2016 by GIS_WG
        email                : info@giswg.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AlBA class from file AlBA.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .al_ba import AlBA
    return AlBA(iface)
