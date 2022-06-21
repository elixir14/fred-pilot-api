from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping
from django.core.management import BaseCommand
import pandas as pd
from apps.mapbox.models import Shape

mapping = {
    'byggid': 'byggid',
    'bygningsnr': 'bygningsnr',
    'bebygdarea': 'bebygdarea',
    'bygningsty': 'bygningsty',
    'bygnings_1': 'bygnings_1',
    'kommunenav': 'kommunenav',
    'fylkesnavn': 'fylkesnavn',
    'matrikkeln': 'matrikkeln',
    'lagretbere': 'lagretbere',
    'lokalid': 'lokalid',
    'flood_Dept': 'flood_Dept',
    'basement': 'basement',
    'S_drponds': 'S_drponds',
    'S_filterst': 'S_filterst',
    'S_filterdr': 'S_filterdr',
    'S_dryswale': 'S_dryswale',
    'S_permpave': 'S_permpave',
    'S_filtertr': 'S_filtertr',
    'S_raingard': 'S_raingard',
    'S_RWH': 'S_RWH',
    'S_greenroo': 'S_greenroo',
    'S_infilttr': 'S_infilttr',
    'S_infilbas': 'S_infilbas',
    'S_soakaway': 'S_soakaway',
    'S_swdettan': 'S_swdettan',
    'SGM_drypro': 'SGM_drypro',
    'SGM_wetpro': 'SGM_wetpro',
    'SGM_pumpsu': 'SGM_pumpsu',
    'SGM_sandba': 'SGM_sandba',
    'SGM_fdoor': 'SGM_fdoor',
    'SGM_airbri': 'SGM_airbri',
    'SGM_NRvalv': 'SGM_NRvalv',
    'rx_3h_2010': 'rx_3h_2010',
    'rx_3h_2030': 'rx_3h_2030',
    'rx_3h_2050': 'rx_3h_2050',
    'rx_1d_2010': 'rx_1d_2010',
    'rx_1d_2030': 'rx_1d_2030',
    'rx_1d_2050': 'rx_1d_2050',
    'rx_5d_2010': 'rx_5d_2010',
    'rx_5d_2030': 'rx_5d_2030',
    'rx_5d_2050': 'rx_5d_2050',
    # 'Label': 'POINT',
    # 'Shape_Leng': 'Shape_Leng',
    'Shape_Area': 'POLYGON',
}


def import_shape_file(shape_file):
    ds = DataSource(shape_file)
    layer = ds[0]
    print(layer.fields)
    print(layer.get_fields("Shape_Leng"))
    # print(layer)
    # lm = LayerMapping(Shape, shape_file, mapping, transaction_mode='autocommit')
    # lm.save(verbose=True)


class Command(BaseCommand):

    def handle(self, **options):
        # shape_file = int(input("Please enter the shape file path: "))
        shape_file = "/home/akash/others/python/projects/fred-pilot-api/data/Fred_prop_suitability.shp"
        # import_shape_file(shape_file)

        file_path = 'data/Fred_pilot_Fremtind.xlsx'
        df = pd.read_excel(file_path)
        temp = df.to_dict()
        latitude = temp['Latitude']
        # print(latitude)
        longitude = temp['Longitude']
        # print(longitude)
        buiding_ID = temp['Buiding ID']
        # print(buiding_ID)

        main_data = {}
        for key, value in buiding_ID.items():
            main_data[f"{value}"] = {
                'latitude': latitude[key],
                'longitude': longitude[key]
            }
        # print(main_data)
        shape_objects = Shape.objects.all()
        for shape in shape_objects:
            # print(shape.byggid)
            data = main_data.get(str(shape.byggid))
            # print(data)
            shape.latitude = data['latitude']
            shape.longitude = data['longitude']
            shape.save()
            # break


