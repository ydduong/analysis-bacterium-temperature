# encode=utf-8
import os
import sys

from homology.args import Args
from homology.preprocessingSequence import processing_sequence
from homology.filterResult import filter_result

def processing_html(args):
    # find html file
    result_html_file = None
    homology_dir_files = os.listdir(args.homology_dir)
    for file_name in homology_dir_files:
        if file_name.find('.html') != -1:
            result_html_file = os.path.join(args.homology_dir, file_name)
    if result_html_file is None:
        print(f'not find html file!')
        sys.exit(1)
    else:
        print(f'using: {result_html_file}')

    # save middle result file
    result_sequence_file = args.result_sequence_file
    result_score_file = args.result_score_file

    if os.path.exists(result_sequence_file):
        os.remove(result_sequence_file)
    if os.path.exists(result_score_file):
        os.remove(result_score_file)

    # open
    result_sequence_file_writer = open(result_sequence_file, 'a', encoding='utf-8')
    result_score_file_writer = open(result_score_file, 'a', encoding='utf-8')

    with open(result_html_file, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()
        for line in lines:
            line = line.strip() + '\n'
            if line.find('Sequences (') != -1 and line.find('Score:') != -1:
                result_score_file_writer.write(line)
            if line.find('Sequence ') != -1 and line.find(': tr|') != -1:
                result_sequence_file_writer.write(line)

    # close
    result_sequence_file_writer.close()
    result_score_file_writer.close()


if __name__ == '__main__':
    args = Args()
    processing_html(args)
    processing_sequence(args)
    filter_result(args)




