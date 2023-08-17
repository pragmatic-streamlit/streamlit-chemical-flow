import { memo } from "react";
import { Handle, NodeProps, Position } from "reactflow";
import { useCallback } from 'react';

import Molecule from "./Molecule";

const MoleculeNode = ({
                          data,
                          isConnectable,
                          targetPosition = Position.Right,
                          sourcePosition = Position.Bottom
                      }: NodeProps) => {
    const onChange = useCallback((evt: { target: { value: any; }; }) => {
        console.log(evt.target.value);
    }, []);
    return (
        <div className=".react-flow__node-molecule">
            <Handle
                type="target"
                position={targetPosition}
                isConnectable={isConnectable}

            />
            <div>
                <div>
                    <label>{data?.label}</label>
                </div>
                <div style={{ width: '100%', height: '100%' }}>
                    <Molecule smiles={data?.value} />
                </div>
            </div>
            <Handle
                type="source"
                position={sourcePosition}
                isConnectable={isConnectable}
            />
        </div>
    );
};

MoleculeNode.displayName = "MoleculeNode";

export default memo(MoleculeNode);
