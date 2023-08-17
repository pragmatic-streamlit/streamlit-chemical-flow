
import os
import streamlit.components.v1 as components
from base64 import b64encode

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_DEVELOP_MODE = os.getenv('DEVELOP_MODE')
# _DEVELOP_MODE = True

_RELEASE = not _DEVELOP_MODE

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("streamlit_chemical_flow_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "streamlit_chemical_flow_component",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("streamlit_chemical_flow_component", path=build_dir)


def chemical_flow(nodes, edges, height="240px", key=None):
    params = {
        "height": height,
        "nodes": nodes,
        "edges": edges
    }
    return _component_func(key=key, default=None, **params)


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run streamlit_chemical_flow_component/__init__.py`
if not _RELEASE:
    import streamlit as st
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
