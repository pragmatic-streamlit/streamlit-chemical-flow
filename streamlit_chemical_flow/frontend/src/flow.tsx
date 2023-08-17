import 'reactflow/dist/style.css';
import "./molecule-node.css";
import Dagre from '@dagrejs/dagre';
import { Button } from 'antd';
import type {  ButtonType } from 'antd/lib/button/buttonHelpers';

import 'antd/dist/reset.css'
import React, {useState, useCallback} from 'react';
import ReactFlow, {
    Node,
    Edge,
    Connection,
    addEdge,
    Controls,
    Position,
    EdgeMarker,
    NodeChange,
    EdgeChange,
    Panel
} from 'reactflow';
import {applyEdgeChanges, applyNodeChanges, useNodesState,
    useEdgesState} from 'reactflow';
import MoleculeNode from "./moleculeNode";

const position = { x: 0, y: 0 };

const initialNodes: Node[] = [
    {
        id: '1',
        position: position,
        data: {value: 'c1ccccc1', label: 'c1ccccc1'},
        type: 'molecule',
        sourcePosition: 'right' as Position,

    },
    {
        id: '2',
        type: 'molecule',
        position: position,
        data: {value: 'CCO', label: 'CCO'},
    },
    {
        id: '3',
        type: 'molecule',
        position: position,
        data: {value: 'CC(=O)Oc1ccccc1C(=O)O', label: 'CC(=O)Oc1ccccc1C(=O)O'},
    }
];

const initialEdges: Edge[] = [
    {
        id: '1-2',
        source: '1',
        target: '2',
        label: '+',
        type: 'step',
        animated: true,
    },
    {
        id: '2-3',
        source: '2',
        target: '3',
        label: 'expert',
        type: 'step',
        animated: true,
        markerEnd: {type: 'arrow', color: '#000'} as EdgeMarker,
    },
];
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
        // so it matches the React Flow node anchor point (top left).
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
function Flow() {
    const [nodesStates, setNodes, nNodesChange] = useNodesState(initialNodes);
    const [edgesStates, setEdges, ] = useEdgesState(initialEdges);
    const [redesignButtonType, setRedesignButtonType] = useState<ButtonType>('dashed'); // 默认按钮类型
    const [rerunButtonType, setRerunButtonType] = useState<ButtonType>('dashed'); // 默认按钮类型

    const onNodesChange = useCallback(
        (changes: NodeChange[]) =>
            setNodes((nds) => applyNodeChanges(changes, nds)),
        []
    );
    const onEdgesChange = useCallback(
        (changes: EdgeChange[]) =>
            setEdges((eds) => applyEdgeChanges(changes, eds)),
        []
    );
    const onConnect = useCallback(
        (params: Edge | Connection) => setEdges((els) => addEdge(params, els)),
        [setEdges]
    );

    const onNodeClick = (event: React.MouseEvent, node: any) => {
        // Handle node click event
        console.log('Node clicked:', node);
        setRedesignButtonType('primary');
        setRerunButtonType('dashed');

    };

    const onEdgeClick = (event: React.MouseEvent, edge: any) => {
        // Handle node click event
        console.log('Edge clicked:', edge);
        setRedesignButtonType('dashed');
        setRerunButtonType('primary');
    };

    getLayoutElements(
        initialNodes,
        initialEdges,
        'LR'
    );

    return (
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

            {/*<Panel position="top-right">*/}
            {/*    <Button id={'redesign'} type={redesignButtonType}>Re-design selected molecule</Button>*/}
            {/*    <Button id={'rerun'} type={rerunButtonType}>Re-run retro pipeline</Button>*/}
            {/*</Panel>*/}
            <Controls />
        </ReactFlow>

    );
}

export default Flow;

