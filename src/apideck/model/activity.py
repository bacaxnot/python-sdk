"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 9.8.1
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
    from apideck.model.activity_attendee import ActivityAttendee
    from apideck.model.address import Address
    from apideck.model.custom_field import CustomField
    globals()['ActivityAttendee'] = ActivityAttendee
    globals()['Address'] = Address
    globals()['CustomField'] = CustomField


class Activity(ModelNormal):
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
        ('type',): {
            'None': None,
            'CALL': "call",
            'MEETING': "meeting",
            'EMAIL': "email",
            'NOTE': "note",
            'TASK': "task",
            'DEADLINE': "deadline",
            'SEND-LETTER': "send-letter",
            'SEND-QUOTE': "send-quote",
            'OTHER': "other",
        },
        ('show_as',): {
            'None': None,
            'FREE': "free",
            'BUSY': "busy",
        },
    }

    validations = {
        ('duration_seconds',): {
            'inclusive_minimum': 0,
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
            'type': (str, none_type,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'downstream_id': (str, none_type,),  # noqa: E501
            'activity_datetime': (str, none_type,),  # noqa: E501
            'duration_seconds': (int, none_type,),  # noqa: E501
            'user_id': (str, none_type,),  # noqa: E501
            'account_id': (str, none_type,),  # noqa: E501
            'contact_id': (str, none_type,),  # noqa: E501
            'company_id': (str, none_type,),  # noqa: E501
            'opportunity_id': (str, none_type,),  # noqa: E501
            'lead_id': (str, none_type,),  # noqa: E501
            'owner_id': (str, none_type,),  # noqa: E501
            'campaign_id': (str, none_type,),  # noqa: E501
            'case_id': (str, none_type,),  # noqa: E501
            'asset_id': (str, none_type,),  # noqa: E501
            'contract_id': (str, none_type,),  # noqa: E501
            'product_id': (str, none_type,),  # noqa: E501
            'solution_id': (str, none_type,),  # noqa: E501
            'custom_object_id': (str, none_type,),  # noqa: E501
            'title': (str, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'note': (str, none_type,),  # noqa: E501
            'location': (str, none_type,),  # noqa: E501
            'location_address': (Address,),  # noqa: E501
            'all_day_event': (bool, none_type,),  # noqa: E501
            'private': (bool, none_type,),  # noqa: E501
            'group_event': (bool, none_type,),  # noqa: E501
            'event_sub_type': (str, none_type,),  # noqa: E501
            'group_event_type': (str, none_type,),  # noqa: E501
            'child': (bool, none_type,),  # noqa: E501
            'archived': (bool, none_type,),  # noqa: E501
            'deleted': (bool, none_type,),  # noqa: E501
            'show_as': (str, none_type,),  # noqa: E501
            'done': (bool, none_type,),  # noqa: E501
            'start_datetime': (str, none_type,),  # noqa: E501
            'end_datetime': (str, none_type,),  # noqa: E501
            'duration_minutes': (int, none_type,),  # noqa: E501
            'activity_date': (str, none_type,),  # noqa: E501
            'end_date': (str, none_type,),  # noqa: E501
            'recurrent': (bool,),  # noqa: E501
            'reminder_datetime': (str, none_type,),  # noqa: E501
            'reminder_set': (bool, none_type,),  # noqa: E501
            'video_conference_url': (str, none_type,),  # noqa: E501
            'video_conference_id': (str, none_type,),  # noqa: E501
            'custom_fields': ([CustomField],),  # noqa: E501
            'attendees': ([ActivityAttendee],),  # noqa: E501
            'updated_by': (str, none_type,),  # noqa: E501
            'created_by': (str, none_type,),  # noqa: E501
            'updated_at': (str, none_type,),  # noqa: E501
            'created_at': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'type': 'type',  # noqa: E501
        'id': 'id',  # noqa: E501
        'downstream_id': 'downstream_id',  # noqa: E501
        'activity_datetime': 'activity_datetime',  # noqa: E501
        'duration_seconds': 'duration_seconds',  # noqa: E501
        'user_id': 'user_id',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'contact_id': 'contact_id',  # noqa: E501
        'company_id': 'company_id',  # noqa: E501
        'opportunity_id': 'opportunity_id',  # noqa: E501
        'lead_id': 'lead_id',  # noqa: E501
        'owner_id': 'owner_id',  # noqa: E501
        'campaign_id': 'campaign_id',  # noqa: E501
        'case_id': 'case_id',  # noqa: E501
        'asset_id': 'asset_id',  # noqa: E501
        'contract_id': 'contract_id',  # noqa: E501
        'product_id': 'product_id',  # noqa: E501
        'solution_id': 'solution_id',  # noqa: E501
        'custom_object_id': 'custom_object_id',  # noqa: E501
        'title': 'title',  # noqa: E501
        'description': 'description',  # noqa: E501
        'note': 'note',  # noqa: E501
        'location': 'location',  # noqa: E501
        'location_address': 'location_address',  # noqa: E501
        'all_day_event': 'all_day_event',  # noqa: E501
        'private': 'private',  # noqa: E501
        'group_event': 'group_event',  # noqa: E501
        'event_sub_type': 'event_sub_type',  # noqa: E501
        'group_event_type': 'group_event_type',  # noqa: E501
        'child': 'child',  # noqa: E501
        'archived': 'archived',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'show_as': 'show_as',  # noqa: E501
        'done': 'done',  # noqa: E501
        'start_datetime': 'start_datetime',  # noqa: E501
        'end_datetime': 'end_datetime',  # noqa: E501
        'duration_minutes': 'duration_minutes',  # noqa: E501
        'activity_date': 'activity_date',  # noqa: E501
        'end_date': 'end_date',  # noqa: E501
        'recurrent': 'recurrent',  # noqa: E501
        'reminder_datetime': 'reminder_datetime',  # noqa: E501
        'reminder_set': 'reminder_set',  # noqa: E501
        'video_conference_url': 'video_conference_url',  # noqa: E501
        'video_conference_id': 'video_conference_id',  # noqa: E501
        'custom_fields': 'custom_fields',  # noqa: E501
        'attendees': 'attendees',  # noqa: E501
        'updated_by': 'updated_by',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'downstream_id',  # noqa: E501
        'duration_minutes',  # noqa: E501
        'updated_by',  # noqa: E501
        'created_by',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, type, *args, **kwargs):  # noqa: E501
        """Activity - a model defined in OpenAPI

        Args:
            type (str, none_type): The type of the activity

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
            id (str): The unique identifier of the activity. [optional]  # noqa: E501
            downstream_id (str, none_type): The third-party API ID of original entity. [optional]  # noqa: E501
            activity_datetime (str, none_type): The date and time of the activity. [optional]  # noqa: E501
            duration_seconds (int, none_type): The duration of the activity in seconds. [optional]  # noqa: E501
            user_id (str, none_type): The user related to the activity. [optional]  # noqa: E501
            account_id (str, none_type): The account related to the activity. [optional]  # noqa: E501
            contact_id (str, none_type): The contact related to the activity. [optional]  # noqa: E501
            company_id (str, none_type): The company related to the activity. [optional]  # noqa: E501
            opportunity_id (str, none_type): The opportunity related to the activity. [optional]  # noqa: E501
            lead_id (str, none_type): The lead related to the activity. [optional]  # noqa: E501
            owner_id (str, none_type): The owner of the activity. [optional]  # noqa: E501
            campaign_id (str, none_type): The campaign related to the activity. [optional]  # noqa: E501
            case_id (str, none_type): The case related to the activity. [optional]  # noqa: E501
            asset_id (str, none_type): The asset related to the activity. [optional]  # noqa: E501
            contract_id (str, none_type): The contract related to the activity. [optional]  # noqa: E501
            product_id (str, none_type): The product related to the activity. [optional]  # noqa: E501
            solution_id (str, none_type): The solution related to the activity. [optional]  # noqa: E501
            custom_object_id (str, none_type): The custom object related to the activity. [optional]  # noqa: E501
            title (str, none_type): The title of the activity. [optional]  # noqa: E501
            description (str, none_type): A description of the activity. [optional]  # noqa: E501
            note (str, none_type): An internal note about the activity. [optional]  # noqa: E501
            location (str, none_type): The location of the activity. [optional]  # noqa: E501
            location_address (Address): [optional]  # noqa: E501
            all_day_event (bool, none_type): Whether the Activity is an all day event or not. [optional]  # noqa: E501
            private (bool, none_type): Whether the Activity is private or not. [optional]  # noqa: E501
            group_event (bool, none_type): Whether the Activity is a group event or not. [optional]  # noqa: E501
            event_sub_type (str, none_type): The sub type of the group event. [optional]  # noqa: E501
            group_event_type (str, none_type): The type of the group event. [optional]  # noqa: E501
            child (bool, none_type): Whether the activity is a child of another activity or not. [optional]  # noqa: E501
            archived (bool, none_type): Whether the activity is archived or not. [optional]  # noqa: E501
            deleted (bool, none_type): Whether the activity is deleted or not. [optional]  # noqa: E501
            show_as (str, none_type): [optional]  # noqa: E501
            done (bool, none_type): Whether the Activity is done or not. [optional]  # noqa: E501
            start_datetime (str, none_type): The start date and time of the activity. [optional]  # noqa: E501
            end_datetime (str, none_type): The end date and time of the activity. [optional]  # noqa: E501
            duration_minutes (int, none_type): The duration of the activity in minutes. [optional]  # noqa: E501
            activity_date (str, none_type): The date of the activity. [optional]  # noqa: E501
            end_date (str, none_type): The end date of the activity. [optional]  # noqa: E501
            recurrent (bool): Whether the activity is recurrent or not. [optional]  # noqa: E501
            reminder_datetime (str, none_type): The date and time of the reminder. [optional]  # noqa: E501
            reminder_set (bool, none_type): Whether the reminder is set or not. [optional]  # noqa: E501
            video_conference_url (str, none_type): The URL of the video conference. [optional]  # noqa: E501
            video_conference_id (str, none_type): The ID of the video conference. [optional]  # noqa: E501
            custom_fields ([CustomField]): Custom fields of the activity. [optional]  # noqa: E501
            attendees ([ActivityAttendee]): [optional]  # noqa: E501
            updated_by (str, none_type): The user who last updated the activity. [optional]  # noqa: E501
            created_by (str, none_type): The user who created the activity. [optional]  # noqa: E501
            updated_at (str, none_type): The date and time when the activity was last updated. [optional]  # noqa: E501
            created_at (str, none_type): The date and time when the activity was created. [optional]  # noqa: E501
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

        self.type = type
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
    def __init__(self, type, *args, **kwargs):  # noqa: E501
        """Activity - a model defined in OpenAPI

        Args:
            type (str, none_type): The type of the activity

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
            id (str): The unique identifier of the activity. [optional]  # noqa: E501
            downstream_id (str, none_type): The third-party API ID of original entity. [optional]  # noqa: E501
            activity_datetime (str, none_type): The date and time of the activity. [optional]  # noqa: E501
            duration_seconds (int, none_type): The duration of the activity in seconds. [optional]  # noqa: E501
            user_id (str, none_type): The user related to the activity. [optional]  # noqa: E501
            account_id (str, none_type): The account related to the activity. [optional]  # noqa: E501
            contact_id (str, none_type): The contact related to the activity. [optional]  # noqa: E501
            company_id (str, none_type): The company related to the activity. [optional]  # noqa: E501
            opportunity_id (str, none_type): The opportunity related to the activity. [optional]  # noqa: E501
            lead_id (str, none_type): The lead related to the activity. [optional]  # noqa: E501
            owner_id (str, none_type): The owner of the activity. [optional]  # noqa: E501
            campaign_id (str, none_type): The campaign related to the activity. [optional]  # noqa: E501
            case_id (str, none_type): The case related to the activity. [optional]  # noqa: E501
            asset_id (str, none_type): The asset related to the activity. [optional]  # noqa: E501
            contract_id (str, none_type): The contract related to the activity. [optional]  # noqa: E501
            product_id (str, none_type): The product related to the activity. [optional]  # noqa: E501
            solution_id (str, none_type): The solution related to the activity. [optional]  # noqa: E501
            custom_object_id (str, none_type): The custom object related to the activity. [optional]  # noqa: E501
            title (str, none_type): The title of the activity. [optional]  # noqa: E501
            description (str, none_type): A description of the activity. [optional]  # noqa: E501
            note (str, none_type): An internal note about the activity. [optional]  # noqa: E501
            location (str, none_type): The location of the activity. [optional]  # noqa: E501
            location_address (Address): [optional]  # noqa: E501
            all_day_event (bool, none_type): Whether the Activity is an all day event or not. [optional]  # noqa: E501
            private (bool, none_type): Whether the Activity is private or not. [optional]  # noqa: E501
            group_event (bool, none_type): Whether the Activity is a group event or not. [optional]  # noqa: E501
            event_sub_type (str, none_type): The sub type of the group event. [optional]  # noqa: E501
            group_event_type (str, none_type): The type of the group event. [optional]  # noqa: E501
            child (bool, none_type): Whether the activity is a child of another activity or not. [optional]  # noqa: E501
            archived (bool, none_type): Whether the activity is archived or not. [optional]  # noqa: E501
            deleted (bool, none_type): Whether the activity is deleted or not. [optional]  # noqa: E501
            show_as (str, none_type): [optional]  # noqa: E501
            done (bool, none_type): Whether the Activity is done or not. [optional]  # noqa: E501
            start_datetime (str, none_type): The start date and time of the activity. [optional]  # noqa: E501
            end_datetime (str, none_type): The end date and time of the activity. [optional]  # noqa: E501
            duration_minutes (int, none_type): The duration of the activity in minutes. [optional]  # noqa: E501
            activity_date (str, none_type): The date of the activity. [optional]  # noqa: E501
            end_date (str, none_type): The end date of the activity. [optional]  # noqa: E501
            recurrent (bool): Whether the activity is recurrent or not. [optional]  # noqa: E501
            reminder_datetime (str, none_type): The date and time of the reminder. [optional]  # noqa: E501
            reminder_set (bool, none_type): Whether the reminder is set or not. [optional]  # noqa: E501
            video_conference_url (str, none_type): The URL of the video conference. [optional]  # noqa: E501
            video_conference_id (str, none_type): The ID of the video conference. [optional]  # noqa: E501
            custom_fields ([CustomField]): Custom fields of the activity. [optional]  # noqa: E501
            attendees ([ActivityAttendee]): [optional]  # noqa: E501
            updated_by (str, none_type): The user who last updated the activity. [optional]  # noqa: E501
            created_by (str, none_type): The user who created the activity. [optional]  # noqa: E501
            updated_at (str, none_type): The date and time when the activity was last updated. [optional]  # noqa: E501
            created_at (str, none_type): The date and time when the activity was created. [optional]  # noqa: E501
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

        self.type = type
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
