
layerPath  = "C:\\myworld\\cgis\\adkforests\\nygis\\2ftInfrared_2003\\BlueMountainWildForest\\e_05221848_24_14400_cir_2003.sid"
layerName = "e_05221848_24_14400_cir_2003"
rasterLyr = QgsRasterLayer(layerPath, layerName)
layerIsValid = rasterLyr.isValid()

if layerIsValid:
    print("Path: " + layerPath)
    print("Name: " + layerName)
    print("Valid: " + str(layerIsValid))
    QgsProject.instance().addMapLayer(rasterLyr)

    # Height and Width
    rasterWidth = rasterLyr.width()
    rasterHeight = rasterLyr.height()
    print("Width: " + str(rasterWidth) )
    print("Height: " + str(rasterHeight) )

    unitsPerPixelX = rasterLyr.rasterUnitsPerPixelX()
    unitsPerPixelY = rasterLyr.rasterUnitsPerPixelY()

    print("Units Per Pixel X: " + str(unitsPerPixelX))
    print("Units Per Pixel Y: " + str(unitsPerPixelY))

    rasterBandsCount = rasterLyr.bandCount()
    print("Bands: " + str(rasterBandsCount))

    c = rasterLyr.extent().center()
    qry = rasterLyr.dataProvider().identify(c,QgsRaster.IdentifyFormatValue)
    qry.isValid()
    centerPointValues = qry.results()
    print("Center Point Values: " + str(centerPointValues))

else: 
    print("Invalid Raster")