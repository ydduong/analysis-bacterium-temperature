# encode=utf-8
import os

from homology.args import Args


def merge_fasta(args):
    homology_dir = args.homology_dir
    all_fasta_file = os.path.join(homology_dir, 'all-fasta.txt')

    if os.path.exists(all_fasta_file):
        os.remove(all_fasta_file)

    # source data dir
    fasta_data_dir = args.fasta_dir_path

    fasta_files = os.listdir(fasta_data_dir)
    print(f'fasta file num: {len(fasta_files)}')

    fasta_absolute_files = list()
    for file in fasta_files:
        fasta_absolute_files.append(os.path.join(fasta_data_dir, file))

    # print(fasta_absolute_files)
    with open(all_fasta_file, 'a', encoding='utf-8') as writer:
        for file in fasta_absolute_files:
            with open(file, 'r', encoding='utf-8') as reader:
                data = reader.read()
                if data is not None:
                    writer.write(data)
                    # writer.write('\n')
                else:
                    print(f'data is None: {file}')


if __name__ == '__main__':
    merge_fasta(Args())







