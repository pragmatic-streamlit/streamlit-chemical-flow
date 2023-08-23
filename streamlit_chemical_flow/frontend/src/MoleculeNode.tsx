import { memo } from "react";
import { Handle, NodeProps, Position } from "reactflow";

import Molecule from "./Molecule";
import React from "react";

const MoleculeNode = ({
                          data,
                          isConnectable,
                          targetPosition = Position.Right,
                          sourcePosition = Position.Bottom
                      }: NodeProps) => {
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
