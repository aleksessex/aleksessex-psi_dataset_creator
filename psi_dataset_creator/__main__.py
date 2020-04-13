import argparse
import sys
from psi_dataset_creator import generate_psi_dataset
import traceback

parser = argparse.ArgumentParser(
    description='A tool to generate synthetic datasets for PSI matching')

parser.add_argument(
    '--sender-size',
    nargs=1,
    type=int,
    default=[1000],
    help="Number of records in Sender's dataset Default = 1000")

parser.add_argument(
    '--receiver-size',
    nargs=1,
    type=int,
    default=[100],
    help="Number of records in Receiver's dataset. Default = 1000")

parser.add_argument('--num-common',
                    nargs=1,
                    type=int,
                    default=[10],
                    help="Number of elements to share in common. Default = 10")

parser.add_argument(
    '--record-length',
    nargs=1,
    type=int,
    default=[64],
    help="Length of synthetic data element in characters. Default = 32")

parser.add_argument('--output-path',
                    nargs=1,
                    type=str,
                    default="data/",
                    help="Output path. Default = data/")


def main():
    args = parser.parse_args()

    try:
        generate_psi_dataset.generate_data(args.sender_size[0],
                                           args.receiver_size[0],
                                           args.num_common[0],
                                           args.record_length[0],
                                           args.output_path)

    except ValueError:
        traceback.print_exc()
        sys.exit()


if __name__ == '__main__':
    main()
