# encode=utf-8
import os.path

from homology.args import Args

args = Args()

# result_homology =
check_result_homology = args.check_result_homology_file
if os.path.exists(check_result_homology):
    os.remove(check_result_homology)

fasta_dir = args.fasta_dir_path

result_homology = args.result_homology_file

with open(check_result_homology, 'w', encoding='utf-8') as writer:
    with open(result_homology, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()
        for line in lines:
            line = line.strip()
            file = os.path.join(fasta_dir, line) + '.txt'
            if os.path.exists(file):
                with open(file, 'r', encoding='utf-8') as f:
                    data = f.read()
                    writer.write(data)
            else:
                print(file)













