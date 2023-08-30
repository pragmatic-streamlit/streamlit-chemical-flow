import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib"

import Molecule from "./Molecule";
import React from "react";
import {Edge, Handle, Node, NodeProps, Position} from "reactflow";

interface MoleculeItemData {
    value: string
}

const onClick = (data: MoleculeItemData) => {
    console.log(data);
    Streamlit.setComponentValue(data);
}
const MoleculeItem = ({
                          data,
                      }: any) => {
    return (
            <div onClick={() => onClick(data)}>
                <div>
                    <label>{data?.value}</label>
                </div>
                <div style={{ width: '100%', height: '100%' }}>
                    <Molecule smiles={data?.value} />
                </div>
            </div>

    );
};

export default withStreamlitConnection(MoleculeItem);
