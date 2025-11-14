# Mii.fu

Core Mii implementation in [Fusion](https://fusion-lang.org/).

So far, the only thing written is `FFLResource`, which should allow you to load `FFLRes*.dat` files. Soon enough, I will provide examples (e.g. a three.js renderer of shapes) to show that this works.

## Building

Fusion is reaaaally whacky when it comes to building, it involves a lot of long commands, because fusion dosen't have imports :)
First, it's probably a good idea to grab the latest version of `mii-fusion-experiments` like so:
```bash
git submodule update --recursive --remote mii-fusion-experiments
```

Great, now on to generating source files! Make sure you have [fut](https://github.com/fusionlanguage/fut) installed, then run the following.
```bash
fut -D CPP -n miifu -l cpp src/Readers.fu src/FFLResource.fu -o gen/FFLResource.cpp
fut -D CPP -n miifu -l cpp mii-fusion-experiments/Ver3StoreData/Ver3CharInfo.fu mii-fusion-experiments/Ver3StoreData/Ver3StoreData.fu mii-fusion-experiments/Ver3StoreData/Crc16Ccitt.fu mii-fusion-experiments/Ver3StoreData/Utf16ToUtf8Converter.fu -o gen/Ver3StoreData.cpp
```
Be sure to replace `-l cpp`, all `.cpp` extensions and `-D CPP` with the language you're generating for.

You can of course output everything to one source file, like so:
```bash
fut -D CPP -n miifu -l cpp src/Readers.fu src/FFLResource.fu mii-fusion-experiments/Ver3StoreData/Ver3CharInfo.fu mii-fusion-experiments/Ver3StoreData/Ver3StoreData.fu mii-fusion-experiments/Ver3StoreData/Crc16Ccitt.fu mii-fusion-experiments/Ver3StoreData/Utf16ToUtf8Converter.fu -o gen/MiiFU.cpp
```

> [!NOTE]
> You should define the target language using `-D` due to some functions having optimised versions for certain languages.

## TODOs

#### Core

* [ ] `FFLResource` full implementation (textures & shapes)
* [X] `Ver3StoreData` (from Arian's repo)
* [ ] `Expression`
* [ ] `FFLDatabase`

#### API-Specific

* [ ] An FFL render server (like [mii-unsecure](https://mii-unsecure.ariankordi.net/))
* [X] Implement in [GDFL](https://github.com/GloriousGlider8/GDFL) (GoDot Face Library)
* [ ] three.js impl.

#### Extras

* [ ] Extended file format support (`rsd`, `charinfo` and maybe even  `miic`..?)
* [ ] Custom Expression support..?
* [ ] Godot Mii Maker..?
* [ ] Data Conversions
