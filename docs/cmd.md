## get info for a specific block (genesis block)
```
bitcoin-cli getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

## python mining header (genesis block)
```
>>> import hashlib
>>> header_hex = ("01000000" +
 "0000000000000000000000000000000000000000000000000000000000000000" +
 "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a" +
 "29ab5f49" +
 "ffff001d" +
 "1dac2b7c")
>>> header_bin = header_hex.decode('hex')
>>> hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
>>> hash.encode('hex_codec')
'6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000'

>>> hash[::-1].encode('hex_codec')
'000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
```

## calc Merkle Root transaction Pizza

```
(export LC_ALL=C; xxd -revert -plain <<< 3bd3a1309a518c381248fdc26c3a6bd62c35db7705069f59206684308cc237b3 | rev | tr -d '\n' | xxd -plain | tr -d '\n')
(export LC_ALL=C; xxd -revert -plain <<< bd9075d78e65a98fb054cb33cf0ecf14e3e7f8b3150231df8680919a79ac8fe5 | rev | tr -d '\n' | xxd -plain | tr -d '\n')\n(export LC_ALL=C; xxd -revert -plain <<< a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d | rev | tr -d '\n' | xxd -plain | tr -d '\n')

echo -en "e58fac799a918086df310215b3f8e7e314cf0ecf33cb54b08fa9658ed77590bd8dd4f5fbd5e980fc02f35c6ce145935b11e284605bf599a13c6d415db55d07a1" | xxd -r -p | shasum -a 256
echo -en "57880d7f58935982cc2c0012c4961d5ce634103109ee9bf3e94bb7a98959d7f7"  | xxd -r -p | shasum -a 256

(export LC_ALL=C; xxd -revert -plain <<<  5a1b723ae6c479056af838a6ea40db6f4acee39f262bf49864cd98f511221d5c | rev | tr -d '\n' | xxd -plain | tr -d '\n')

5c1d2211f598cd6498f42b269fe3ce4a6fdb40eaa638f86a0579c4e63a721b5a
```
