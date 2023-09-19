import { memo } from "react";
import { Handle, NodeProps, Position } from "reactflow";

import Molecule from "./Molecule";
import React from "react";

const ReactionNode = ({
                          isConnectable,
                          targetPosition = Position.Left,
                          sourcePosition = Position.Right
                      }: NodeProps) => {
    return (
        <div className=".react-flow__node-reaction">
            <Handle
                type="target"
                position={targetPosition}
                isConnectable={isConnectable}
            />
            <div>
                <div style={{ width: '100%', height: '100%' }}>
                    +
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

ReactionNode.displayName = "ReactionNode";

export default memo(ReactionNode);
