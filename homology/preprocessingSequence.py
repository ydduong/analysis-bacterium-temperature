# encode=utf-8
import os

from homology.args import Args


def processing_sequence(args):
    # dict form res-sequence
    result_sequence_file = args.result_sequence_file
    result_score_file = args.result_score_file

    result_homology_file = args.result_homology_file
    if os.path.exists(result_homology_file):
        os.remove(result_homology_file)

    # set sequence dict
    sequence_dict = dict()
    with open(result_sequence_file, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()
        print(f'sequence lines: {len(lines)}')
        print(f'e.g. {lines[0].strip()}\n')
        for line in lines:
            line = line.strip()

            sequence_id_start_index = line.find(' ') + 1
            sequence_id_end_index = line.find(':')
            sequence_id = line[sequence_id_start_index:sequence_id_end_index]

            entry_start_index = line.find('|') + 1
            entry_end_index = line.rfind('|')
            entry = line[entry_start_index:entry_end_index]

            # print(f'sequence id: {sequence_id}, entry: {entry}')
            sequence_dict[int(sequence_id)] = entry

    # print(sequence_dict)
    score_is_then_50 = [False] * len(sequence_dict)
    with open(result_score_file, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()
        # print(f'score lines: {len(lines)}')
        # print(f'e.g. {lines[0].strip()}\n')
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
                # print(line)
                score_is_then_50[int(sequence_second_id)-1] = True

    # print(score_is_then_50)
    with open(result_homology_file, 'w', encoding='utf-8') as writer:
        for index in range(len(score_is_then_50)):
            if score_is_then_50[index] is False:
                writer.write(sequence_dict[index+1])
                writer.write('\n')


if __name__ == '__main__':
    processing_sequence(Args())




