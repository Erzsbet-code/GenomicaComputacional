import sys

def fastq_to_fasta(input_file, output_file):

	with open(input_file, 'r') as i_f:

		lines = list(filter(lambda l: len(l) > 0, i_f.read().split('\n')))

		output_lines = list()

		for j in range(0, len(lines), 2):

			header, sequence = tuple(lines[j: j + 2])

			if header[0] == '@':

				output_lines.append(header)

				output_lines.append(sequence)

		output_lines = list(map(lambda x: x.replace('@', '>'), output_lines))

		with open(output_file, 'w') as o_f:

			o_f.write('\n'.join(output_lines))


if __name__ == '__main__':
	fastq_to_fasta(sys.argv[1], sys.argv[2])