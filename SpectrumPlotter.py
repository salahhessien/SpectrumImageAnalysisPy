import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import SpanSelector
from matplotlib.ticker import FuncFormatter

h = 6.626070040e-34
c = 299792458
eC = 1.6021766208e-19

class SpectrumPlotter(object):
	def __init__(self, spectrum, axis, colour='red'):
		'''Line plot with span selector
		   Input: matplotlib axis object, x and y data points
			 x and y are arrays for plotting against each other
		   '''
		self.main_axis = axis
		self.line_colour = colour
		self.linked_axis = self.main_axis.twiny()
		self.spectrum = spectrum
		self.main_axis.plot(spectrum.SpectrumRange, spectrum.intensity, self.line_colour)
		self.main_axis.set_xlabel(r"%s (%s)" % (spectrum.unit_label, spectrum.units))
		self.main_axis.set_ylabel(r"Intensity (a.u.)")
		self.setup_linked_axis(self.spectrum.SpectrumRange, 
			r"%s (%s)" % (self.spectrum.secondary_unit_label, self.spectrum.secondary_units), nmtoeV)
		self.linked_axis.format_coord = self.axis_display
		plt.gcf().canvas.draw()
		
	def setup_linked_axis(self, x_range, label, FormatFunction):
		self.linked_axis.plot(x_range, self.spectrum.intensity)
		self.linked_axis.clear()
		self.linked_axis.xaxis.set_major_formatter(FuncFormatter(FormatFunction))
		self.linked_axis.set_xlabel(label)
		
	def axis_display(self, x, y):
	    return '%s = %0.4g %s, %s = %0.3g %s, I = %0.5g' % (
	    	self.spectrum.unit_label, x, self.spectrum.units, 
	    	self.spectrum.secondary_unit_label, float(nmtoeV(x)), 
	    	self.spectrum.secondary_units, y)

def eVtonm(eV, pos=None):
    nm = h*c/(eC*abs(eV))*1e9
    if np.isfinite(nm): nm = int(nm)
    return "%.3g" % nm

def nmtoeV(nm, pos=None):
	eV = h*c/(eC*abs(nm))*1e9
	return "%.3g" % eV

