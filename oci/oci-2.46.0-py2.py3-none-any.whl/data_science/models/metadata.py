# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Metadata(object):
    """
    Defines properties of each model metadata.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Metadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Metadata.
        :type key: str

        :param value:
            The value to assign to the value property of this Metadata.
        :type value: str

        :param description:
            The value to assign to the description property of this Metadata.
        :type description: str

        :param category:
            The value to assign to the category property of this Metadata.
        :type category: str

        """
        self.swagger_types = {
            'key': 'str',
            'value': 'str',
            'description': 'str',
            'category': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'value': 'value',
            'description': 'description',
            'category': 'category'
        }

        self._key = None
        self._value = None
        self._description = None
        self._category = None

    @property
    def key(self):
        """
        Gets the key of this Metadata.
        Key of the model Metadata. The key can either be user defined or OCI defined.
           List of OCI defined keys:
                 * useCaseType
                 * libraryName
                 * libraryVersion
                 * estimatorClass
                 * hyperParameters
                 * testartifactresults


        :return: The key of this Metadata.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Metadata.
        Key of the model Metadata. The key can either be user defined or OCI defined.
           List of OCI defined keys:
                 * useCaseType
                 * libraryName
                 * libraryVersion
                 * estimatorClass
                 * hyperParameters
                 * testartifactresults


        :param key: The key of this Metadata.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """
        Gets the value of this Metadata.
        Allowed values for useCaseType:
                     binary_classification, regression, multinomial_classification, clustering, recommender,
                     dimensionality_reduction/representation, time_series_forecasting, anomaly_detection,
                     topic_modeling, ner, sentiment_analysis, image_classification, object_localization, other

        Allowed values for libraryName:
                     scikit-learn, xgboost, tensorflow, pytorch, mxnet, keras, lightGBM, pymc3, pyOD, spacy,
                     prophet, sktime, statsmodels, cuml, oracle_automl, h2o, transformers, nltk, emcee, pystan,
                     bert, gensim, flair, word2vec, ensemble, other


        :return: The value of this Metadata.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Metadata.
        Allowed values for useCaseType:
                     binary_classification, regression, multinomial_classification, clustering, recommender,
                     dimensionality_reduction/representation, time_series_forecasting, anomaly_detection,
                     topic_modeling, ner, sentiment_analysis, image_classification, object_localization, other

        Allowed values for libraryName:
                     scikit-learn, xgboost, tensorflow, pytorch, mxnet, keras, lightGBM, pymc3, pyOD, spacy,
                     prophet, sktime, statsmodels, cuml, oracle_automl, h2o, transformers, nltk, emcee, pystan,
                     bert, gensim, flair, word2vec, ensemble, other


        :param value: The value of this Metadata.
        :type: str
        """
        self._value = value

    @property
    def description(self):
        """
        Gets the description of this Metadata.
        Description of model metadata


        :return: The description of this Metadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Metadata.
        Description of model metadata


        :param description: The description of this Metadata.
        :type: str
        """
        self._description = description

    @property
    def category(self):
        """
        Gets the category of this Metadata.
        Category of model metadata which should be null for defined metadata.For custom metadata is should be one of the following values \"Performance,Training Profile,Training and Validation Datasets,Training Environment,other\".


        :return: The category of this Metadata.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Metadata.
        Category of model metadata which should be null for defined metadata.For custom metadata is should be one of the following values \"Performance,Training Profile,Training and Validation Datasets,Training Environment,other\".


        :param category: The category of this Metadata.
        :type: str
        """
        self._category = category

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
