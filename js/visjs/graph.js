// render container
const container = document.getElementById('network');

// nodes dataset
const nodes = new vis.DataSet([
  { id: 1, label: 'Node 1' },
  { id: 2, label: 'Node 2' },
  { id: 3, label: 'Node 3' },
  { id: 4, label: 'Node 4' },
  { id: 5, label: 'Node 5' },
]);

// edges dataset
const edges = new vis.DataSet([
  { from: 1, to: 2 },
  { from: 1, to: 3 },
  { from: 2, to: 4 },
  { from: 2, to: 5 },
  { from: 3, to: 5 },
]);

// create graph data
const data = {
  nodes: nodes,
  edges: edges,
};

// graph options
const options = {
  nodes: {
    shape: 'circle',
    size: 20,
    font: {
      size: 14,
      color: '#ffffff',
    },
    color: {
      background: '#007bff',
      border: '#0056b3',
    },
    borderWidth: 2,
  },
  edges: {
    color: '#848484',
    arrows: {
      to: { enabled: true, scaleFactor: 1 },
    },
  },
  physics: {
    enabled: true,
  },
};

// init network
const network = new vis.Network(container, data, options);
