#!/usr/bin/env python

# Copyright (c) 2020, Atsuto Seko
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of the phonopy project nor the
#   names of its contributors may be used to endorse or promote products
#   derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT
# HOLDER> BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import numpy as np
import os
import argparse
import sqlite3

default_database = (
    '/'.join(__file__.split('/')[:-1]) + '/recommender-2024-07-01.sqlite'
)

ps = argparse.ArgumentParser()
ps.add_argument(
    '-d', 
    '--database', 
    type=str, 
    default=default_database,
    help='Database name'
)
ps.add_argument(
    '-n', 
    '--nary',
    type=int,
    nargs='*',
    default=[3],
    help='Number of atomic species in recommended compositions'
)
ps.add_argument(
    '-e',
    '--elements',
    type=str,
    nargs='*',
    default=[],
    help='Elements in recommended compositions'
)
ps.add_argument(
    '--threshold', 
    type=float, 
    default=0.01,
    help='Score threshold for recommendation'
)
args = ps.parse_args()


print("Read from", args.database)

if max(args.nary) > 5 or 1 in args.nary:
    print("Only binary, ternary, quaternary, and quinary compositions are available.")
if 4 in args.nary:
    print("Only ionic compositions are available for -n 4 option.")
if 5 in args.nary:
    print("Only ionic compositions are available for -n 5 option.")

conn = sqlite3.connect(args.database)
resall = []
if 2 in args.nary:
    res = conn.execute('select * from data2')
    resall.extend(res.fetchall())
if 3 in args.nary:
    res = conn.execute('select * from data3')
    resall.extend(res.fetchall())
if 4 in args.nary:
    res = conn.execute('select * from data4ionic')
    resall.extend(res.fetchall())
if 5 in args.nary:
    res = conn.execute('select * from data5ionic')
    resall.extend(res.fetchall())

output = []
for d in resall:
    size = int((len(d)-2) / 2)
    if (
        d[-1] > args.threshold and len(set(args.elements) & set(d[1:size+1]))
    ) == len(args.elements):
        output.append((d[0], d[-1]))

output = sorted(output,key=lambda x: x[1],reverse=True)
print('# Composition, Score')
for comp, score in output:
    print(' ', comp, ' ', score)

