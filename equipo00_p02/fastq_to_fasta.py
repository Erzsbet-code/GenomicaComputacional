import sys

def fastq_to_fasta(input_file, output_file):

	with open(input_file, 'r') as i_f:

		lines = i_f.read().split('\n')

		output_lines = list()

		for i, line in enumerate(lines):

			if '@' in line:

				output_lines.append(line)

				output_lines.append(lines[i + 1])

		output_lines = list(map(lambda x: x.replace('@', '>'), output_lines))

		with open(output_file, 'w') as o_f:

			o_f.write('\n'.join(output_lines))


if __name__ == '__main__':
	fastq_to_fasta(sys.argv[1], sys.argv[2])