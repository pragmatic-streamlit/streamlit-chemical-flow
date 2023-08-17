# streamlit-chemical-flow

## Install
`pip install streamlit-chemical-flow`

## Usage

```python
import streamlit as st
from streamlit_chemical_flow import chemical_flow
nodes = [
    {
        'id': '1',
        'data': {'value': 'c1ccccc1', 'label': 'c1ccccc1'},
        'type': 'molecule',
        'sourcePosition': 'right'
    },
    {
        'id': '2',
        'type': 'molecule',
        'data': {'value': 'CCO', 'label': 'CCO'}
    },
    {
        'id': '3',
        'type': 'molecule',
        'data': {'value': 'CC(=O)Oc1ccccc1C(=O)O', 'label': 'CC(=O)Oc1ccccc1C(=O)O'}
    }
]

edges = [
    {
        'id': '1-2',
        'source': '1',
        'target': '2',
        'label': '+',
        'type': 'step',
        'animated': True
    },
    {
        'id': '2-3',
        'source': '2',
        'target': '3',
        'label': 'expert',
        'type': 'step',
        'animated': True,
        'markerEnd': {'type': 'arrow', 'color': '#000'}
    }
]
selected_node, selected_edge = chemical_flow(nodes, edges)
if selected_node:
    print(f"node selected {selected_node}")
if selected_edge:
    print(f"edge selected {selected_edge}")
```
