test_str = 'Sequence 15555: tr|A0A4D8FFS6K9|A0A4D8S6K9_METPR   202 aa'

index1 = test_str.find('|')
index2 = test_str.rfind('|')
index3 = test_str.find(' ')
index4 = test_str.find(':')

print(test_str[index1+1:index2])
print(test_str[index3+1:index4])

line = 'Sequences (1200068:127005) Aligned. Score: 17.2999566'
sequence_start_index = line.find('(') + 1
sequence_middle_index = line.find(':')
sequence_end_index = line.find(')')

sequence_first_id = line[sequence_start_index:sequence_middle_index]
sequence_second_id = line[sequence_middle_index+1:sequence_end_index]

score_index = line.rfind(' ')
score = line[score_index:]

print(f'first: {sequence_first_id}, second: {sequence_second_id}, score: {score}')











