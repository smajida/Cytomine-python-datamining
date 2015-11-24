# -*- coding: utf-8 -*-
"""
Copyright 2010-2013 University of Liège, Belgium.

This software is provided 'as-is', without any express or implied warranty.
In no event will the authors be held liable for any damages arising from the
use of this software.

Permission is only granted to use this software for non-commercial purposes.
"""

__author__ = "Begon Jean-Michel <jm.begon@gmail.com>"
__copyright__ = "Copyright 2010-2013 University of Liège, Belgium"
__version__ = '0.1'

import abc

class DataStore(object):
    """
    =========
    DataStore
    =========
    A :class:`DataStore` encapsulates all the information about the data
    required by a given SLDC workflow.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_main_slide_stream(self):
        """
        Return
        ------
        slide_stream : :class:`SlideStream`
            The :class:`SlideStream` encapsulating the slides to process
        """
        pass

    @abc.abstractmethod
    def store_polygons(self, dict_polygons):
        """
        Stores the given polygons in the datastore

        Parameters
        ----------
        dict_polygons : a dictionary of polygons
                    (:class:`shapely.Polygon`)
            key = image_id => sequence of polygons
            The polygons are expressed in "real" coordinates
            (from the bottom left corner of the enclosing image)
        """
        self.dict_polygons = dict_polygons

    def get_polygons(self):
        """
        Return
        -----
        dict_polygons : a dictionary of polygons
                    (:class:`shapely.Polygon`)
            key = image_id => sequence of polygons
            The polygons are expressed in "real" coordinates
            (from the bottom left corner of the enclosing image)
        """
        return self.dict_polygons

class ThyroidDataStore(DataStore):
    """
    ================
    ThyroidDataStore
    ================
    A :class:`DataStore` dedicated to the thyroid cell classification
    application
    """
    __metaclass__ = abc.ABCMeta

    #---------------ThyroidDataStore---------------------#
    @abc.abstractmethod
    def store_cell(self, img_id, polygon):
        """
        Store the given polygon representing a cell

        Parameters
        ----------
        polygon : shapely.Polygon
            The polygon representing the cell
        """
        pass

    @abc.abstractmethod
    def store_aggregate(self, img_id, polygon):
        """
        Store the given polygon representing an aggregate

        Parameters
        ----------
        polygon : shapely.Polygon
            The polygon representing the aggregate
        """
        pass

    @abc.abstractmethod
    def store_architectural_pattern(self, img_id, polygon):
        """
        Store the given polygon representing an architectural pattern

        Parameters
        ----------
        polygon : shapely.Polygon
            The polygon representing the architectural pattern
        """
        pass

    @abc.abstractmethod
    def store_crop_to_segment(self, indices_and_polygons):
        """
        Return an :class:`SlideBuffer` where each slides are comprised of
        only the crops of the given polygons

        Parameters
        ----------
        indices_and_polygons : sequence of pairs (id, polygon)
            id : int
                The id of the slide where the polygon belongs
            polygon : :class:`shapely.Polygon`
                The polygon whose crop to get.
        Return
        ------
        slide_buffer : an :class:`SlideBuffer`
            A buffer where each slides are comprised of only the crops of the
            given polygons
        """
        pass

    @abc.abstractmethod
    def get_cells_to_classify(self):
        """
        Return
        ------
        An sequence of images depicting the cell to classify
        """
        pass

    @abc.abstractmethod
    def get_arch_pattern_to_classify(self):
        """
        Return
        ------
        An sequence of images depicting the architectural pattern to classify
        """
        pass

    @abc.abstractmethod
    def second_segmentation(self):
        """
        Switch to the second segmentation phase
        """
        pass

    @abc.abstractmethod
    def publish_results(self, cell_classif, arch_pattern_classif):
        pass