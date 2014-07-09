import argparse

class HelpAction(argparse._HelpAction):

    def __call__(self, parser, namespace, values, option_string=None):
        parser.print_help()

        print("")
        print("Don't forget the base arguments - see cassandra-snapshotter --help")
        parser.exit()

