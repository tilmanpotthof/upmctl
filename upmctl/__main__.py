# Copyright (c) 2016, Tobias Schaefer
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of upmctl nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import argparse
from client import Client
from plugins import list_plugins


def stype(bytestring):
    unicode_string = bytestring.decode(sys.listfilesystemencoding())
    return unicode_string


def parse_options():
    parser = argparse.ArgumentParser(description='upmctl')
    parser.add_argument('--base-url',
                        type=unicode,
                        help='Confluence URL')
    parser.add_argument('--base-authentication',
                        type=unicode,
                        help='base authentication user, password')
    parser.add_argument('--configuration-file',
                        type=stype,
                        help='configuration file')
    subparsers = parser.add_subparsers()

    parser_list = subparsers.add_parser('list')
    parser_list.set_defaults(list=True)
    parser_list.add_argument('--user',
                             action='store_true',
                             help='list user installed plugins')
    parser_list.add_argument('--system',
                             action='store_true',
                             help='list system plugins')

    return parser.parse_args()


def run(args):
    client = Client(base_url=args.base_url,
                    base_auth=args.base_authentication)

    if hasattr(args, 'list'):
        if args.user:
            plugins = list_plugins(client, True)
        elif args.system:
            plugins = list_plugins(client, False)
        else:
            plugins = list_plugins(client, None)
        for plugin in plugins:
            print plugin


def main():
    args = parse_options()
    run(args)


if __name__ == '__main__':
    main()
