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

    console.log("Molecule", props.smiles)

    return (
        <div>
            {rdkitLoaded ? (
                    <span
                        dangerouslySetInnerHTML={{
                    __html: window.RDKit.get_mol(props.smiles).get_svg(),
                }}
    />
) : (
        "Loading..."
    )}
        </div>
);
}

export default Molecule