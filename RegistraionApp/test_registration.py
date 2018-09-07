import unittest
from registration import Registration


class RegistrationTest(unittest.TestCase):

    
    def setUp(self):
        self.register = Registration()

    def test_register_creation(self):
        self.assertIsInstance(self.register, Registration)

    def test_user_bio_length(self):
        self.register.add('info@example.com', 'john', 'mike')
        self.assertEqual(self.register.user_bio_length(self.register.user_bio), 1)    

    def test_add_user(self):
        self.register.add('info@example.com','John doe', 'mike')
        self.assertEqual(len(self.register.user_bio), 1)

    # def test_check_file_exist(self):
    #     pass
    
    # def test_add_member(self):
    #     pass

    def test_missing_key(self):
        with self.assertRaises(KeyError):
            self.register.get_email('info@example.com')

    @unittest.skip('WIP')
    def test_unknown_method(self):
        pass #self.assertEqual(self.register.some_method(), 1)

