
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
        "streamlit_molecule_item_component",
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
    _component_func = components.declare_component("streamlit_molecule_item_component", path=build_dir)


def molecule_item(value, height="100px", key=None):
    params = {
        "height": height,
        "value": value
    }
    return _component_func(key=key, **params)


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run streamlit_chemical_flow_component/__init__.py`
if not _RELEASE:
    import streamlit as st
    st.text("debug mode")
    molecule_item(value="CC(=O)Oc1ccccc1C(=O)O", key="a", height="100px")
    col1, col2, col3 = st.columns(3)
    with col1:
        a = molecule_item(value="CN")
        if a:
            st.text(a)
    with col2:
        a = molecule_item(value="CCO")
        if a:
            st.text(a)
    with col3:
        a = molecule_item(value="CC(=O)Oc1ccccc1C(=O)O", key="b")
        if a:
            st.text(a)
