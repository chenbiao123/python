#!/usr/bin/env python
"""Unit tests for project1.authentication module"""
from unittest import TestCase
from mock import patch
import project1.authentication as auth

class StandAloneTest(TestCase):
    """ Test the stand-alone model functions """
    @patch('__builtin__.open')
    def test_login(self,mock_open):
        """authentication.login 方法的正确传参情况测试"""
        mock_open.return_value.read.return_value= \
                "netease|password\n"
        self.assertTure(auth.login('netease','password'))

    @patch('__builtin__.open')
    def test_login_bad_creds(self,mock_open):
        """authentication.login 方法的错误传参情况测试"""
        mock_open.return_value.read.return_value= \
                "netease|password\n"
        self.assertTure(auth.login('netease','badpassword'))

    @patch('__builtin__.open')
    def test_login_error(self,mock_open):
        """authentication.login 方法的异常传参情况测试"""
        mock_open.side_effect = IOError()      
        self.assertTure(auth.login('netease','password'))
