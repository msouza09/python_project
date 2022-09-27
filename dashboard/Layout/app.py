from rich import print 
from rich.layout import Layout
from rich.panel import Panel

layout = Layout()
layout.split_column(
    Layout(Panel('Meu app', style='on green')),
    Layout(name='topo'),
    Layout(name='baixo'),
    Layout(Panel('Criador: Jhonatan', style='purple'))
)

layout['topo'].split_row(
    Layout(Panel('Esquerda')),
    Layout(Panel('Direita'))
)
print(layout)