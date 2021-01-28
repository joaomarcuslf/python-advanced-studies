class CompressedGene:
    def __init__(self, gene):
        self._compress(gene)
        self._compress2(gene)

    def _compress2(self, gene):
        gene_dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

        self.bit_string2 = 0

        for nucleotide in gene.upper():
            if gene_dict[nucleotide]:
                self.bit_string2 = (self.bit_string2*10) + \
                    gene_dict[nucleotide]
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress2(self):
        gene_dict = {'1': 'A', '2': 'C', '3': 'G', '4': 'T'}
        gene = ""

        for i in str(self.bit_string2):
            if gene_dict[i]:
                gene += gene_dict[i]
            else:
                raise ValueError("Invalid bits:{}".format(i))
        return gene

    def _compress(self, gene):
        gene_dict = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}

        self.bit_string = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide in gene_dict:
                self.bit_string |= gene_dict[nucleotide]
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self):
        gene_dict = {0b00: 'A', 0b01: 'C', 0b10: 'G', 0b11: 'T'}
        gene = ""

        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits = self.bit_string >> i & 0b11

            if bits in gene_dict:
                gene += gene_dict[bits]
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self):
        return self.decompress()


""" USAGE:
from sys import getsizeof
original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
print("original is {} bytes".format(getsizeof(original)))
compressed: CompressedGene = CompressedGene(original)  # compress
print("compressed1 is {} bytes".format(getsizeof(compressed.bit_string)))
print("compressed2 is {} bytes".format(getsizeof(compressed.bit_string2)))
print("original and decompressed are the same: {}".format(
    original == compressed.decompress()))
print("original and decompressed are the same: {}".format(
    original == compressed.decompress2()))
"""

"""
This code was built based on the book:
- Classic Computer Science Problems in Python by David Kopec
"""
