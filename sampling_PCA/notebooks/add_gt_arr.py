#!python3
import numpy as np
# import scikit-allel
import allel
# import click
'''
add_gt_arr() takes genotype array from 1000 Genomes VCF
and saves a .npy byte array with processed diploid genotypes
'''
#
# click.command()
# @click.option('--slimoutputfile',default = '',
#                     help = 'SLiM output file')
def add_gt_arr():
    GT = allel.read_vcf('../../data/vcf/ALL.chr21.phase3_shapeit2_mvncall_'
                     +'integrated_v5a.20130502.genotypes.vcf.gz',
                    fields = ['calldata/GT'])
    GT = GT['calldata/GT']
    GT[GT> 0] = 1
    np.save('summarized_genotypes',np.sum(GT,axis=2))

if __name__ == "__main__":
    add_gt_arr()
