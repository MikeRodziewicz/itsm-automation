from searches.itsm_searches import inc_search, wo_search, inc_wo_req_search
from argparse import ArgumentParser



def _setup_inc_search_subparser(subparsers):
    subparser = subparsers.add_parser(
        'inc_search', description=(
            'Converts excel column for incidents into txt format for ITSM Remedy'
        )
    )
    subparser.set_defaults(subcommand=inc_search)


def _setup_wo_search_subparser(subparsers):
    subparser = subparsers.add_parser(
        'wo_search', description=(
            'Converts excel column for workorders into txt format for ITSM Remedy'
        )
    )
    subparser.set_defaults(subcommand=wo_search)


def _setup_inc_wo_req_search(subparsers):
    subparser = subparsers.add_parser(
        'inc_wo_req_search', description=(
            'Conversts INC and WO columnts into two txt files for ITSM remedy'
        )
    )
    subparser.set_defaults(subcommand=inc_wo_req_search)



def _setup_subparsers(main_parser):
    subparsers = main_parser.add_subparsers(dest='subcommand', required=True)
    _setup_inc_search_subparser(subparsers)
    _setup_wo_search_subparser(subparsers)
    _setup_inc_wo_req_search(subparsers)


def parse_args():
    parser = ArgumentParser(description='Search string creation script')
    _setup_subparsers(parser)
    return vars(parser.parse_args())


def main():
    parsed_args = parse_args()
    subcommand = parsed_args.pop('subcommand')
    subcommand(**parsed_args)


if __name__ == '__main__':
    main()