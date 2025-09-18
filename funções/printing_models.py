import printing_functions
from printing_functions import print_models
from printing_functions import print_models as pm
import printing_functions as pf
from printing_functions import *

unprinted_designs = ['iphone_case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
