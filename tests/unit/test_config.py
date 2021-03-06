#!/usr/bin/env
# Copyright (c) 2012 Mitch Garnaat http://garnaat.org/
# Copyright 2012 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
import unittest
import os
import botocore.session
import botocore.exceptions


class TestConfig(unittest.TestCase):

    def test_config_not_found(self):
        config_path = os.path.join(os.path.dirname(__file__),
                                   'aws_config_notfound')
        os.environ['AWS_CONFIG_FILE'] = config_path
        session = botocore.session.get_session()
        self.assertRaises(botocore.exceptions.ConfigNotFound,
                          session.get_config)

    def test_config_parse_error(self):
        config_path = os.path.join(os.path.dirname(__file__),
                                   'aws_config_bad')
        os.environ['AWS_CONFIG_FILE'] = config_path
        session = botocore.session.get_session()
        self.assertRaises(botocore.exceptions.ConfigParseError,
                          session.get_config)


if __name__ == "__main__":
    unittest.main()
