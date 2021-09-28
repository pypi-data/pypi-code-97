# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachTargetResponderRecipeDetails(object):
    """
    The information required to create TargetResponderRecipe
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachTargetResponderRecipeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param responder_recipe_id:
            The value to assign to the responder_recipe_id property of this AttachTargetResponderRecipeDetails.
        :type responder_recipe_id: str

        """
        self.swagger_types = {
            'responder_recipe_id': 'str'
        }

        self.attribute_map = {
            'responder_recipe_id': 'responderRecipeId'
        }

        self._responder_recipe_id = None

    @property
    def responder_recipe_id(self):
        """
        **[Required]** Gets the responder_recipe_id of this AttachTargetResponderRecipeDetails.
        ResponderRecipe Identifier


        :return: The responder_recipe_id of this AttachTargetResponderRecipeDetails.
        :rtype: str
        """
        return self._responder_recipe_id

    @responder_recipe_id.setter
    def responder_recipe_id(self, responder_recipe_id):
        """
        Sets the responder_recipe_id of this AttachTargetResponderRecipeDetails.
        ResponderRecipe Identifier


        :param responder_recipe_id: The responder_recipe_id of this AttachTargetResponderRecipeDetails.
        :type: str
        """
        self._responder_recipe_id = responder_recipe_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
