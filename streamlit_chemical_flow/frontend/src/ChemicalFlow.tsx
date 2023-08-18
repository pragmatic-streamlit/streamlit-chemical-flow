import 'reactflow/dist/style.css';
import "./molecule-node.css";
import Dagre from '@dagrejs/dagre';

import 'antd/dist/reset.css'
import React, {useEffect, useCallback} from 'react';
import ReactFlow, {
    Node,
    Edge,
    Connection,
    addEdge,
    Controls,
    Position,
    NodeChange,
    EdgeChange,
} from 'reactflow';
import {applyEdgeChanges, applyNodeChanges, useNodesState,
    useEdgesState} from 'reactflow';
import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib"

// @ts-ignore
import MoleculeNode from "./MoleculeNode";

enum StreamlitEventType {
    NODE = "node",
    EDGE = "edge"
}
interface StreamlitEvent {
    type: StreamlitEventType;
    nodes?: Node[],
    edges?: Edge[]
}

const nodeWidth = 172;
const nodeHeight = 36;
const g = new Dagre.graphlib.Graph().setDefaultEdgeLabel(() => ({}));
const getLayoutElements = (nodes: Node[], edges: Edge[], direction = 'LR') => {

    const isHorizontal = direction === 'LR';
    g.setGraph({ rankdir: direction });

    nodes.forEach((node) => {
        g.setNode(node.id, { width: nodeWidth, height: nodeHeight });
    });

    edges.forEach((edge) => {
        g.setEdge(edge.source, edge.target);
    });

    Dagre.layout(g);

    nodes.forEach((node: Node) => {
        const nodeWithPosition = g.node(node.id);
        node.targetPosition = isHorizontal ? 'left' as Position : 'top' as Position;
        node.sourcePosition = isHorizontal ? 'right' as Position : 'bottom' as Position;

        // We are shifting the dagre node position (anchor=center center) to the top left
        // so it matches the React ChemicalFlow node anchor point (top left).
        node.position = {
            x: nodeWithPosition.x - nodeWidth / 2,
            y: nodeWithPosition.y - nodeHeight / 2,
        };

        return node;
    });

    return { nodes, edges };
}

const nodeTypes = {molecule: MoleculeNode};
const defaultViewport = { x: 0, y: 0, zoom: 0.5 };
function ChemicalFlow({args}: ComponentProps): React.JSX.Element {
    // set height
    useEffect(() => {
        Streamlit.setFrameHeight(args.height || 500)
    })

    // def events
    const [
        nodesStates,
        setNodes,
    ] = useNodesState(args.nodes);
    const [
        edgesStates,
        setEdges,
    ] = useEdgesState(args.edges);

    const onNodesChange = useCallback(
        (changes: NodeChange[]) =>
            setNodes((nds) => applyNodeChanges(changes, nds)),
        [setNodes]
    );
    const onEdgesChange = useCallback(
        (changes: EdgeChange[]) =>
            setEdges((eds) => applyEdgeChanges(changes, eds)),
        [setEdges]
    );
    const onConnect = useCallback(
        (params: Edge | Connection) => setEdges((els) => addEdge(params, els)),
        [setEdges]
    );

    // return selection to streamlit
    const onNodeClick = (event: React.MouseEvent, node: any) => {
        // Handle node click event
        console.log('Node clicked:', node);
        Streamlit.setComponentValue({
            type: StreamlitEventType.NODE,
            nodes: [node]
        } as StreamlitEvent)
    };

    const onEdgeClick = (event: React.MouseEvent, edge: any) => {
        // Handle node click event
        console.log('Edge clicked:', edge);
        Streamlit.setComponentValue({
            type: StreamlitEventType.EDGE,
            edges: [edge]
        } as StreamlitEvent)
    };

    // auto layout
    getLayoutElements(
        args.nodes,
        args.edges,
        'LR'
    );

    return (
        <div style={{ width: '100%', height: args.height || '500px' }}>
            <ReactFlow nodes={nodesStates}
                       edges={edgesStates}
                       onNodesChange={onNodesChange}
                       onEdgesChange={onEdgesChange}
                       onConnect={onConnect}
                       onNodeClick={onNodeClick}
                       onEdgeClick={onEdgeClick}
                       nodeTypes={nodeTypes}
                       fitView
                       defaultViewport={defaultViewport}
                       attributionPosition="top-left" >
                <Controls />
            </ReactFlow>
        </div>
    );
}

export default withStreamlitConnection(ChemicalFlow);

