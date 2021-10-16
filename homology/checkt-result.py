# encode=utf-8
import os.path

from homology.args import Args

args = Args()

# result_homology =

check_result = args.check_result_fasta_file

with open(check_result, 'r', encoding='utf-8') as reader:
    lines = reader.readlines()
    print(f'score lines: {len(lines)}')
    print(f'e.g. {lines[0].strip()}\n')
    for line in lines:
        line = line.strip()

        sequence_start_index = line.find('(') + 1
        sequence_middle_index = line.find(':')
        sequence_end_index = line.find(')')

        sequence_first_id = line[sequence_start_index:sequence_middle_index]
        sequence_second_id = line[sequence_middle_index + 1:sequence_end_index]

        score_index = line.rfind(' ')
        score = line[score_index:]

        # print(f'first: {sequence_first_id}, second: {sequence_second_id}, score: {score}')

        if float(score) > 50:
            print(line)








