import os
import streamlit.components.v1 as components
from base64 import b64encode

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_DEVELOP_MODE = os.getenv("DEVELOP_MODE")
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
    _component_func = components.declare_component(
        "streamlit_chemical_flow_component", path=build_dir
    )


def chemical_flow(nodes, edges, height="240px", key=None):
    params = {"height": height, "nodes": nodes, "edges": edges}
    return _component_func(key=key, **params)


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run streamlit_chemical_flow_component/__init__.py`
if not _RELEASE:
    import streamlit as st

    # nodes = [
    #     {
    #         'id': '1',
    #         'data': {'value': 'c1ccccc1', 'label': 'c1ccccc1'},
    #         'type': 'molecule',
    #         'sourcePosition': 'right'
    #     },
    #     {
    #         'id': '2',
    #         'type': 'molecule',
    #         'data': {'value': 'CCO', 'label': 'CCO'}
    #     },
    #     {
    #         'id': '3',
    #         'type': 'molecule',
    #         'data': {'value': 'CC(=O)Oc1ccccc1C(=O)O', 'label': 'CC(=O)Oc1ccccc1C(=O)O'}
    #     }
    # ]
    #
    # edges = [
    #     {
    #         'id': '1-2',
    #         'source': '1',
    #         'target': '2',
    #         'label': '+',
    #         'type': 'step',
    #         'animated': True
    #     },
    #     {
    #         'id': '2-3',
    #         'source': '2',
    #         'target': '3',
    #         'label': 'expert',
    #         'type': 'molecule',
    #         'animated': True,
    #         'data': {'catalyst': 'CCO'},
    #         'markerEnd': {'type': 'arrow', 'color': '#000'}
    #     }
    # ]

    data = {
        "nodes": [
            {
                "id": "1",
                "data": {
                    "value": "CC(C)(C)[Si](C)(C)Cl",
                    "label": "CC(C)(C)[Si](C)(C)Cl",
                    "commercial": True,
                },
                "type": "molecule",
            },
            {
                "id": "2",
                "data": {
                    "value": "O=C1O[C@H](CO)[C@@H](O)[C@H]1O",
                    "label": "O=C1O[C@H](CO)[C@@H](O)[C@H]1O",
                    "commercial": True,
                },
                "type": "molecule",
            },
            {
                "id": "3",
                "data": {"value": "+", "label": "+"},
                "type": "reaction",
                "label": "+",
            },
            {
                "id": "4",
                "data": {
                    "value": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "label": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "commercial": False,
                },
                "type": "molecule",
            },
            {
                "id": "5",
                "data": {
                    "value": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "label": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "commercial": False,
                },
                "type": "molecule",
            },
            {
                "id": "6",
                "data": {
                    "value": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "label": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "commercial": False,
                },
                "type": "molecule",
            },
            {
                "id": "7",
                "data": {
                    "value": "CCC(CC)CO",
                    "label": "CCC(CC)CO",
                    "commercial": True,
                },
                "type": "molecule",
            },
            {
                "id": "8",
                "data": {
                    "value": "C[C@H](N)C(=O)O",
                    "label": "C[C@H](N)C(=O)O",
                    "commercial": True,
                },
                "type": "molecule",
            },
            {
                "id": "9",
                "data": {"value": "+", "label": "+"},
                "type": "reaction",
                "label": "+",
            },
            {
                "id": "10",
                "data": {
                    "value": "CCC(CC)COC(=O)[C@H](C)N",
                    "label": "CCC(CC)COC(=O)[C@H](C)N",
                    "commercial": False,
                },
                "type": "molecule",
            },
            {
                "id": "11",
                "data": {
                    "value": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1",
                    "label": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1",
                    "commercial": False,
                },
                "type": "molecule",
            },
            {
                "id": "12",
                "data": {"value": "+", "label": "+"},
                "type": "reaction",
                "label": "+",
            },
            {
                "id": "13",
                "data": {
                    "value": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1",
                    "label": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1",
                    "commercial": False,
                },
                "type": "molecule",
            },
            {
                "id": "14",
                "data": {
                    "value": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "label": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "commercial": False,
                },
                "type": "molecule",
            },
        ],
        "edges": [
            {
                "id": "1-3",
                "source": "1",
                "target": "3",
                "type": "step",
                "animated": True,
            },
            {
                "id": "2-3",
                "source": "2",
                "target": "3",
                "type": "step",
                "animated": True,
            },
            {
                "id": "3-4",
                "source": "3",
                "label": "transformer_network",
                "data": {"catalyst": ""},
                "target": "4",
                "type": "molecule",
                "animated": True,
            },
            {
                "id": "4-5",
                "source": "4",
                "label": "database",
                "data": {"catalyst": "Nc1ncnn2c(I)ccc12"},
                "target": "5",
                "type": "molecule",
                "animated": True,
            },
            {
                "id": "5-6",
                "source": "5",
                "label": "database",
                "data": {"catalyst": "C[Si](C)(C)C#N.O=C(O)C(F)(F)F"},
                "target": "6",
                "type": "molecule",
                "animated": True,
            },
            {
                "id": "7-9",
                "source": "7",
                "target": "9",
                "type": "step",
                "animated": True,
            },
            {
                "id": "8-9",
                "source": "8",
                "target": "9",
                "type": "step",
                "animated": True,
            },
            {
                "id": "9-10",
                "source": "9",
                "label": "database",
                "data": {"catalyst": ""},
                "target": "10",
                "type": "molecule",
                "animated": True,
            },
            {
                "id": "10-11",
                "source": "10",
                "label": "transformer_network",
                "data": {"catalyst": "O=P(Cl)(Cl)c1ccccc1.Oc1c(F)c(F)c(F)c(F)c1F"},
                "target": "11",
                "type": "molecule",
                "animated": True,
            },
            {
                "id": "6-12",
                "source": "6",
                "target": "12",
                "type": "step",
                "animated": True,
            },
            {
                "id": "11-12",
                "source": "11",
                "target": "12",
                "type": "step",
                "animated": True,
            },
            {
                "id": "12-13",
                "source": "12",
                "label": "transformer_network",
                "data": {"catalyst": ""},
                "target": "13",
                "type": "molecule",
                "animated": True,
            },
            {
                "id": "13-14",
                "source": "13",
                "label": "expert_system",
                "data": {"catalyst": ""},
                "target": "14",
                "type": "molecule",
                "animated": True,
            },
        ],
        "backup_reactions": {
            "CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C": [
                {
                    "smiles": "CC(C)(C)[Si](C)(C)Cl.CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O)[C@@H]1O[Si](C)(C)C(C)(C)C>>CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "reaction_type": "transformer_network",
                    "confidence_score": -0.07182464748620987,
                    "probability": -0.06447131931781769,
                },
                {
                    "smiles": "CC(C)(C)[Si](C)(C)Cl.O=C1O[C@H](CO)[C@@H](O)[C@H]1O>>CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "reaction_type": "transformer_network",
                    "confidence_score": -0.07855594903230667,
                    "probability": -0.08524945378303528,
                },
            ],
            "CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C": [
                {
                    "smiles": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C.Nc1ncnn2c(I)ccc12>Cl[Mg]c1ccccc1.C[Si](C)(C)Cl.CC(C)[Mg]Cl.C1CCOC1.Cl[La](Cl)Cl>CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "reaction_type": "database",
                    "confidence_score": 1.0,
                    "probability": 1.0,
                },
                {
                    "smiles": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C.Nc1ncnn2c(Br)ccc12>C[Si](C)(C)Cl.[Li]CCCC.C1CCOC1>CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "reaction_type": "similarity",
                    "confidence_score": 0.6923076808452606,
                    "probability": -0.05715880170464516,
                },
                {
                    "smiles": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@H]1O[Si](C)(C)C(C)(C)C.Nc1ncnn2c(I)ccc12>>CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "reaction_type": "transformer_network",
                    "confidence_score": -0.0757591724395752,
                    "probability": -0.05034976080060005,
                },
            ],
            "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C": [
                {
                    "smiles": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C.C[Si](C)(C)C#N.O=C(O)C(F)(F)F>C[Si](C)(C)OS(=O)(=O)C(F)(F)F.CCN(CC)CC.ClCCl.O>CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "reaction_type": "database",
                    "confidence_score": 1.0,
                    "probability": 1.0,
                },
                {
                    "smiles": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C>C[Si](C)(C)OS(=O)(=O)C(F)(F)F.O=C(O)C(F)(F)F.C[Si](C)(C)C#N.ClCCl>CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "reaction_type": "database",
                    "confidence_score": 1.0,
                    "probability": 1.0,
                },
                {
                    "smiles": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO[Si](C)(C)C)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C>>CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C",
                    "reaction_type": "transformer_network",
                    "confidence_score": -0.056912995874881744,
                    "probability": -0.08038846403360367,
                },
            ],
            "CCC(CC)COC(=O)[C@H](C)N": [
                {
                    "smiles": "CCC(CC)CO.C[C@H](N)C(=O)O>CCCC(C)C.Cc1ccccc1.Cc1ccc(S(=O)(=O)O)cc1>CCC(CC)COC(=O)[C@H](C)N",
                    "reaction_type": "database",
                    "confidence_score": 1.0,
                    "probability": 1.0,
                },
                {
                    "smiles": "CCOC(=O)[C@H](C)N.Cl.O=P(Cl)(Cl)Oc1ccccc1>ClCCl>CCC(CC)COC(=O)[C@H](C)N",
                    "reaction_type": "database",
                    "confidence_score": 1.0,
                    "probability": 1.0,
                },
                {
                    "smiles": "CCC(CC)CO.C[C@H](NC(=O)OC(C)(C)C)C(=O)O>C[Si](C)(C)Cl>CCC(CC)COC(=O)[C@H](C)N",
                    "reaction_type": "database",
                    "confidence_score": 1.0,
                    "probability": 1.0,
                },
            ],
            "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1": [
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N.O=P(Cl)(Cl)c1ccccc1.Oc1c(F)c(F)c(F)c(F)c1F>>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1",
                    "reaction_type": "transformer_network",
                    "confidence_score": -0.04458966106176376,
                    "probability": -0.09628116339445114,
                }
            ],
            "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1": [
                {
                    "smiles": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C.CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1>>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1",
                    "reaction_type": "transformer_network",
                    "confidence_score": -0.028011322021484375,
                    "probability": -0.056453727185726166,
                },
                {
                    "smiles": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@H](O[Si](C)(C)C(C)(C)C)[C@](C#N)(c2ccc3c(N)ncnn23)O[C@@H]1CO.CCC(CC)COC(=O)[C@H](C)N[P@@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1>>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1",
                    "reaction_type": "transformer_network",
                    "confidence_score": -0.04624204337596893,
                    "probability": -0.05625361204147339,
                },
            ],
            "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1": [
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@H]1O[C@H](C)CC(=O)O)c1ccccc1>C1CCOC1.CC(C)(C)[O-].[K+]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H](O[C@H](C)CC(=O)O)[C@H]1O[C@H](C)CC(=O)O)c1ccccc1>C1CCOC1.CC(C)(C)[O-].[K+]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H](O[C@H](C)CC(=O)O)[C@@H]1O)c1ccccc1>C1CCOC1.CC(C)(C)[O-].[K+]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O[Si](c1ccccc1)(c1ccccc1)C(C)(C)C)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](c2ccccc2)(c2ccccc2)C(C)(C)C)[C@@H]1O[Si](c1ccccc1)(c1ccccc1)C(C)(C)C)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](c2ccccc2)(c2ccccc2)C(C)(C)C)[C@@H]1O)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NC(C)=O)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>O.CCO.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N4C(=O)c5ccccc5C4=O)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>NN.O.CCO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NS(=O)(=O)c4ccc(C)cc4)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>[MgH2].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "C=CCOC(=O)Nc1ncnn2c([C@]3(C#N)O[C@H](CO[P@@](=O)(N[C@@H](C)C(=O)OCC(CC)CC)c4ccccc4)[C@@H](O)[C@H]3O)ccc12>C1CCNC1.O.C1COCCO1.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N(C(=O)OC(C)(C)C)C(=O)OC(C)(C)C)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>CCOC(=O)C.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]2OC(C)(C)O[C@H]12)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NC=O)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>O.Cc1ccccc1.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NCc4ccccc4)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>[H][H].[Pd].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N(Cc4ccccc4)Cc4ccccc4)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>[H][H].[Pd].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "C=CCN(CC=C)c1ncnn2c([C@]3(C#N)O[C@H](CO[P@@](=O)(N[C@@H](C)C(=O)OCC(CC)CC)c4ccccc4)[C@@H](O)[C@H]3O)ccc12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.CN1C(=O)CC(=O)N(C)C1=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NC(=O)OCC[Si](C)(C)C)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC.C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC=O)c1ccccc1>[BH4-].[Na+].C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC=O)[C@@H]1OC=O)c1ccccc1>[BH4-].[Na+].C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC=O)[C@@H]1O)c1ccccc1>[BH4-].[Na+].C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC(=O)c1ccc(C)cc1)c1ccccc1>[NH2-].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC(=O)c2ccc(C)cc2)[C@@H]1OC(=O)c1ccc(C)cc1)c1ccccc1>[NH2-].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC(=O)c2ccc(C)cc2)[C@@H]1O)c1ccccc1>[NH2-].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC1CCCCO1)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC2CCCCO2)[C@@H]1OC1CCCCO1)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC2CCCCO2)[C@@H]1O)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC(=O)c1ccccc1)c1ccccc1>O.C[O-].[Na+].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC(=O)c2ccccc2)[C@@H]1OC(=O)c1ccccc1)c1ccccc1>O.C[O-].[Na+].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC(=O)c2ccccc2)[C@@H]1O)c1ccccc1>O.C[O-].[Na+].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@@H]1C=C[C@](C#N)(c2ccc3c(N)ncnn23)O1)c1ccccc1>N=O.O=[Os](=O)(=O)=O.O.CC(C)=O>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(-n4c(C)ccc4C)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>CCO.Cl.NO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N=C(c4ccccc4)c4ccccc4)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC)c1ccccc1>B(Br)(Br)Br.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC)[C@@H]1OC)c1ccccc1>B(Br)(Br)Br.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC)[C@@H]1O)c1ccccc1>B(Br)(Br)Br.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]2OC(c3ccccc3)O[C@H]12)c1ccccc1>[H][H].[Pd]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NC(=O)OC(C)(C)C)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>CCOC(=O)C.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
                {
                    "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]2O[Si](C(C)(C)C)(C(C)(C)C)O[C@H]12)c1ccccc1>C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                    "reaction_type": "expert_system",
                    "confidence_score": 0.8,
                    "probability": 0.8,
                },
            ],
        },
    }

    selected_event = chemical_flow(data["nodes"], data["edges"], height="460px")

    if selected_event:
        st.json(selected_event)
        print(f"selected {selected_event}")
