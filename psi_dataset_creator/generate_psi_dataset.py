import random
import os
from pathlib import Path
import secrets
import sys
import traceback


def generate_random_records(num_records, record_length):
    """Return a list containing num_records random strings of length
    record_length"""
    return [secrets.token_urlsafe(record_length) for i in range(num_records)]


def generate_data(sender_size, receiver_size, num_common, record_length,
                  output_path):
    if any(num_common > i for i in (sender_size, receiver_size)):
        raise ValueError('Number of common records cannot exceed dataset size')

    if any(i <= 1
           for i in [sender_size, receiver_size, num_common, record_length]):
        raise ValueError('Arguments must be greater than 1')

    if not Path(output_path).exists():
        try:
            os.mkdir(output_path)
        except OSError:
            print("Output directory could not be created")
            traceback.print_exc()
            sys.exit()

    common_records = generate_random_records(num_common, record_length)

    sender_records = generate_random_records(sender_size - num_common,
                                             record_length) + common_records

    receiver_records = generate_random_records(receiver_size - num_common,
                                               record_length) + common_records

    random.shuffle(sender_records)
    random.shuffle(receiver_records)

    with open(output_path + "sender-records.txt", "w") as fs:
        for record in sender_records:
            fs.write(record + '\n')

    with open(output_path + "receiver-records.txt", "w") as fr:
        for record in receiver_records:
            fr.write(record + '\n')

    with open(output_path + "common-records.txt", "w") as fc:
        for record in common_records:
            fc.write(record + '\n')
