## get info for a specific block (geneis block)
```
bitcoin-cli getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

## python mining header
```
>>> import hashlib
>>> header_hex = ("01000000" +
 "81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000" +
 "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b" +
 "c7f5d74d" +
 "f2b9441a" +
 "42a14695")
>>> header_bin = header_hex.decode('hex')
>>> hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
>>> hash.encode('hex_codec')
'1dbd981fe6985776b644b173a4d0385ddc1aa2a829688d1e0000000000000000'
>>> hash[::-1].encode('hex_codec')
'00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'
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
