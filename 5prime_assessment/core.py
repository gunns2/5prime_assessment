# -*- coding: utf-8 -*-
from . import helpers

def remove_palidromic_thresh(dat, threshold):
        """Remove palindromic SNPS within threshold of 0.5

        Keyword arguments:

        dat -- GWAS results in a pandas dataframe
        threshold -- allele frequency threshold about 0.5
        """
    return dat[~detect_palindromic(dat) | detect_palindromic(dat) & ~detect_within_thresh(dat, threshold)]

def count_sig(dat):
    """Sums number of SNPs with p-value below 5e-08"""
 return sum(dat['p-value'] < 5e-08)

def clean_dat_rsids(dat):
    """Returns dataframe with only valid rsids"""
    return dat[dat['rs_number'].str.contains('rs')]

def return_window(dat, chr, position, window):
    """Subset GWAS results to window about certain variant

    Keyword arguments:

    dat -- GWAS results in a pandas dataframe
    chr -- chromosome of variant
    position -- position of variant
    window -- window in kilobases about the variant to be returned
    """
    return dat[(dat['chromosome'] == chr) & (df_rs['position'] > position - window*1000) & (df_rs['position'] < position + window*1000)]
