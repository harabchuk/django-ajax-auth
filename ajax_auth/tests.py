"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .services import AuthHelper


class AuthHelperTest(TestCase):

    def test_is_email(self):
        self.assertTrue(AuthHelper.is_email('aaa@bbb.com'))
        self.assertTrue(AuthHelper.is_email('aaa+1@bbb.com'))
        self.assertTrue(AuthHelper.is_email('aa.bb@bbb.com'))
        self.assertTrue(AuthHelper.is_email('aa_bb@bbb.com'))
        self.assertTrue(AuthHelper.is_email('aa_bb@domain.by'))
        self.assertFalse(AuthHelper.is_email('aa_bb'))
        self.assertFalse(AuthHelper.is_email('aa_bb@aaa'))
        self.assertFalse(AuthHelper.is_email('@'))
        self.assertFalse(AuthHelper.is_email(''))

    def test_truncate(self):
        self.assertEqual(len(AuthHelper.truncate('aaa')), 3)
        self.assertEqual(len(AuthHelper.truncate('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')), 30)

        self.assertEqual(AuthHelper.truncate('bb@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com'), 'bb')
        self.assertEqual(AuthHelper.truncate('bb@aaaa.com'), 'bb@aaaa.com')

    def test_normalize(self):
        self.assertEqual(AuthHelper.normalize('aaa'), 'aaa')
        self.assertEqual(AuthHelper.normalize('aaa@bbb.com'), 'aaa@bbb.com')
        self.assertEqual(AuthHelper.normalize('bb@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com'), 'bb')