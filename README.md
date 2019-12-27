# Bitcoin Mining Genesis Block in Python
A Python implementation of the Bitcoin mining algorithm

This small script is a pseudo-simulation of the Bitcoin Genesis block mining process.

Given the Genesis block's data, this script double-hashes it using SHA-256 and attempts to find a hash less than the Genesis target.

Please note for the academic purpose, all the header is fixed and only the nonce change.
In that example, the nonce start at 2083000000 so we need to increment by one, 236893 times to get the magic nonce of 2083236893.
It take approximately 5 second on average computer to find the solution.

In the real circumstance the header has 4 variables that can change between the 10 minutes average window. The variables is :  **merkle_root, timestamp, size_bits and nonce**. So the code do not reflect the reality because in that case only the nonce is changing but it's easier to understand and enable to find the same parameter of the first mining block header.

In case that the block contain only one transaction, the merkle_root is equal to the hash of the transaction. It was the case of the first mining block. The list of tx was only one transaction. The one that send the coinbase reward 50BTC to the adress `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa`

```js
tx: [
  "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b"
]
```
So the tx expressed in little Indian is (reverse order) is equal to the merkle_root :
```
3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a
```
You can browse the fist block at [blockchair](https://blockchair.com/bitcoin/block/0)

| Variable | circumstance of change |
| ------ | ------ |
| merkle_root | when the new transactions is added to the memory pool, the merkle root is recalculated |
| timestamp | when the second change (the Epoch) |
| size_bits | when the new transactions is added to the memory pool |
| nonce | with the random generator |

## Print the hexadecimal data block

If you have the bitcoin-qt wallet you can take a look of all the blockchain inside the folder blocks. The path differ from the os.

| OS | path of the blocks |
| ------ | ------ |
| Linux | ~/.bitcoin/blocks |
| MacOS | ~/Library/Application\ Support/Bitcoin/blocks |
| Windows | %APPDATA%\Bitcoin\blocks |

## To print the fist mined block
```
$ hexdump -C -n 293 blk00000.dat

00000000  f9 be b4 d9 1d 01 00 00  01 00 00 00 00 00 00 00  |................|
00000010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000020  00 00 00 00 00 00 00 00  00 00 00 00 3b a3 ed fd  |............;...|
00000030  7a 7b 12 b2 7a c7 2c 3e  67 76 8f 61 7f c8 1b c3  |z{..z.,>gv.a....|
00000040  88 8a 51 32 3a 9f b8 aa  4b 1e 5e 4a 29 ab 5f 49  |..Q2:...K.^J)._I|
00000050  ff ff 00 1d 1d ac 2b 7c  01 01 00 00 00 01 00 00  |......+|........|
00000060  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000070  00 00 00 00 00 00 00 00  00 00 00 00 00 00 ff ff  |................|
00000080  ff ff 4d 04 ff ff 00 1d  01 04 45 54 68 65 20 54  |..M.......EThe T|
00000090  69 6d 65 73 20 30 33 2f  4a 61 6e 2f 32 30 30 39  |imes 03/Jan/2009|
000000a0  20 43 68 61 6e 63 65 6c  6c 6f 72 20 6f 6e 20 62  | Chancellor on b|
000000b0  72 69 6e 6b 20 6f 66 20  73 65 63 6f 6e 64 20 62  |rink of second b|
000000c0  61 69 6c 6f 75 74 20 66  6f 72 20 62 61 6e 6b 73  |ailout for banks|
000000d0  ff ff ff ff 01 00 f2 05  2a 01 00 00 00 43 41 04  |........*....CA.|
000000e0  67 8a fd b0 fe 55 48 27  19 67 f1 a6 71 30 b7 10  |g....UH'.g..q0..|
000000f0  5c d6 a8 28 e0 39 09 a6  79 62 e0 ea 1f 61 de b6  |\..(.9..yb...a..|
00000100  49 f6 bc 3f 4c ef 38 c4  f3 55 04 e5 1e c1 12 de  |I..?L.8..U......|
00000110  5c 38 4d f7 ba 0b 8d 57  8a 4c 70 2b 6b f1 1d 5f  |\8M....W.Lp+k.._|
00000120  ac 00 00 00 00                                    |.....|
00000125
```

## To print the fist 3 mined blocks
```
$ hexdump -C  -n 739 blk00000.dat

00000000  f9 be b4 d9 1d 01 00 00  01 00 00 00 00 00 00 00  |................|
00000010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000020  00 00 00 00 00 00 00 00  00 00 00 00 3b a3 ed fd  |............;...|
00000030  7a 7b 12 b2 7a c7 2c 3e  67 76 8f 61 7f c8 1b c3  |z{..z.,>gv.a....|
00000040  88 8a 51 32 3a 9f b8 aa  4b 1e 5e 4a 29 ab 5f 49  |..Q2:...K.^J)._I|
00000050  ff ff 00 1d 1d ac 2b 7c  01 01 00 00 00 01 00 00  |......+|........|
00000060  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000070  00 00 00 00 00 00 00 00  00 00 00 00 00 00 ff ff  |................|
00000080  ff ff 4d 04 ff ff 00 1d  01 04 45 54 68 65 20 54  |..M.......EThe T|
00000090  69 6d 65 73 20 30 33 2f  4a 61 6e 2f 32 30 30 39  |imes 03/Jan/2009|
000000a0  20 43 68 61 6e 63 65 6c  6c 6f 72 20 6f 6e 20 62  | Chancellor on b|
000000b0  72 69 6e 6b 20 6f 66 20  73 65 63 6f 6e 64 20 62  |rink of second b|
000000c0  61 69 6c 6f 75 74 20 66  6f 72 20 62 61 6e 6b 73  |ailout for banks|
000000d0  ff ff ff ff 01 00 f2 05  2a 01 00 00 00 43 41 04  |........*....CA.|
000000e0  67 8a fd b0 fe 55 48 27  19 67 f1 a6 71 30 b7 10  |g....UH'.g..q0..|
000000f0  5c d6 a8 28 e0 39 09 a6  79 62 e0 ea 1f 61 de b6  |\..(.9..yb...a..|
00000100  49 f6 bc 3f 4c ef 38 c4  f3 55 04 e5 1e c1 12 de  |I..?L.8..U......|
00000110  5c 38 4d f7 ba 0b 8d 57  8a 4c 70 2b 6b f1 1d 5f  |\8M....W.Lp+k.._|
00000120  ac 00 00 00 00 f9 be b4  d9 d7 00 00 00 01 00 00  |................|
00000130  00 6f e2 8c 0a b6 f1 b3  72 c1 a6 a2 46 ae 63 f7  |.o......r...F.c.|
00000140  4f 93 1e 83 65 e1 5a 08  9c 68 d6 19 00 00 00 00  |O...e.Z..h......|
00000150  00 98 20 51 fd 1e 4b a7  44 bb be 68 0e 1f ee 14  |.. Q..K.D..h....|
00000160  67 7b a1 a3 c3 54 0b f7  b1 cd b6 06 e8 57 23 3e  |g{...T.......W#>|
00000170  0e 61 bc 66 49 ff ff 00  1d 01 e3 62 99 01 01 00  |.a.fI......b....|
00000180  00 00 01 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000190  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
000001a0  00 00 00 ff ff ff ff 07  04 ff ff 00 1d 01 04 ff  |................|
000001b0  ff ff ff 01 00 f2 05 2a  01 00 00 00 43 41 04 96  |.......*....CA..|
000001c0  b5 38 e8 53 51 9c 72 6a  2c 91 e6 1e c1 16 00 ae  |.8.SQ.rj,.......|
000001d0  13 90 81 3a 62 7c 66 fb  8b e7 94 7b e6 3c 52 da  |...:b|f....{.<R.|
000001e0  75 89 37 95 15 d4 e0 a6  04 f8 14 17 81 e6 22 94  |u.7...........".|
000001f0  72 11 66 bf 62 1e 73 a8  2c bf 23 42 c8 58 ee ac  |r.f.b.s.,.#B.X..|
00000200  00 00 00 00 f9 be b4 d9  d7 00 00 00 01 00 00 00  |................|
00000210  48 60 eb 18 bf 1b 16 20  e3 7e 94 90 fc 8a 42 75  |H`..... .~....Bu|
00000220  14 41 6f d7 51 59 ab 86  68 8e 9a 83 00 00 00 00  |.Ao.QY..h.......|
00000230  d5 fd cc 54 1e 25 de 1c  7a 5a dd ed f2 48 58 b8  |...T.%..zZ...HX.|
00000240  bb 66 5c 9f 36 ef 74 4e  e4 2c 31 60 22 c9 0f 9b  |.f\.6.tN.,1`"...|
00000250  b0 bc 66 49 ff ff 00 1d  08 d2 bd 61 01 01 00 00  |..fI.......a....|
00000260  00 01 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000270  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000280  00 00 ff ff ff ff 07 04  ff ff 00 1d 01 0b ff ff  |................|
00000290  ff ff 01 00 f2 05 2a 01  00 00 00 43 41 04 72 11  |......*....CA.r.|
000002a0  a8 24 f5 5b 50 52 28 e4  c3 d5 19 4c 1f cf aa 15  |.$.[PR(....L....|
000002b0  a4 56 ab df 37 f9 b9 d9  7a 40 40 af c0 73 de e6  |.V..7...z@@..s..|
000002c0  c8 90 64 98 4f 03 38 52  37 d9 21 67 c1 3e 23 64  |..d.O.8R7.!g.>#d|
000002d0  46 b4 17 ab 79 a0 fc ae  41 2a e3 31 6b 77 ac 00  |F...y...A*.1kw..|
000002e0  00 00 00                                          |...|
000002e3
```

## Sample Output
![Sample output](./data/command_example.png)
