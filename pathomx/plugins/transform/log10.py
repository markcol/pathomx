import numpy as np
output_data = np.log10(input_data)

# Generate simple result figure (using pathomx libs)
from pathomx.figures import spectra

View = spectra(output_data)
