"""
    Apideck

    The Apideck OpenAPI Spec: SDK Optimized  # noqa: E501

    The version of the OpenAPI document: 10.1.2
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
    from apideck.model.bank_account import BankAccount
    from apideck.model.country import Country
    from apideck.model.custom_field import CustomField
    from apideck.model.email import Email
    from apideck.model.employee_compensation import EmployeeCompensation
    from apideck.model.employee_employment_role import EmployeeEmploymentRole
    from apideck.model.employee_job import EmployeeJob
    from apideck.model.employee_manager import EmployeeManager
    from apideck.model.employment_status import EmploymentStatus
    from apideck.model.gender import Gender
    from apideck.model.person import Person
    from apideck.model.phone_number import PhoneNumber
    from apideck.model.probation_period import ProbationPeriod
    from apideck.model.social_link import SocialLink
    from apideck.model.tags import Tags
    from apideck.model.team import Team
    globals()['Address'] = Address
    globals()['BankAccount'] = BankAccount
    globals()['Country'] = Country
    globals()['CustomField'] = CustomField
    globals()['Email'] = Email
    globals()['EmployeeCompensation'] = EmployeeCompensation
    globals()['EmployeeEmploymentRole'] = EmployeeEmploymentRole
    globals()['EmployeeJob'] = EmployeeJob
    globals()['EmployeeManager'] = EmployeeManager
    globals()['EmploymentStatus'] = EmploymentStatus
    globals()['Gender'] = Gender
    globals()['Person'] = Person
    globals()['PhoneNumber'] = PhoneNumber
    globals()['ProbationPeriod'] = ProbationPeriod
    globals()['SocialLink'] = SocialLink
    globals()['Tags'] = Tags
    globals()['Team'] = Team


class Employee(ModelNormal):
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
        ('leaving_reason',): {
            'None': None,
            'DISMISSED': "dismissed",
            'RESIGNED': "resigned",
            'REDUNDANCY': "redundancy",
            'OTHER': "other",
        },
    }

    validations = {
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
            'first_name': (str, none_type,),  # noqa: E501
            'last_name': (str, none_type,),  # noqa: E501
            'middle_name': (str, none_type,),  # noqa: E501
            'display_name': (str, none_type,),  # noqa: E501
            'preferred_name': (str, none_type,),  # noqa: E501
            'initials': (str, none_type,),  # noqa: E501
            'salutation': (str, none_type,),  # noqa: E501
            'title': (str, none_type,),  # noqa: E501
            'marital_status': (str, none_type,),  # noqa: E501
            'partner': (Person,),  # noqa: E501
            'division': (str, none_type,),  # noqa: E501
            'division_id': (str, none_type,),  # noqa: E501
            'department': (str, none_type,),  # noqa: E501
            'department_id': (str, none_type,),  # noqa: E501
            'department_name': (str, none_type,),  # noqa: E501
            'team': (Team,),  # noqa: E501
            'company_id': (str, none_type,),  # noqa: E501
            'company_name': (str, none_type,),  # noqa: E501
            'employment_start_date': (str, none_type,),  # noqa: E501
            'employment_end_date': (str, none_type,),  # noqa: E501
            'leaving_reason': (str, none_type,),  # noqa: E501
            'employee_number': (str, none_type,),  # noqa: E501
            'employment_status': (EmploymentStatus,),  # noqa: E501
            'employment_role': (EmployeeEmploymentRole,),  # noqa: E501
            'ethnicity': (str, none_type,),  # noqa: E501
            'manager': (EmployeeManager,),  # noqa: E501
            'direct_reports': ([str], none_type,),  # noqa: E501
            'social_security_number': (str, none_type,),  # noqa: E501
            'birthday': (date, none_type,),  # noqa: E501
            'deceased_on': (date, none_type,),  # noqa: E501
            'country_of_birth': (Country,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'gender': (Gender,),  # noqa: E501
            'pronouns': (str, none_type,),  # noqa: E501
            'preferred_language': (str, none_type,),  # noqa: E501
            'languages': ([str, none_type],),  # noqa: E501
            'nationalities': ([str, none_type],),  # noqa: E501
            'photo_url': (str, none_type,),  # noqa: E501
            'timezone': (str, none_type,),  # noqa: E501
            'source': (str, none_type,),  # noqa: E501
            'source_id': (str, none_type,),  # noqa: E501
            'record_url': (str, none_type,),  # noqa: E501
            'jobs': ([EmployeeJob], none_type,),  # noqa: E501
            'compensations': ([EmployeeCompensation], none_type,),  # noqa: E501
            'works_remote': (bool, none_type,),  # noqa: E501
            'addresses': ([Address],),  # noqa: E501
            'phone_numbers': ([PhoneNumber],),  # noqa: E501
            'emails': ([Email],),  # noqa: E501
            'custom_fields': ([CustomField],),  # noqa: E501
            'social_links': ([SocialLink],),  # noqa: E501
            'bank_accounts': ([BankAccount],),  # noqa: E501
            'tax_code': (str, none_type,),  # noqa: E501
            'tax_id': (str, none_type,),  # noqa: E501
            'dietary_preference': (str, none_type,),  # noqa: E501
            'food_allergies': ([str], none_type,),  # noqa: E501
            'probation_period': (ProbationPeriod,),  # noqa: E501
            'tags': (Tags,),  # noqa: E501
            'custom_mappings': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'row_version': (str, none_type,),  # noqa: E501
            'deleted': (bool, none_type,),  # noqa: E501
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
        'first_name': 'first_name',  # noqa: E501
        'last_name': 'last_name',  # noqa: E501
        'middle_name': 'middle_name',  # noqa: E501
        'display_name': 'display_name',  # noqa: E501
        'preferred_name': 'preferred_name',  # noqa: E501
        'initials': 'initials',  # noqa: E501
        'salutation': 'salutation',  # noqa: E501
        'title': 'title',  # noqa: E501
        'marital_status': 'marital_status',  # noqa: E501
        'partner': 'partner',  # noqa: E501
        'division': 'division',  # noqa: E501
        'division_id': 'division_id',  # noqa: E501
        'department': 'department',  # noqa: E501
        'department_id': 'department_id',  # noqa: E501
        'department_name': 'department_name',  # noqa: E501
        'team': 'team',  # noqa: E501
        'company_id': 'company_id',  # noqa: E501
        'company_name': 'company_name',  # noqa: E501
        'employment_start_date': 'employment_start_date',  # noqa: E501
        'employment_end_date': 'employment_end_date',  # noqa: E501
        'leaving_reason': 'leaving_reason',  # noqa: E501
        'employee_number': 'employee_number',  # noqa: E501
        'employment_status': 'employment_status',  # noqa: E501
        'employment_role': 'employment_role',  # noqa: E501
        'ethnicity': 'ethnicity',  # noqa: E501
        'manager': 'manager',  # noqa: E501
        'direct_reports': 'direct_reports',  # noqa: E501
        'social_security_number': 'social_security_number',  # noqa: E501
        'birthday': 'birthday',  # noqa: E501
        'deceased_on': 'deceased_on',  # noqa: E501
        'country_of_birth': 'country_of_birth',  # noqa: E501
        'description': 'description',  # noqa: E501
        'gender': 'gender',  # noqa: E501
        'pronouns': 'pronouns',  # noqa: E501
        'preferred_language': 'preferred_language',  # noqa: E501
        'languages': 'languages',  # noqa: E501
        'nationalities': 'nationalities',  # noqa: E501
        'photo_url': 'photo_url',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
        'source': 'source',  # noqa: E501
        'source_id': 'source_id',  # noqa: E501
        'record_url': 'record_url',  # noqa: E501
        'jobs': 'jobs',  # noqa: E501
        'compensations': 'compensations',  # noqa: E501
        'works_remote': 'works_remote',  # noqa: E501
        'addresses': 'addresses',  # noqa: E501
        'phone_numbers': 'phone_numbers',  # noqa: E501
        'emails': 'emails',  # noqa: E501
        'custom_fields': 'custom_fields',  # noqa: E501
        'social_links': 'social_links',  # noqa: E501
        'bank_accounts': 'bank_accounts',  # noqa: E501
        'tax_code': 'tax_code',  # noqa: E501
        'tax_id': 'tax_id',  # noqa: E501
        'dietary_preference': 'dietary_preference',  # noqa: E501
        'food_allergies': 'food_allergies',  # noqa: E501
        'probation_period': 'probation_period',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'custom_mappings': 'custom_mappings',  # noqa: E501
        'row_version': 'row_version',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'updated_by': 'updated_by',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'custom_mappings',  # noqa: E501
        'updated_by',  # noqa: E501
        'created_by',  # noqa: E501
        'updated_at',  # noqa: E501
        'created_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, *args, **kwargs):  # noqa: E501
        """Employee - a model defined in OpenAPI

        Args:
            id (str): A unique identifier for an object.

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
            first_name (str, none_type): The first name of the person.. [optional]  # noqa: E501
            last_name (str, none_type): The last name of the person.. [optional]  # noqa: E501
            middle_name (str, none_type): Middle name of the person.. [optional]  # noqa: E501
            display_name (str, none_type): The name used to display the employee, often a combination of their first and last names.. [optional]  # noqa: E501
            preferred_name (str, none_type): The name the employee prefers to be addressed by, which may be different from their legal name.. [optional]  # noqa: E501
            initials (str, none_type): The initials of the person, usually derived from their first, middle, and last names.. [optional]  # noqa: E501
            salutation (str, none_type): A formal salutation for the person. For example, 'Mr', 'Mrs'. [optional]  # noqa: E501
            title (str, none_type): The job title of the person.. [optional]  # noqa: E501
            marital_status (str, none_type): The marital status of the employee.. [optional]  # noqa: E501
            partner (Person): [optional]  # noqa: E501
            division (str, none_type): The division the person is currently in. Usually a collection of departments or teams or regions.. [optional]  # noqa: E501
            division_id (str, none_type): Unique identifier of the division this employee belongs to.. [optional]  # noqa: E501
            department (str, none_type): The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.. [optional]  # noqa: E501
            department_id (str, none_type): Unique identifier of the department ID this employee belongs to.. [optional]  # noqa: E501
            department_name (str, none_type): Name of the department this employee belongs to.. [optional]  # noqa: E501
            team (Team): [optional]  # noqa: E501
            company_id (str, none_type): The unique identifier of the company.. [optional]  # noqa: E501
            company_name (str, none_type): The name of the company.. [optional]  # noqa: E501
            employment_start_date (str, none_type): A Start Date is the date that the employee started working at the company. [optional]  # noqa: E501
            employment_end_date (str, none_type): An End Date is the date that the employee ended working at the company. [optional]  # noqa: E501
            leaving_reason (str, none_type): The reason because the employment ended.. [optional]  # noqa: E501
            employee_number (str, none_type): An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company.. [optional]  # noqa: E501
            employment_status (EmploymentStatus): [optional]  # noqa: E501
            employment_role (EmployeeEmploymentRole): [optional]  # noqa: E501
            ethnicity (str, none_type): The ethnicity of the employee. [optional]  # noqa: E501
            manager (EmployeeManager): [optional]  # noqa: E501
            direct_reports ([str], none_type): Direct reports is an array of ids that reflect the individuals in an organizational hierarchy who are directly supervised by this specific employee.. [optional]  # noqa: E501
            social_security_number (str, none_type): A unique identifier assigned by the government. This field is considered sensitive information and may be subject to special security and privacy restrictions.. [optional]  # noqa: E501
            birthday (date, none_type): The date of birth of the person.. [optional]  # noqa: E501
            deceased_on (date, none_type): The date the person deceased.. [optional]  # noqa: E501
            country_of_birth (Country): [optional]  # noqa: E501
            description (str, none_type): A description of the object.. [optional]  # noqa: E501
            gender (Gender): [optional]  # noqa: E501
            pronouns (str, none_type): The preferred pronouns of the person.. [optional]  # noqa: E501
            preferred_language (str, none_type): language code according to ISO 639-1. For the United States - EN. [optional]  # noqa: E501
            languages ([str, none_type]): [optional]  # noqa: E501
            nationalities ([str, none_type]): [optional]  # noqa: E501
            photo_url (str, none_type): The URL of the photo of a person.. [optional]  # noqa: E501
            timezone (str, none_type): The time zone related to the resource. The value is a string containing a standard time zone identifier, e.g. Europe/London.. [optional]  # noqa: E501
            source (str, none_type): When the employee is imported as a new hire, this field indicates what system (e.g. the name of the ATS) this employee was imported from.. [optional]  # noqa: E501
            source_id (str, none_type): Unique identifier of the employee in the system this employee was imported from (e.g. the ID in the ATS).. [optional]  # noqa: E501
            record_url (str, none_type): [optional]  # noqa: E501
            jobs ([EmployeeJob], none_type): [optional]  # noqa: E501
            compensations ([EmployeeCompensation], none_type): [optional]  # noqa: E501
            works_remote (bool, none_type): Indicates if the employee works from a remote location.. [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumber]): [optional]  # noqa: E501
            emails ([Email]): [optional]  # noqa: E501
            custom_fields ([CustomField]): [optional]  # noqa: E501
            social_links ([SocialLink]): [optional]  # noqa: E501
            bank_accounts ([BankAccount]): [optional]  # noqa: E501
            tax_code (str, none_type): [optional]  # noqa: E501
            tax_id (str, none_type): [optional]  # noqa: E501
            dietary_preference (str, none_type): Indicate the employee's dietary preference.. [optional]  # noqa: E501
            food_allergies ([str], none_type): Indicate the employee's food allergies.. [optional]  # noqa: E501
            probation_period (ProbationPeriod): [optional]  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            row_version (str, none_type): A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.. [optional]  # noqa: E501
            deleted (bool, none_type): Flag to indicate if the object is deleted.. [optional]  # noqa: E501
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

        self.id = id
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
        """Employee - a model defined in OpenAPI

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
            first_name (str, none_type): The first name of the person.. [optional]  # noqa: E501
            last_name (str, none_type): The last name of the person.. [optional]  # noqa: E501
            middle_name (str, none_type): Middle name of the person.. [optional]  # noqa: E501
            display_name (str, none_type): The name used to display the employee, often a combination of their first and last names.. [optional]  # noqa: E501
            preferred_name (str, none_type): The name the employee prefers to be addressed by, which may be different from their legal name.. [optional]  # noqa: E501
            initials (str, none_type): The initials of the person, usually derived from their first, middle, and last names.. [optional]  # noqa: E501
            salutation (str, none_type): A formal salutation for the person. For example, 'Mr', 'Mrs'. [optional]  # noqa: E501
            title (str, none_type): The job title of the person.. [optional]  # noqa: E501
            marital_status (str, none_type): The marital status of the employee.. [optional]  # noqa: E501
            partner (Person): [optional]  # noqa: E501
            division (str, none_type): The division the person is currently in. Usually a collection of departments or teams or regions.. [optional]  # noqa: E501
            division_id (str, none_type): Unique identifier of the division this employee belongs to.. [optional]  # noqa: E501
            department (str, none_type): The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.. [optional]  # noqa: E501
            department_id (str, none_type): Unique identifier of the department ID this employee belongs to.. [optional]  # noqa: E501
            department_name (str, none_type): Name of the department this employee belongs to.. [optional]  # noqa: E501
            team (Team): [optional]  # noqa: E501
            company_id (str, none_type): The unique identifier of the company.. [optional]  # noqa: E501
            company_name (str, none_type): The name of the company.. [optional]  # noqa: E501
            employment_start_date (str, none_type): A Start Date is the date that the employee started working at the company. [optional]  # noqa: E501
            employment_end_date (str, none_type): An End Date is the date that the employee ended working at the company. [optional]  # noqa: E501
            leaving_reason (str, none_type): The reason because the employment ended.. [optional]  # noqa: E501
            employee_number (str, none_type): An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company.. [optional]  # noqa: E501
            employment_status (EmploymentStatus): [optional]  # noqa: E501
            employment_role (EmployeeEmploymentRole): [optional]  # noqa: E501
            ethnicity (str, none_type): The ethnicity of the employee. [optional]  # noqa: E501
            manager (EmployeeManager): [optional]  # noqa: E501
            direct_reports ([str], none_type): Direct reports is an array of ids that reflect the individuals in an organizational hierarchy who are directly supervised by this specific employee.. [optional]  # noqa: E501
            social_security_number (str, none_type): A unique identifier assigned by the government. This field is considered sensitive information and may be subject to special security and privacy restrictions.. [optional]  # noqa: E501
            birthday (date, none_type): The date of birth of the person.. [optional]  # noqa: E501
            deceased_on (date, none_type): The date the person deceased.. [optional]  # noqa: E501
            country_of_birth (Country): [optional]  # noqa: E501
            description (str, none_type): A description of the object.. [optional]  # noqa: E501
            gender (Gender): [optional]  # noqa: E501
            pronouns (str, none_type): The preferred pronouns of the person.. [optional]  # noqa: E501
            preferred_language (str, none_type): language code according to ISO 639-1. For the United States - EN. [optional]  # noqa: E501
            languages ([str, none_type]): [optional]  # noqa: E501
            nationalities ([str, none_type]): [optional]  # noqa: E501
            photo_url (str, none_type): The URL of the photo of a person.. [optional]  # noqa: E501
            timezone (str, none_type): The time zone related to the resource. The value is a string containing a standard time zone identifier, e.g. Europe/London.. [optional]  # noqa: E501
            source (str, none_type): When the employee is imported as a new hire, this field indicates what system (e.g. the name of the ATS) this employee was imported from.. [optional]  # noqa: E501
            source_id (str, none_type): Unique identifier of the employee in the system this employee was imported from (e.g. the ID in the ATS).. [optional]  # noqa: E501
            record_url (str, none_type): [optional]  # noqa: E501
            jobs ([EmployeeJob], none_type): [optional]  # noqa: E501
            compensations ([EmployeeCompensation], none_type): [optional]  # noqa: E501
            works_remote (bool, none_type): Indicates if the employee works from a remote location.. [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumber]): [optional]  # noqa: E501
            emails ([Email]): [optional]  # noqa: E501
            custom_fields ([CustomField]): [optional]  # noqa: E501
            social_links ([SocialLink]): [optional]  # noqa: E501
            bank_accounts ([BankAccount]): [optional]  # noqa: E501
            tax_code (str, none_type): [optional]  # noqa: E501
            tax_id (str, none_type): [optional]  # noqa: E501
            dietary_preference (str, none_type): Indicate the employee's dietary preference.. [optional]  # noqa: E501
            food_allergies ([str], none_type): Indicate the employee's food allergies.. [optional]  # noqa: E501
            probation_period (ProbationPeriod): [optional]  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            custom_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): When custom mappings are configured on the resource, the result is included here.. [optional]  # noqa: E501
            row_version (str, none_type): A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.. [optional]  # noqa: E501
            deleted (bool, none_type): Flag to indicate if the object is deleted.. [optional]  # noqa: E501
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
