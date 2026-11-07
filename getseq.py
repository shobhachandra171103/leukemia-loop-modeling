from modeller import *
# Get the sequence of the PDB file, and write to an alignment file
code = 'model_01'

e = Environ()
m = Model(e, file=code)
aln = Alignment(e)
aln.append_model(m, align_codes=code)
aln.write(file=code+'.ali')