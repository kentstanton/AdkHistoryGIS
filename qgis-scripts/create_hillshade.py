import processing
import os


dems = [
"b36elu.dem","b37elu.dem","b38elu.dem","b39elu.dem","b40elu.dem","b41elu.dem","b42elu.dem","b43elu.dem","b44elu.dem","b45elu.dem","b46elu.dem","b47elu.dem","b48elu.dem",
"b49elu.dem","b50elu.dem","b51elu.dem","c36elu.dem","c37elu.","em","c38elu.dem","c39elu.dem","c40elu.dem","c41elu.dem","c42elu.dem","c43elu.dem","c44elu.dem","c45elu.dem",
"c46elu.dem","c47elu.dem","c48elu.dem","c49elu.dem","c50elu.dem","c51elu.dem","d36elu.dem","d37elu.dem","d38elu.dem","d","9elu.dem","d40elu.dem","d41elu.dem","d42elu.dem",
"d43elu.dem","d44elu.dem","d45elu.dem","d46elu.dem","d47elu.dem","d48elu.dem","d49elu.dem","d50elu.dem","d51elu.dem","e36elu.dem","e37elu.dem","e38elu.dem","e39elu.dem",
"e40elu.d","m","e41elu.dem","e42elu.dem","e43elu.dem","e44elu.dem","e45elu.dem","e46elu.dem","e47elu.dem","e48elu.dem","e49elu.dem","e50elu.dem","e51elu.dem","f34elu.dem",
"f35elu.dem","f36elu.dem","f37elu.dem","f38elu.dem","f39elu.dem","f4","elu.dem","f41elu.dem","f42elu.dem","f43elu.dem","f44elu.dem","f45elu.dem","f46elu.dem","f47elu.dem",
"f48elu.dem","f49elu.dem","f50elu.dem","f51elu.dem","g34elu.dem","g35elu.dem","g36elu.dem","g37elu.dem","g38elu.dem","g39elu.dem","g40elu.dem","g41elu.dem","g42elu.dem","g43elu.dem",
"g44elu.dem","g45elu.dem","g46elu.dem","g47elu.dem","g48elu.dem","g49elu.dem","g50elu.dem","g51elu.dem","h34elu.dem","h35elu.dem","h36elu.dem","h37elu.dem","h38elu.dem","h39el",".dem",
"h40elu.dem","h41elu.dem","h42elu.dem","h43elu.dem","h44elu.dem","h45elu.dem","h46elu.dem","h47elu.dem","h48elu.dem","h49elu.dem","h50elu.dem","h51elu.dem","i34elu.dem","i35elu.dem",
"i36elu.dem","i37elu.dem","i38elu.dem","i39elu.dem","i40elu.dem","i41elu.dem","i42elu.dem","i43elu.dem","i44elu.dem","i45elu.dem","i46elu.dem","i47elu.dem","i48elu.dem","i49elu.dem",
"i50elu.dem","i51elu.dem","j34elu.dem","j35elu.dem","j36elu.dem","j37elu.dem","j38elu.d","m","j39elu.dem","j40elu.dem","j41elu.dem","j42elu.dem","j43elu.dem","j44elu.dem","j45elu.dem",
"j46elu.dem","j47elu.dem","j48elu.dem","j49elu.dem","j50elu.dem","j51elu.dem","k34elu.dem","k35elu.dem","k36elu.dem","k37elu.dem","k3","elu.dem","k39elu.dem","k40elu.dem","k41elu.dem",
"k42elu.dem","k43elu.dem","k44elu.dem","k45elu.dem","k46elu.dem","k47elu.dem","k48elu.dem","k49elu.dem","k50elu.dem","k51elu.dem","l34elu.dem","l35elu.dem","l36elu.dem","l37elu.dem",
"l38elu.dem","l39elu.dem","l40elu.dem","l41elu.dem","l42elu.dem","l43elu.dem","l44elu.dem","l45elu.dem","l46elu.dem","l47elu.dem","l48elu.dem","l49elu.dem","l50elu.dem","l51elu.dem",
"m34elu.dem","m35elu.dem","m36elu.dem","m37el",".dem","m38elu.dem","m39elu.dem","m40elu.dem","m41elu.dem","m42elu.dem","m43elu.dem","m44elu.dem","m45elu.dem","m46elu.dem","m47elu.dem",
"m48elu.dem","m49elu.dem","m50elu.dem","n38elu.dem","n39elu.dem","n40elu.dem","n41elu.dem","n42elu.dem","n43elu.dem","n44elu.dem","n45elu.dem","n46elu.dem","n47elu.dem","n48elu.dem",
"n49elu.dem","o38elu.dem","o39elu.dem","o40elu.dem","o41elu.dem","o42elu.dem","o43elu.dem","o44elu.dem","o45elu.dem","o46elu.dem","o47elu.dem","o48elu.dem","o49elu.d","m","p38elu.dem",
"p39elu.dem","p40elu.dem","p41elu.dem","p42elu.dem","p43elu.dem","p44elu.dem","p45elu.dem","p46elu.dem","p47elu.dem","p48elu.dem","p49elu.dem","q44elu.dem","q45elu.dem","q46elu.dem",
"q47elu.dem","q48elu.dem","q49elu.dem","k38elu.dem","j38elu.dem","h39elu.dem","q40elu.dem","f40elu.dem","e40elu.dem"
]



layerPath  = "C:\\myworld\\cgis\\adkforests\\cugir-10m-all-adk\\"
counter = 1
for layerName in dems:
    #print(os.path.basename(path))
    
    fullPath = layerPath + layerName 
    rasterLyr = QgsRasterLayer(fullPath, layerName)
    layerIsValid = rasterLyr.isValid()

    if layerIsValid:
        print("Valid Raster")
        outputPath = layerPath + layerName + "_hillshade.tif"
        print(outputPath)
        parameters = {'INPUT': rasterLyr, 
                    'BAND': 1, 
                    'COMPUTE_EDGES': False,
                    'ZEVENBERGEN': False,
                    'Z_FACTOR': 1.0,
                    'SCALE': 1.0,
                    'AZIMUTH': 315,
                    'COMBINED': False,
                    'ALTITUDE': 45,
                    'MULTIDIRECTIONAL': False,
                    'OUTPUT': outputPath}

        processing.runAndLoadResults('gdal:hillshade',parameters)
        counter = counter + 1
    else: 
        print("Invalid Raster")