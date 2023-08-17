import type { RDKitModule } from "@rdkit/rdkit";
import React, {useEffect, useState} from "react";

declare global {
    interface Window {
        RDKit: RDKitModule;
    }
}
interface  MoleculeProps {
    smiles: string;
}
function Molecule(props: MoleculeProps) {
    const [rdkitLoaded, setRdkitLoaded] = useState(false);

    useEffect(() => {
        window.initRDKitModule().then((rdkit) => {
            window.RDKit = rdkit;
            setRdkitLoaded(true);
        });
    }, []);

    return (
        <div>
            {rdkitLoaded ? (
                    <span
                        dangerouslySetInnerHTML={{
                    __html: window.RDKit.get_mol(props.smiles).get_svg(50, 50),
                }}
    />
) : (
        "Loading..."
    )}
        </div>
);
}

export default Molecule