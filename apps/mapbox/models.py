from django.contrib.gis.db import models


class Shape(models.Model):
    byggid = models.BigIntegerField(null=True, blank=True, verbose_name="Building ID")
    bygningsnr = models.BigIntegerField(null=True, blank=True, verbose_name="Building No")
    bebygdarea = models.BigIntegerField(null=True, blank=True, verbose_name="Build-area(sqm)")
    bygningsty = models.BigIntegerField(null=True, blank=True, verbose_name="Building type code")
    bygnings_1 = models.CharField(max_length=255, null=True, blank=True, verbose_name="Building type")
    kommunenav = models.CharField(max_length=255, null=True, blank=True, verbose_name="Kommune Name")
    fylkesnavn = models.CharField(max_length=255, null=True, blank=True, verbose_name="Country Name")
    matrikkeln = models.CharField(max_length=255, null=True, blank=True, verbose_name="Matrikkel No")
    lagretbere = models.FloatField(null=True, blank=True, verbose_name="Plot Area")
    lokalid = models.BigIntegerField(null=True, blank=True, verbose_name="Local ID(plot)")
    flood_Dept = models.FloatField(null=True, blank=True, verbose_name="Max Flood depth")
    basement = models.BigIntegerField(null=True, blank=True, verbose_name="Basement(Y/N)")
    S_drponds = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability DR ponds")
    S_filterst = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability filter strips")
    S_filterdr = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability filter drains")
    S_dryswale = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability dry swale")
    S_permpave = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability permeable pavements")
    S_filtertr = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability filter strips tr")
    S_raingard = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability rain gardens")
    S_RWH = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability rainwater harvesting")
    S_greenroo = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability greenroo")
    S_infilttr = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability infiltration trench")
    S_infilbas = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability infiltration basin")
    S_soakaway = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability soakaway")
    S_swdettan = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability_Stormwater detention tank")
    SGM_drypro = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability (grey measures)_Dryproofing")
    SGM_wetpro = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability (grey measures)_Wetproofing")
    SGM_pumpsu = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability (grey measures)_Pumpsump")
    SGM_sandba = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability (grey measures)_Sandbagging")
    SGM_fdoor = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability (grey measures)_Flood doors")
    SGM_airbri = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability (grey measures)_Airbrick covers")
    SGM_NRvalv = models.CharField(max_length=255, null=True, blank=True, verbose_name="Suitability (grey measures)_Non-return valves")
    rx_3h_2010 = models.BigIntegerField(null=True, blank=True, verbose_name="Max 3h precipitation 2010")
    rx_3h_2030 = models.BigIntegerField(null=True, blank=True, verbose_name="Max 3h precipitation 2030")
    rx_3h_2050 = models.BigIntegerField(null=True, blank=True, verbose_name="Max 3h precipitation 2050")
    rx_1d_2010 = models.BigIntegerField(null=True, blank=True, verbose_name="Max 1d precipitation 2010")
    rx_1d_2030 = models.BigIntegerField(null=True, blank=True, verbose_name="Max 1d precipitation 2030")
    rx_1d_2050 = models.BigIntegerField(null=True, blank=True, verbose_name="Max 1d precipitation 2050")
    rx_5d_2010 = models.BigIntegerField(null=True, blank=True, verbose_name="Max 5d precipitation 2010")
    rx_5d_2030 = models.BigIntegerField(null=True, blank=True, verbose_name="Max 5d precipitation 2030")
    rx_5d_2050 = models.BigIntegerField(null=True, blank=True, verbose_name="Max 5d precipitation 2050")
    Label = models.PolygonField(srid=4269, null=True)
    Shape_Leng = models.PolygonField(srid=4269, null=True)
    Shape_Area = models.PolygonField(srid=4269, null=True)
    latitude = models.FloatField(null=True, blank=True, verbose_name="latitude")
    longitude = models.FloatField(null=True, blank=True, verbose_name="longitude")