# Bitcoin Mining Genesis Block in Python
A Python implementation of the Bitcoin mining algorithm

This small script is a pseudo-simulation of the Bitcoin Genesis block mining process.

Given the Genesis block's data, this script double-hashes it using SHA-256 and attempts to find a hash less than the Genesis target.

Please note for the academic purpose, all the header is fixed and only the nonce change.
In that example, the nonce start at 2083000000 so we need to increment by one 236893 time to get the magic nonce of 2083236893.
It take approximately 5 second on average computer to find the solution.

In the real circumstance the header has 4 variables that change between the 10 minutes average window. The variables is :  **merkle_root, timestamp, size_bits and nonce**. So the code do not reflect the reality because in that case only the nonce is changing but it's easier to understand and enable to find the same parameter of the first mining block header.


In case that the block contain only one transaction, the merkle_root is equal to the hash of the transaction. It was the case of the first mining block. The list of tx was only one transaction.

```js
tx: [
  "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b"
],
```
so the tx expressed in little Indian is :
```
3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a
```

| Variable | circumstance of change |
| ------ | ------ |
| merkle_root | when the new transactions is added to the memory pool, the merkle root is recalculated |
| timestamp | when the second change (the Epoch) |
| size_bits | when the new transactions is added to the memory pool |
| nonce | with the random generator |

## Sample Output
![Sample output](./data/command_example.png)
