# coding: utf-8

"""
    Swagger Petstore

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.pets_api import PetsApi


class TestPetsApi(unittest.TestCase):
    """PetsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PetsApi()

    def tearDown(self) -> None:
        pass

    def test_create_pets(self) -> None:
        """Test case for create_pets

        Create a pet
        """
        pass

    def test_list_pets(self) -> None:
        """Test case for list_pets

        List all pets
        """
        pass

    def test_show_pet_by_id(self) -> None:
        """Test case for show_pet_by_id

        Info for a specific pet
        """
        pass


if __name__ == '__main__':
    unittest.main()
