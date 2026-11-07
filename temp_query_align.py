from modeller import *
from modeller.environ import Environ
env= Environ()
aln= alignment(env)
mdl = model(env, file='model_01')
aln.append_model(mdl,align_codes='model_01',atom_files='model_01.pdb')
aln.append(file='query.ali', align_codes='model_01')
aln.align2d()
aln.write(file='output.ali',alignment_format='PIR')
aln.write(file='output.pap',alignment_format='PAP')

