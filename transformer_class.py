"""Class instance for BETYdb CSV file upload transformer
"""

import argparse


class Transformer():
    """Generic class for supporting transformers
    """
    def __init__(self, **kwargs):
        """Performs initialization of class instance
        Arguments:
            kwargs: additional parameters passed into Transformer instance
        """
        # pylint: disable=unused-argument
        self.args = None

    def get_transformer_params(self, args: argparse.Namespace, metadata: list) -> dict:
        """Returns a parameter list for processing data
        Arguments:
            args: result of calling argparse.parse_args
            metadata: the list of loaded metadata
        Return:
            A dictionary of parameter names and value to pass to transformer
        """
        # pylint: disable=unused-argument
        self.args = args
        # Get the list of files, if there are some
        file_list = []
        if args.file_list:
            for one_file in args.file_list:
                # Filter out arguments that are obviously not files
                if not one_file.startswith('-'):
                    file_list.append(one_file)

        params = {'check_md': {
            'working_folder': args.working_space,
            'list_files': lambda: file_list
        }}
        return params
