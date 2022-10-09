import sys

def LCS(seq1, seq2):
	dp_array = [[0 for i in range(len(seq2)+1)] for _ in range(len(seq1)+1)]
	str_array = [["" for i in range(len(seq2)+1)] for _ in range(len(seq1)+1)]
    print(dp_array)
	answer_str = []
	for i in range(1, len(seq1)+1):
		for j in range(1, len(seq2)+1):
			if seq1[i-1] == seq2[j-1]:
				dp_array[i][j] = dp_array[i-1][j-1] + 1
				str_array[i][j] = str_array[i-1][j-1] + str(seq2[j-1])
			else:
				if dp_array[i][j-1] < dp_array[i-1][j]:
					dp_array[i][j] = dp_array[i-1][j]
					str_array[i][j] = str_array[i-1][j]
				else:
					dp_array[i][j] = dp_array[i][j-1]
					str_array[i][j] = str_array[i][j-1]
	print(dp_array[len(seq1)][len(seq2)]-1)
	print(str_array[len(seq1)][len(seq2)])

	
seq1 = sys.stdin.readline()
seq2 = sys.stdin.readline()
LCS(seq1, seq2)

