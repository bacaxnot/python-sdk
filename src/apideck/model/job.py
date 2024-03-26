"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.4.0
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
    from apideck.model.address import Address
    from apideck.model.branch import Branch
    from apideck.model.custom_field import CustomField
    from apideck.model.department import Department
    from apideck.model.job_links import JobLinks
    from apideck.model.job_salary import JobSalary
    from apideck.model.job_status import JobStatus
    from apideck.model.tags import Tags
    globals()['Address'] = Address
    globals()['Branch'] = Branch
    globals()['CustomField'] = CustomField
    globals()['Department'] = Department
    globals()['JobLinks'] = JobLinks
    globals()['JobSalary'] = JobSalary
    globals()['JobStatus'] = JobStatus
    globals()['Tags'] = Tags


class Job(ModelNormal):
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
        ('visibility',): {
            'DRAFT': "draft",
            'PUBLIC': "public",
            'INTERNAL': "internal",
        },
        ('employment_terms',): {
            'None': None,
            'FULL-TIME': "full-time",
            'PART-TIME': "part-time",
            'INTERNSHIP': "internship",
            'CONTRACTOR': "contractor",
            'EMPLOYEE': "employee",
            'FREELANCE': "freelance",
            'TEMP': "temp",
            'SEASONAL': "seasonal",
            'VOLUNTEER': "volunteer",
            'OTHER': "other",
        },
    }

    validations = {
        ('links',): {
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
            'id': (str,),  # noqa: E501
            'slug': (str, none_type,),  # noqa: E501
            'title': (str, none_type,),  # noqa: E501
            'sequence': (int,),  # noqa: E501
            'visibility': (str,),  # noqa: E501
            'status': (JobStatus,),  # noqa: E501
            'code': (str,),  # noqa: E501
            'language': (str, none_type,),  # noqa: E501
            'employment_terms': (str, none_type,),  # noqa: E501
            'experience': (str,),  # noqa: E501
            'location': (str, none_type,),  # noqa: E501
            'remote': (bool, none_type,),  # noqa: E501
            'requisition_id': (str,),  # noqa: E501
            'department': (Department,),  # noqa: E501
            'branch': (Branch,),  # noqa: E501
            'recruiters': ([str], none_type,),  # noqa: E501
            'hiring_managers': ([str],),  # noqa: E501
            'followers': ([str], none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'description_html': (str, none_type,),  # noqa: E501
            'blocks': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'closing': (str, none_type,),  # noqa: E501
            'closing_html': (str, none_type,),  # noqa: E501
            'closing_date': (date, none_type,),  # noqa: E501
            'salary': (JobSalary,),  # noqa: E501
            'url': (str, none_type,),  # noqa: E501
            'job_portal_url': (str, none_type,),  # noqa: E501
            'record_url': (str, none_type,),  # noqa: E501
            'links': ([JobLinks],),  # noqa: E501
            'confidential': (bool,),  # noqa: E501
            'available_to_employees': (bool,),  # noqa: E501
            'tags': (Tags,),  # noqa: E501
            'addresses': ([Address],),  # noqa: E501
            'custom_fields': ([CustomField],),  # noqa: E501
            'deleted': (bool, none_type,),  # noqa: E501
            'owner_id': (str, none_type,),  # noqa: E501
            'published_at': (datetime, none_type,),  # noqa: E501
            'custom_mappings': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'updated_by': (str, none_type,),  # noqa: E501
            'created_by': (str, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'slug': 'slug',  # noqa: E501
        'title': 'title',  # noqa: E501
        'sequence': 'sequence',  # noqa: E501
        'visibility': 'visibility',  # noqa: E501
        'status': 'status',  # noqa: E501
        'code': 'code',  # noqa: E501
        'language': 'language',  # noqa: E501
        'employment_terms': 'employment_terms',  # noqa: E501
        'experience': 'experience',  # noqa: E501
        'location': 'location',  # noqa: E501
        'remote': 'remote',  # noqa: E501
        'requisition_id': 'requisition_id',  # noqa: E501
        'department': 'department',  # noqa: E501
        'branch': 'branch',  # noqa: E501
        'recruiters': 'recruiters',  # noqa: E501
        'hiring_managers': 'hiring_managers',  # noqa: E501
        'followers': 'followers',  # noqa: E501
        'description': 'description',  # noqa: E501
        'description_html': 'description_html',  # noqa: E501
        'blocks': 'blocks',  # noqa: E501
        'closing': 'closing',  # noqa: E501
        'closing_html': 'closing_html',  # noqa: E501
        'closing_date': 'closing_date',  # noqa: E501
        'salary': 'salary',  # noqa: E501
        'url': 'url',  # noqa: E501
        'job_portal_url': 'job_portal_url',  # noqa: E501
        'record_url': 'record_url',  # noqa: E501
        'links': 'links',  # noqa: E501
        'confidential': 'confidential',  # noqa: E501
        'available_to_employees': 'available_to_employees',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'addresses': 'addresses',  # noqa: E501
        'custom_fields': 'custom_fields',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'owner_id': 'owner_id',  # noqa: E501
        'published_at': 'published_at',  # noqa: E501
        'custom_mappings': 'custom_mappings',  # noqa: E501
        'updated_by': 'updated_by',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'published_at',  # noqa: E501
        'custom_mappings',  # noqa: E501
        'updated_by',  # noqa: E501
        'created_by',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Job - a model defined in OpenAPI

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
            id (str): A unique identifier for an object.. [optional]  # noqa: E501
            slug (str, none_type): [optional]  # noqa: E501
            title (str, none_type): The job title of the person.. [optional]  # noqa: E501
            sequence (int): Sequence in relation to other jobs.. [optional]  # noqa: E501
            visibility (str): The visibility of the job. [optional]  # noqa: E501
            status (JobStatus): [optional]  # noqa: E501
            code (str): The code of the job.. [optional]  # noqa: E501
            language (str, none_type): language code according to ISO 639-1. For the United States - EN. [optional]  # noqa: E501
            employment_terms (str, none_type): [optional]  # noqa: E501
            experience (str): Level of experience required for the job role.. [optional]  # noqa: E501
            location (str, none_type): Specifies the location for the job posting.. [optional]  # noqa: E501
            remote (bool, none_type): Specifies whether the posting is for a remote job.. [optional]  # noqa: E501
            requisition_id (str): A job's Requisition ID (Req ID) allows your organization to identify and track a job based on alphanumeric naming conventions unique to your company's internal processes.. [optional]  # noqa: E501
            department (Department): [optional]  # noqa: E501
            branch (Branch): [optional]  # noqa: E501
            recruiters ([str], none_type): The recruiter is generally someone who is tasked to help the hiring manager find and screen qualified applicant. [optional]  # noqa: E501
            hiring_managers ([str]): [optional]  # noqa: E501
            followers ([str], none_type): [optional]  # noqa: E501
            description (str, none_type): A description of the object.. [optional]  # noqa: E501
            description_html (str, none_type): The job description in HTML format. [optional]  # noqa: E501
            blocks ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            closing (str, none_type): [optional]  # noqa: E501
            closing_html (str, none_type): The closing section of the job description in HTML format. [optional]  # noqa: E501
            closing_date (date, none_type): [optional]  # noqa: E501
            salary (JobSalary): [optional]  # noqa: E501
            url (str, none_type): URL of the job description. [optional]  # noqa: E501
            job_portal_url (str, none_type): URL of the job portal. [optional]  # noqa: E501
            record_url (str, none_type): [optional]  # noqa: E501
            links ([JobLinks]): [optional]  # noqa: E501
            confidential (bool): [optional]  # noqa: E501
            available_to_employees (bool): Specifies whether an employee of the organization can apply for the job.. [optional]  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            custom_fields ([CustomField]): [optional]  # noqa: E501
            deleted (bool, none_type): Flag to indicate if the object is deleted.. [optional]  # noqa: E501
            owner_id (str, none_type): [optional]  # noqa: E501
            published_at (datetime, none_type): [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            updated_by (str, none_type): The user who last updated the object.. [optional]  # noqa: E501
            created_by (str, none_type): The user who created the object.. [optional]  # noqa: E501
            updated_at (datetime, none_type): The date and time when the object was last updated.. [optional]  # noqa: E501
            created_at (datetime, none_type): The date and time when the object was created.. [optional]  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Job - a model defined in OpenAPI

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
            id (str): A unique identifier for an object.. [optional]  # noqa: E501
            slug (str, none_type): [optional]  # noqa: E501
            title (str, none_type): The job title of the person.. [optional]  # noqa: E501
            sequence (int): Sequence in relation to other jobs.. [optional]  # noqa: E501
            visibility (str): The visibility of the job. [optional]  # noqa: E501
            status (JobStatus): [optional]  # noqa: E501
            code (str): The code of the job.. [optional]  # noqa: E501
            language (str, none_type): language code according to ISO 639-1. For the United States - EN. [optional]  # noqa: E501
            employment_terms (str, none_type): [optional]  # noqa: E501
            experience (str): Level of experience required for the job role.. [optional]  # noqa: E501
            location (str, none_type): Specifies the location for the job posting.. [optional]  # noqa: E501
            remote (bool, none_type): Specifies whether the posting is for a remote job.. [optional]  # noqa: E501
            requisition_id (str): A job's Requisition ID (Req ID) allows your organization to identify and track a job based on alphanumeric naming conventions unique to your company's internal processes.. [optional]  # noqa: E501
            department (Department): [optional]  # noqa: E501
            branch (Branch): [optional]  # noqa: E501
            recruiters ([str], none_type): The recruiter is generally someone who is tasked to help the hiring manager find and screen qualified applicant. [optional]  # noqa: E501
            hiring_managers ([str]): [optional]  # noqa: E501
            followers ([str], none_type): [optional]  # noqa: E501
            description (str, none_type): A description of the object.. [optional]  # noqa: E501
            description_html (str, none_type): The job description in HTML format. [optional]  # noqa: E501
            blocks ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            closing (str, none_type): [optional]  # noqa: E501
            closing_html (str, none_type): The closing section of the job description in HTML format. [optional]  # noqa: E501
            closing_date (date, none_type): [optional]  # noqa: E501
            salary (JobSalary): [optional]  # noqa: E501
            url (str, none_type): URL of the job description. [optional]  # noqa: E501
            job_portal_url (str, none_type): URL of the job portal. [optional]  # noqa: E501
            record_url (str, none_type): [optional]  # noqa: E501
            links ([JobLinks]): [optional]  # noqa: E501
            confidential (bool): [optional]  # noqa: E501
            available_to_employees (bool): Specifies whether an employee of the organization can apply for the job.. [optional]  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            custom_fields ([CustomField]): [optional]  # noqa: E501
            deleted (bool, none_type): Flag to indicate if the object is deleted.. [optional]  # noqa: E501
            owner_id (str, none_type): [optional]  # noqa: E501
            published_at (datetime, none_type): [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            updated_by (str, none_type): The user who last updated the object.. [optional]  # noqa: E501
            created_by (str, none_type): The user who created the object.. [optional]  # noqa: E501
            updated_at (datetime, none_type): The date and time when the object was last updated.. [optional]  # noqa: E501
            created_at (datetime, none_type): The date and time when the object was created.. [optional]  # noqa: E501
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
