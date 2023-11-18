def detect_palindromic(dat):
     return ((dat['reference_allele'] == "T") & (dat['other_allele'] == "A") |
            (dat['reference_allele'] == "A") & (dat['other_allele'] == "T") |
            (dat['reference_allele'] == "G") & (dat['other_allele'] == "C") |
            (dat['reference_allele'] == "C") & (dat['other_allele'] == "G"))

def detect_within_thresh(dat, threshold):
    return abs(dat['eaf'] - 0.5) < threshold
