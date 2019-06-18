import unittest

from biothings_schema import Schema


class TestSchemaOrg(unittest.TestCase):
    """Using SchemaOrg Schema to test all functions in biothings_schema
    """
    def setUp(self):
        # preload schemaorg schema
        self.se = Schema()
        # test list_all_classes
        self.clses = self.se.list_all_classes()
        # test list_all_properties
        self.props = self.se.list_all_properties()

    def test_schemaclass_class(self):
        """ Test the SchemaClass Class using all classes in Schemaorg schema"""
        # loop through all classes
        for _cls in self.clses:
            # test get_class
            scls = self.se.get_class(_cls.name)
            # test describe function
            describe = scls.describe()

    def test_schemaproperty_class(self):
        """ Test the SchemaProperty Class using all classes in Schemaorg schema
        """
        # loop through all properties
        for _prop in self.props:
            # test get_property
            sp = self.se.get_property(_prop.name)
            # test describe function
            describe = sp.describe()


if __name__ == '__main__':
    unittest.main()
