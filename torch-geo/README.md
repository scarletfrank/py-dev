# README

## Datasets

一个吸引人的地方就是，这个库带了很多预制数据集，对原数据进行下载，并写好了处理方案。

## Mini-batches

对于图来说，也要遵循`batch-wise`的方式。`torch-geometric`通过创建`sparse block diagonal adjacency matrices`来实现mini-batch的并行，在节点的维度对特征和目标矩阵进行拼接。

## COO

```
 COO format
 [
    [src1, ..., srcn],
    [dest1, ..., destn]
 ]
```
data.x Node feature matrix with shape [num_nodes, num_nodes_features]

data.edge_index Graph connectivity in COO format with shape [2, num_edges] and type torch.long
