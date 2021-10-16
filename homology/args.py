# encode=utf-8
import os
import shutil


class Args:
    def __init__(self):
        # get pytorch path
        self.root_dir = os.path.abspath('../..')

        self.homology_dir = os.path.join(self.root_dir, "data", "homology")
        # source file
        self.source_xlsx_file = 'source-data.xlsx'
        self.homology_file = os.path.join(self.homology_dir, self.source_xlsx_file)
        # get absolute file path and file name suffix
        file_absolute_dir, file_name_suffix = os.path.splitext(self.homology_file)

        self.result_non_homology_file = file_absolute_dir + 'non+homology' + file_name_suffix

        # fasta
        self.fasta_dir_path = os.path.join(self.homology_dir, "fasta")

        # source result file
        self.result_sequence_file = os.path.join(self.homology_dir, 'res-sequence.txt')
        self.result_score_file = os.path.join(self.homology_dir, 'res-score.txt')

        # score less 50, and save entry number
        self.result_homology_file = os.path.join(self.homology_dir, 'res-homology.txt')

        # from res-homology.txt and set up fasta string to the file
        self.check_result_homology_file = os.path.join(self.homology_dir, 'check-result-homology-fasta.txt')

        # check result file
        self.check_result_fasta_file = os.path.join(self.homology_dir, 'check-result.txt')


if __name__ == '__main__':
    args = Args()
    print(f'{args.homology_file}')
    print(f'{args.fasta_dir_path}')
    print(f'{args.result_sequence_file}')
    print(f'{args.result_score_file}')


