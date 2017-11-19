import re
##print(re.split(r'(s*)','here are some words'))

##print(re.split(r'[a-n][a-n]','jshbchbskhzmnbkhsBJHDSBCCMCNBBMcbd'),
 ##     re.I|re.M) 

print(re.findall(r'\d{1,5}\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\.','cacdc1253 W 5th st Apt 42 Chico california 95928.sddv'))
