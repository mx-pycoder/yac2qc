#!/usr/bin/env python3

''' category mapping rules for yac2qc '''

# The MIT License (MIT)
#
# Copyright (c) 2015 mx[replace-this]pycoder.nl
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from collections import namedtuple as _namedtuple

# a mapping rule consists of the following fields:
#
# category     - the category to assign to the record
# code         - the 'code' of the original record
# namedesc     - the 'namedesc' of the original record
# otheraccount - the 'other account' of the original record
# description  - the 'description' of the original record
#
# When more than 1 field is set (i.e. not None), all these fields should match
# before the category is assigned to the record. A field 'matches' when the
# defined string in the rule is a substring of the field in the record
# (case-sensitive).
#
# run yac2qc.py with the -u parameter to get an idea about missing rules.


# namedtuple for the mapping rules
_rule = _namedtuple('mapping_rule', 'category code namedesc '
                                    'otheraccount description')

# just some examples with fake names and numbers.
# These should be modified for your own needs. Comments can be deleted.
rules = [
    # rule that matches when the transaction is from a 'Betaalautomaat (BA)'
    # and has the name 'special fuels incorporated'
    _rule('car - fuel', 'BA', 'special fuels incorporated', None, None),
    # similar for 'CleanFuelInc'
    _rule('car - fuel', 'BA', 'CleanFuelInc', None, None),
    # with my bank ST means 'deposit'
    _rule('cash - deposit', 'ST', None, None, None),
    # .. and 'GM' means 'withdrawal' at a cash machine
    _rule('cash - withdrawal', 'GM', None, None, None),
    # just some fake supermarkets
    _rule('supermarket - galbert geijn', 'BA', 'Galbert Geijn', None, None),
    _rule('supermarket - mega', 'BA', 'MEGA', None, None),
    _rule('supermarket - smallmart', 'BA', 'Small Mart', None, None),
    # and other types of stores
    _rule('store - Hamma', 'BA', 'Hamma', None, None),
    _rule('store - Gema', 'BA', 'GEMA', None, None),
    _rule('store - AEKI', 'BA', 'Inter AEKI Systems', None, None),
    _rule('store - warkei', 'BA', 'WarKei Bouwmarkt', None, None),
    # specific accounts can also be defined as follows
    _rule('account - savings', None, None, '0123456789', None),
    # when the account number matches and some number appears in the
    # 'description' field, this is a statement related to income tax
    _rule('taxes - income tax', None, None, '999999999999', '1111.1111.111'),
]

