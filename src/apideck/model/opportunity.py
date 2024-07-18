"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.7.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from apideck.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from apideck.exceptions import ApiAttributeError


def lazy_import():
    from apideck.model.currency import Currency
    from apideck.model.custom_field import CustomField
    from apideck.model.pass_through_body import PassThroughBody
    from apideck.model.tags import Tags
    globals()['Currency'] = Currency
    globals()['CustomField'] = CustomField
    globals()['PassThroughBody'] = PassThroughBody
    globals()['Tags'] = Tags


class Opportunity(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('title',): {
            'min_length': 1,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'title': (str,),  # noqa: E501
            'primary_contact_id': (str, none_type,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
            'monetary_amount': (float, none_type,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'win_probability': (float, none_type,),  # noqa: E501
            'expected_revenue': (float, none_type,),  # noqa: E501
            'close_date': (date, none_type,),  # noqa: E501
            'loss_reason_id': (str, none_type,),  # noqa: E501
            'loss_reason': (str, none_type,),  # noqa: E501
            'won_reason_id': (str, none_type,),  # noqa: E501
            'won_reason': (str, none_type,),  # noqa: E501
            'pipeline_id': (str, none_type,),  # noqa: E501
            'pipeline_stage_id': (str, none_type,),  # noqa: E501
            'source_id': (str, none_type,),  # noqa: E501
            'lead_id': (str, none_type,),  # noqa: E501
            'lead_source': (str, none_type,),  # noqa: E501
            'contact_id': (str, none_type,),  # noqa: E501
            'contact_ids': ([str],),  # noqa: E501
            'company_id': (str, none_type,),  # noqa: E501
            'company_name': (str, none_type,),  # noqa: E501
            'owner_id': (str, none_type,),  # noqa: E501
            'priority': (str, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'status_id': (str, none_type,),  # noqa: E501
            'tags': (Tags,),  # noqa: E501
            'interaction_count': (float, none_type,),  # noqa: E501
            'custom_fields': ([CustomField],),  # noqa: E501
            'stage_last_changed_at': (datetime, none_type,),  # noqa: E501
            'last_activity_at': (str, none_type,),  # noqa: E501
            'deleted': (bool,),  # noqa: E501
            'date_stage_changed': (datetime, none_type,),  # noqa: E501
            'date_last_contacted': (datetime, none_type,),  # noqa: E501
            'date_lead_created': (datetime, none_type,),  # noqa: E501
            'custom_mappings': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'updated_by': (str, none_type,),  # noqa: E501
            'created_by': (str, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
            'pass_through': (PassThroughBody,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'title': 'title',  # noqa: E501
        'primary_contact_id': 'primary_contact_id',  # noqa: E501
        'id': 'id',  # noqa: E501
        'description': 'description',  # noqa: E501
        'type': 'type',  # noqa: E501
        'monetary_amount': 'monetary_amount',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'win_probability': 'win_probability',  # noqa: E501
        'expected_revenue': 'expected_revenue',  # noqa: E501
        'close_date': 'close_date',  # noqa: E501
        'loss_reason_id': 'loss_reason_id',  # noqa: E501
        'loss_reason': 'loss_reason',  # noqa: E501
        'won_reason_id': 'won_reason_id',  # noqa: E501
        'won_reason': 'won_reason',  # noqa: E501
        'pipeline_id': 'pipeline_id',  # noqa: E501
        'pipeline_stage_id': 'pipeline_stage_id',  # noqa: E501
        'source_id': 'source_id',  # noqa: E501
        'lead_id': 'lead_id',  # noqa: E501
        'lead_source': 'lead_source',  # noqa: E501
        'contact_id': 'contact_id',  # noqa: E501
        'contact_ids': 'contact_ids',  # noqa: E501
        'company_id': 'company_id',  # noqa: E501
        'company_name': 'company_name',  # noqa: E501
        'owner_id': 'owner_id',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'status': 'status',  # noqa: E501
        'status_id': 'status_id',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'interaction_count': 'interaction_count',  # noqa: E501
        'custom_fields': 'custom_fields',  # noqa: E501
        'stage_last_changed_at': 'stage_last_changed_at',  # noqa: E501
        'last_activity_at': 'last_activity_at',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'date_stage_changed': 'date_stage_changed',  # noqa: E501
        'date_last_contacted': 'date_last_contacted',  # noqa: E501
        'date_lead_created': 'date_lead_created',  # noqa: E501
        'custom_mappings': 'custom_mappings',  # noqa: E501
        'updated_by': 'updated_by',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'pass_through': 'pass_through',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'expected_revenue',  # noqa: E501
        'interaction_count',  # noqa: E501
        'last_activity_at',  # noqa: E501
        'deleted',  # noqa: E501
        'date_stage_changed',  # noqa: E501
        'date_last_contacted',  # noqa: E501
        'date_lead_created',  # noqa: E501
        'custom_mappings',  # noqa: E501
        'updated_by',  # noqa: E501
        'created_by',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, title, primary_contact_id, *args, **kwargs):  # noqa: E501
        """Opportunity - a model defined in OpenAPI

        Args:
            title (str): The title or name of the opportunity.
            primary_contact_id (str, none_type): The unique identifier of the primary contact associated with the opportunity.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): A unique identifier for the opportunity.. [optional]  # noqa: E501
            description (str, none_type): A description of the opportunity.. [optional]  # noqa: E501
            type (str, none_type): The type of the opportunity. [optional]  # noqa: E501
            monetary_amount (float, none_type): The monetary value associated with the opportunity. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            win_probability (float, none_type): The probability of winning the opportunity, expressed as a percentage.. [optional]  # noqa: E501
            expected_revenue (float, none_type): The expected revenue from the opportunity. [optional]  # noqa: E501
            close_date (date, none_type): The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet.. [optional]  # noqa: E501
            loss_reason_id (str, none_type): The unique identifier of the reason why the opportunity was lost.. [optional]  # noqa: E501
            loss_reason (str, none_type): The reason why the opportunity was lost.. [optional]  # noqa: E501
            won_reason_id (str, none_type): The unique identifier of the reason why the opportunity was won.. [optional]  # noqa: E501
            won_reason (str, none_type): The reason why the opportunity was won.. [optional]  # noqa: E501
            pipeline_id (str, none_type): The unique identifier of the pipeline associated with the opportunity. [optional]  # noqa: E501
            pipeline_stage_id (str, none_type): The unique identifier of the stage in the pipeline associated with the opportunity.. [optional]  # noqa: E501
            source_id (str, none_type): The unique identifier of the source of the opportunity.. [optional]  # noqa: E501
            lead_id (str, none_type): The unique identifier of the lead associated with the opportunity.. [optional]  # noqa: E501
            lead_source (str, none_type): The source of the lead associated with the opportunity.. [optional]  # noqa: E501
            contact_id (str, none_type): The unique identifier of the contact associated with the opportunity.. [optional]  # noqa: E501
            contact_ids ([str]): An array of unique identifiers of all contacts associated with the opportunity.. [optional]  # noqa: E501
            company_id (str, none_type): The unique identifier of the company associated with the opportunity.. [optional]  # noqa: E501
            company_name (str, none_type): The name of the company associated with the opportunity.. [optional]  # noqa: E501
            owner_id (str, none_type): The unique identifier of the user who owns the opportunity.. [optional]  # noqa: E501
            priority (str, none_type): The priority level of the opportunity.. [optional]  # noqa: E501
            status (str, none_type): The current status of the opportunity.. [optional]  # noqa: E501
            status_id (str, none_type): The unique identifier of the current status of the opportunity.. [optional]  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            interaction_count (float, none_type): The number of interactions with the opportunity.. [optional]  # noqa: E501
            custom_fields ([CustomField]): [optional]  # noqa: E501
            stage_last_changed_at (datetime, none_type): The date and time when the stage of the opportunity was last changed.. [optional]  # noqa: E501
            last_activity_at (str, none_type): The date and time of the last activity associated with the opportunity.. [optional]  # noqa: E501
            deleted (bool): Indicates whether the opportunity has been deleted.. [optional]  # noqa: E501
            date_stage_changed (datetime, none_type): The date and time when the stage of the opportunity was last changed.. [optional]  # noqa: E501
            date_last_contacted (datetime, none_type): The date and time when the opportunity was last contacted.. [optional]  # noqa: E501
            date_lead_created (datetime, none_type): The date and time when the lead associated with the opportunity was created.. [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            updated_by (str, none_type): The unique identifier of the user who last updated the opportunity.. [optional]  # noqa: E501
            created_by (str, none_type): The unique identifier of the user who created the opportunity.. [optional]  # noqa: E501
            updated_at (datetime, none_type): The date and time when the opportunity was last updated.. [optional]  # noqa: E501
            created_at (datetime, none_type): The date and time when the opportunity was created.. [optional]  # noqa: E501
            pass_through (PassThroughBody): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.title = title
        self.primary_contact_id = primary_contact_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, title, primary_contact_id, *args, **kwargs):  # noqa: E501
        """Opportunity - a model defined in OpenAPI

        Args:
            title (str): The title or name of the opportunity.
            primary_contact_id (str, none_type): The unique identifier of the primary contact associated with the opportunity.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): A unique identifier for the opportunity.. [optional]  # noqa: E501
            description (str, none_type): A description of the opportunity.. [optional]  # noqa: E501
            type (str, none_type): The type of the opportunity. [optional]  # noqa: E501
            monetary_amount (float, none_type): The monetary value associated with the opportunity. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            win_probability (float, none_type): The probability of winning the opportunity, expressed as a percentage.. [optional]  # noqa: E501
            expected_revenue (float, none_type): The expected revenue from the opportunity. [optional]  # noqa: E501
            close_date (date, none_type): The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet.. [optional]  # noqa: E501
            loss_reason_id (str, none_type): The unique identifier of the reason why the opportunity was lost.. [optional]  # noqa: E501
            loss_reason (str, none_type): The reason why the opportunity was lost.. [optional]  # noqa: E501
            won_reason_id (str, none_type): The unique identifier of the reason why the opportunity was won.. [optional]  # noqa: E501
            won_reason (str, none_type): The reason why the opportunity was won.. [optional]  # noqa: E501
            pipeline_id (str, none_type): The unique identifier of the pipeline associated with the opportunity. [optional]  # noqa: E501
            pipeline_stage_id (str, none_type): The unique identifier of the stage in the pipeline associated with the opportunity.. [optional]  # noqa: E501
            source_id (str, none_type): The unique identifier of the source of the opportunity.. [optional]  # noqa: E501
            lead_id (str, none_type): The unique identifier of the lead associated with the opportunity.. [optional]  # noqa: E501
            lead_source (str, none_type): The source of the lead associated with the opportunity.. [optional]  # noqa: E501
            contact_id (str, none_type): The unique identifier of the contact associated with the opportunity.. [optional]  # noqa: E501
            contact_ids ([str]): An array of unique identifiers of all contacts associated with the opportunity.. [optional]  # noqa: E501
            company_id (str, none_type): The unique identifier of the company associated with the opportunity.. [optional]  # noqa: E501
            company_name (str, none_type): The name of the company associated with the opportunity.. [optional]  # noqa: E501
            owner_id (str, none_type): The unique identifier of the user who owns the opportunity.. [optional]  # noqa: E501
            priority (str, none_type): The priority level of the opportunity.. [optional]  # noqa: E501
            status (str, none_type): The current status of the opportunity.. [optional]  # noqa: E501
            status_id (str, none_type): The unique identifier of the current status of the opportunity.. [optional]  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            interaction_count (float, none_type): The number of interactions with the opportunity.. [optional]  # noqa: E501
            custom_fields ([CustomField]): [optional]  # noqa: E501
            stage_last_changed_at (datetime, none_type): The date and time when the stage of the opportunity was last changed.. [optional]  # noqa: E501
            last_activity_at (str, none_type): The date and time of the last activity associated with the opportunity.. [optional]  # noqa: E501
            deleted (bool): Indicates whether the opportunity has been deleted.. [optional]  # noqa: E501
            date_stage_changed (datetime, none_type): The date and time when the stage of the opportunity was last changed.. [optional]  # noqa: E501
            date_last_contacted (datetime, none_type): The date and time when the opportunity was last contacted.. [optional]  # noqa: E501
            date_lead_created (datetime, none_type): The date and time when the lead associated with the opportunity was created.. [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            updated_by (str, none_type): The unique identifier of the user who last updated the opportunity.. [optional]  # noqa: E501
            created_by (str, none_type): The unique identifier of the user who created the opportunity.. [optional]  # noqa: E501
            updated_at (datetime, none_type): The date and time when the opportunity was last updated.. [optional]  # noqa: E501
            created_at (datetime, none_type): The date and time when the opportunity was created.. [optional]  # noqa: E501
            pass_through (PassThroughBody): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.title = title
        self.primary_contact_id = primary_contact_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
