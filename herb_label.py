"""
Author: M Maher

Date: 20171130

herb_label.py
Python class to define a herbarium label, to be produced from CSV -> JSON -> Mustache template -> HTML.

"""

class HerbLabel(object):
    #object initialized from a dictionary
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
        

    def geoTertiaryDivision(self):
        return self.geoTertiaryDivision

    def collector(self):
        return self.collector

    def collectionNumber(self):
        return self.collectionNumber

    def additionalCollectors(self):
        return self.additionalCollectors

    def family(self):
        return self.family

    def genus(self):
        return self.genus

    def geoSecondaryDivision(self):
        return self.geoSecondaryDivision

    def specificEpithet(self):
        return self.specificEpithet

    def authority(self):
        return self.authority

    def rank(self):
        return self.rank

    def infraspecificName(self):
        return self.infraspecificName

    def infraspecificAuthority(self):
        return self.infraspecificAuthority

    def ecology(self):
        return self.ecology

    def observations(self):
        return self.observations

    def elevation(self):
        return self.elevation

    def elevationUnit(self):
        return self.elevationUnit

    def locality(self):
        return self.locality

    def latitudeDecimal(self):
        return self.latitudeDecimal

    def longitudeDecimal(self):
        return self.longitudeDecimal

    def date(self):
        return self.date
