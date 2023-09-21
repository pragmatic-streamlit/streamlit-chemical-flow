import {
    ComponentProps,
    Streamlit,
    withStreamlitConnection,
} from "streamlit-component-lib"

import {FullScreen, useFullScreenHandle} from "react-full-screen"
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
    const handler = useFullScreenHandle()
    Streamlit.setFrameHeight(height)

    return (
        <div>
           {/*<button className="fullscreen-button" onClick={handler.enter}>*/}
           {/*     <span></span>*/}
           {/*     <span></span>*/}
           {/*     <span></span>*/}
           {/*     <span></span>*/}
           {/* </button>*/}
            <FullScreen className="myfullscreen" handle={handler}>
                <div onClick={handler.enter} className="molecule-item">
                    <Molecule smiles={args.value}/>
                </div>
            </FullScreen>
        </div>
    )
};

export default withStreamlitConnection(MoleculeItem);
