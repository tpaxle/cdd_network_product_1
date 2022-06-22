import conf_diff
import argparse

def main():

    parser = argparse.ArgumentParser(
        prog="api_diff",
        description="""Diff between configs""",
    )
    parser.add_argument(
        "-a",
        "--source-a",
        action="store",
        dest="action_sourcea",
        help="Path to file",
        required=True,
    )
    parser.add_argument(
        "-b",
        "--source-b",
        action="store",
        dest="action_sourceb",
        help="Path to file",
        required=True,
    )    
    parser.add_argument(
        "-f",
        "--filename",
        action="store",
        dest="action_filename",
        help="Path to output file",
    )

    options = parser.parse_args()


    # Instantiate a class object 'html_diff'
    html_diff = conf_diff.ConfDiff(options.action_sourcea, options.action_sourceb, options.action_filename)

    # Generates a `sbx-nxos-mgmt.cisco.com_html_output.html` in your current directory unless expected absolute path is specified.
    html_diff.diff()

if __name__ == "__main__":
    main()