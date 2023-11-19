# -*- coding: utf-8 -*-
from . import helpers

"""Functions for cleaning and subsetting GWAS summary stastistics,
    assumes GWAS are read in as pandas dataframe with headings:
    'p-value' for p-value
    'rs_number' for rsid
    'chromosome' for chromosome number
    'position' for position number in basepairs
    'reference_allele' for reference allele
    'other_allele' for other allele
    'eaf' for effect allele frequency
"""

def remove_palidromic_thresh(dat, threshold):
    """Remove palindromic SNPS within threshold of 0.5

    Keyword arguments:

    dat -- GWAS results in a pandas dataframe
    threshold -- allele frequency threshold about 0.5
    """
    return dat[~helpers.detect_palindromic(dat)
                | helpers.detect_palindromic(dat)
                & ~helpers.detect_within_thresh(dat, threshold)]

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
    return dat[(dat['chromosome'] == chr)
                & (dat['position'] > position - window*1000)
                & (dat['position'] < position + window*1000)]
