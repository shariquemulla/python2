from bokeh.plotting import figure
from bokeh.io import output_file,show

x=[1,2,3,4,5,6,9]
y=[10,2,35,14,15,26,129]

output_file('graph.html')

f=figure()
f.line(x,y)
f.circle(x,y)
show(f)