import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib"

import Molecule from "./Molecule";
import React from "react";
import "./molecule-item.css";

interface MoleculeItemData {
    value: string
}

const onClick = (data: MoleculeItemData) => {
    console.log("clicked", data);
    Streamlit.setComponentValue(data);
}
function MoleculeItem({args}: ComponentProps): React.JSX.Element {
    const height = args.height || '100px';
    Streamlit.setFrameHeight(height)
    return (
            // set onclick to div onclick event
            <div onClick={() => onClick(args.value)} className="molecule-item">
                <Molecule smiles={args.value} />
            </div>
    );
};

export default withStreamlitConnection(MoleculeItem);
