# Changelog

## 3.10.0 (2025-12-19)

Full Changelog: [v3.9.0...v3.10.0](https://github.com/digitalocean/gradient-python/compare/v3.9.0...v3.10.0)

### Features

* **api:** manual updates ([f1c2eb2](https://github.com/digitalocean/gradient-python/commit/f1c2eb25ae1787b661ab1323528077074aa0cab6))
* **api:** manual updates ([355e13f](https://github.com/digitalocean/gradient-python/commit/355e13f1a4b012e09bc2056179419ede57044b97))


### Bug Fixes

* restore inference endpoints ([#120](https://github.com/digitalocean/gradient-python/issues/120)) ([ee792a1](https://github.com/digitalocean/gradient-python/commit/ee792a181e819d8fa26712fe8bc96ffd4c02d2ed))


### Chores

* **internal:** add `--fix` argument to lint script ([2825cb7](https://github.com/digitalocean/gradient-python/commit/2825cb750edd261a324c2da28afc3cb6ee90f5e9))
* run smoke tests on prs ([#121](https://github.com/digitalocean/gradient-python/issues/121)) ([719a5fb](https://github.com/digitalocean/gradient-python/commit/719a5fb4fcf418db9ede5659710377a47d41b6a8))

## 3.9.0 (2025-12-17)

Full Changelog: [v3.8.0...v3.9.0](https://github.com/digitalocean/gradient-python/compare/v3.8.0...v3.9.0)

### Features

* **api:** update via SDK Studio ([4173864](https://github.com/digitalocean/gradient-python/commit/4173864db71088fb5a2e3fc8033462580bb66603))
* **api:** update via SDK Studio ([f6b12b8](https://github.com/digitalocean/gradient-python/commit/f6b12b8a67014dd608d8260c056d1c75342edda6))
* **api:** update via SDK Studio ([a9cd7d3](https://github.com/digitalocean/gradient-python/commit/a9cd7d3bc6e2e988901e31064a4e607059c7ac09))


### Bug Fixes

* ensure streams are always closed ([80881b5](https://github.com/digitalocean/gradient-python/commit/80881b5248ac8baa2b34043df1d20086f319d2d1))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([b400d38](https://github.com/digitalocean/gradient-python/commit/b400d3808dc93924d7d44b25714bb53ef220bfe8))
* use async_to_httpx_files in patch method ([33d2306](https://github.com/digitalocean/gradient-python/commit/33d2306ee7211b7180ab156697159b9aa02d564e))


### Chores

* add missing docstrings ([9ac1364](https://github.com/digitalocean/gradient-python/commit/9ac136400dbd411b3d2177d20b255b0572861c48))
* add Python 3.14 classifier and testing ([db08b3f](https://github.com/digitalocean/gradient-python/commit/db08b3fb9a7d07ff02a8d45804647ce7c1e34e5a))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([4710dcd](https://github.com/digitalocean/gradient-python/commit/4710dcdcc4600546a048e2769abeee056d9383f6))
* **docs:** use environment variables for authentication in code snippets ([47b051a](https://github.com/digitalocean/gradient-python/commit/47b051af6578df97f84464ae40f04f957a00160a))
* **internal:** add missing files argument to base client ([8ffa56c](https://github.com/digitalocean/gradient-python/commit/8ffa56c38b3816d5598d83976030e1a8706ec45e))
* update lockfile ([516734f](https://github.com/digitalocean/gradient-python/commit/516734f2d19eb314061fb27c049a878b8c766313))

## 3.8.0 (2025-11-20)

Full Changelog: [v3.7.0...v3.8.0](https://github.com/digitalocean/gradient-python/compare/v3.7.0...v3.8.0)

### Features

* **api:** manual updates ([244277b](https://github.com/digitalocean/gradient-python/commit/244277b483ac97f733e8f37e0b556cb49813b554))

## 3.7.0 (2025-11-19)

Full Changelog: [v3.6.0...v3.7.0](https://github.com/digitalocean/gradient-python/compare/v3.6.0...v3.7.0)

### Features

* add wait_for_completion method to IndexingJobs resource with sy… ([#49](https://github.com/digitalocean/gradient-python/issues/49)) ([9edc2a6](https://github.com/digitalocean/gradient-python/commit/9edc2a60f5aa49749e151477615bbecb3a79e92b))
* Add wait_until_ready() method for agent deployment polling ([#56](https://github.com/digitalocean/gradient-python/issues/56)) ([dcef3d5](https://github.com/digitalocean/gradient-python/commit/dcef3d5ebb4ef903c0c91aa4008853bb978f5544))
* **api:** add inference errors ([d61d495](https://github.com/digitalocean/gradient-python/commit/d61d4955f596d9ac1bebc9387a6573989e823022))
* **api:** include indexing jobs ([d249d06](https://github.com/digitalocean/gradient-python/commit/d249d0606e26d585eb2b7859948a796ea7860f53))


### Bug Fixes

* **client:** close streams without requiring full consumption ([33fe04b](https://github.com/digitalocean/gradient-python/commit/33fe04b2e4ab71094ee13e7b83d4c04867e7d485))
* compat with Python 3.14 ([add7b21](https://github.com/digitalocean/gradient-python/commit/add7b21b9fbb8987641d5520da638647fe27b159))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([c945870](https://github.com/digitalocean/gradient-python/commit/c945870a31840d553cb1e3a75314f1c884a56060))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([db39cc6](https://github.com/digitalocean/gradient-python/commit/db39cc63fb126ac81edfe2cb991493d10a2d0936))
* **internal/tests:** avoid race condition with implicit client cleanup ([e0202bb](https://github.com/digitalocean/gradient-python/commit/e0202bb915613872095f7f223a49c4480e50be98))
* **internal:** grammar fix (it's -&gt; its) ([c6ffb3b](https://github.com/digitalocean/gradient-python/commit/c6ffb3becbcb99e36992934fac20d67a6a3b967c))
* merge issues in test_client.py ([#87](https://github.com/digitalocean/gradient-python/issues/87)) ([62fc025](https://github.com/digitalocean/gradient-python/commit/62fc02512e941c6af18b11c19df8828cca31159d))
* **package:** drop Python 3.8 support ([825b1e4](https://github.com/digitalocean/gradient-python/commit/825b1e4f8b257fc103c0d45743133bbc81ca3e10))

## 3.6.0 (2025-10-16)

Full Changelog: [v3.5.0...v3.6.0](https://github.com/digitalocean/gradient-python/compare/v3.5.0...v3.6.0)

### Features

* **api:** manual updates ([da88e9e](https://github.com/digitalocean/gradient-python/commit/da88e9eee0adc6152d0d8212305397483be0d686))


### Bug Fixes

* lints ([a1b1fc6](https://github.com/digitalocean/gradient-python/commit/a1b1fc6b7747c00d9bfc2b86c6262e9c123416dc))
* test setup needs all three access keys ([01ac735](https://github.com/digitalocean/gradient-python/commit/01ac735fb965686699df82ec8763b18ceb660972))

## 3.5.0 (2025-10-14)

Full Changelog: [v3.4.0...v3.5.0](https://github.com/digitalocean/gradient-python/compare/v3.4.0...v3.5.0)

### Features

* **api:** update via SDK Studio ([#74](https://github.com/digitalocean/gradient-python/issues/74)) ([e1ab040](https://github.com/digitalocean/gradient-python/commit/e1ab0407e88f5394f5c299940a4b2fe72dbbf70e))


### Chores

* **internal:** detect missing future annotations with ruff ([0fb9f92](https://github.com/digitalocean/gradient-python/commit/0fb9f9254a0f72a721fa73823399e58eec723f1a))

## 3.4.0 (2025-10-09)

Full Changelog: [v3.3.0...v3.4.0](https://github.com/digitalocean/gradient-python/compare/v3.3.0...v3.4.0)

### Features

* **api:** manual updates ([bbd7ddc](https://github.com/digitalocean/gradient-python/commit/bbd7ddccfb3d98f39e61948365b92202b3cc9e33))

## 3.3.0 (2025-10-07)

Full Changelog: [v3.2.0...v3.3.0](https://github.com/digitalocean/gradient-python/compare/v3.2.0...v3.3.0)

### Features

* **api:** Images generations - openai ([e5a309e](https://github.com/digitalocean/gradient-python/commit/e5a309e46bf05846c580f425e6fa23f323138a4d))
* **api:** update via SDK Studio ([c2bf693](https://github.com/digitalocean/gradient-python/commit/c2bf693d233830dafdfc2aa7f74e2ced2e8d81a0))

## 3.2.0 (2025-10-06)

Full Changelog: [v3.1.0...v3.2.0](https://github.com/digitalocean/gradient-python/compare/v3.1.0...v3.2.0)

### Features

* **api:** Images generations ([37bf67a](https://github.com/digitalocean/gradient-python/commit/37bf67af6097a6396e8f96a64d9224312355ff0f))

## 3.1.0 (2025-10-03)

Full Changelog: [v3.0.2...v3.1.0](https://github.com/digitalocean/gradient-python/compare/v3.0.2...v3.1.0)

### Features

* **api:** update via SDK Studio ([20f2512](https://github.com/digitalocean/gradient-python/commit/20f251223fbe35fbe170b07be41fa6fd2656eed7))
* **api:** update via SDK Studio ([09bf61b](https://github.com/digitalocean/gradient-python/commit/09bf61b5c24b1299a84ea6e8d4df3b88118d9fc3))
* **api:** update via SDK Studio ([76d29b6](https://github.com/digitalocean/gradient-python/commit/76d29b61ce039f3f270715135ab4d0f444a52b3c))
* **api:** update via SDK Studio ([fa68fb4](https://github.com/digitalocean/gradient-python/commit/fa68fb43e3e175b3dacd62d459b5d8c38b07e367))
* **api:** update via SDK Studio ([e23ac14](https://github.com/digitalocean/gradient-python/commit/e23ac14538e17e8d33c33335285389cf13eefe04))
* **api:** update via SDK Studio ([a5f6aa6](https://github.com/digitalocean/gradient-python/commit/a5f6aa656021a9aaa6a2e82dfa251f87f0096de0))
* **api:** update via SDK Studio ([b900d76](https://github.com/digitalocean/gradient-python/commit/b900d769ba4a290523f17d2d69de850366c961b6))


### Chores

* **client:** support model_access_key in image generations ([4b81c5c](https://github.com/digitalocean/gradient-python/commit/4b81c5cf4998707ca2b4eff25845f687e2002602))
* **client:** support model_access_key in image generations for real ([c202e81](https://github.com/digitalocean/gradient-python/commit/c202e81d81732217a839a0c7c5e56178252362a1))
* fix bash quoting ([d92383d](https://github.com/digitalocean/gradient-python/commit/d92383da134a32cb0ae6f5a1c3044ec4947deacc))
* quote bash variables ([6673263](https://github.com/digitalocean/gradient-python/commit/6673263dbdee2ae77eabd2f6d88cf61921f9e63c))
* remove preview warning ([e4cf6a8](https://github.com/digitalocean/gradient-python/commit/e4cf6a8b5b37acf483be7301aa0a661a5db43a05))
* update actions versions ([7056460](https://github.com/digitalocean/gradient-python/commit/7056460cef8093329da4ed24f2e7bd286213e90d))

## 3.0.2 (2025-09-24)

Full Changelog: [v3.0.1...v3.0.2](https://github.com/digitalocean/gradient-python/compare/v3.0.1...v3.0.2)

### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([d83b77a](https://github.com/digitalocean/gradient-python/commit/d83b77a943d7beb3373eebc543cdc787371753a5))
* improve example values ([8f3a107](https://github.com/digitalocean/gradient-python/commit/8f3a107935a7ef0aa7e0e93161a24c7ecf24a272))
* **types:** change optional parameter type from NotGiven to Omit ([78eb019](https://github.com/digitalocean/gradient-python/commit/78eb019c87cc55186abffd92f1d710d0c6ef0895))

## 3.0.1 (2025-09-24)

Full Changelog: [v3.0.0...v3.0.1](https://github.com/digitalocean/gradient-python/compare/v3.0.0...v3.0.1)

### Bug Fixes

* add proto to default inference url ([#52](https://github.com/digitalocean/gradient-python/issues/52)) ([108d7cb](https://github.com/digitalocean/gradient-python/commit/108d7cb79f4d9046136cbc03cf92056575d04f7a))

## 3.0.0 (2025-09-18)

Full Changelog: [v3.0.0-beta.6...v3.0.0](https://github.com/digitalocean/gradient-python/compare/v3.0.0-beta.6...v3.0.0)

### Chores

* remove deprecated env vars ([#50](https://github.com/digitalocean/gradient-python/issues/50)) ([32292f5](https://github.com/digitalocean/gradient-python/commit/32292f5d7cab21cfaa68577a6f838d134842e3fc))
* remove old folders ([60545d7](https://github.com/digitalocean/gradient-python/commit/60545d7857d8c78c23fba888cc5eae29330eb521))
* update author ([695cc57](https://github.com/digitalocean/gradient-python/commit/695cc572e7f506617b1a37ed600f4e485dbe26c0))


### Refactors

* **api:** consistently rename user_agent parameter to user_agent_package in Gradient and AsyncGradient classes for clarity ([af7420c](https://github.com/digitalocean/gradient-python/commit/af7420c654bd30af4e30a939e31960ba6414adb7))
* **api:** rename user_agent parameter to user_agent_package in BaseClient, SyncAPIClient, and AsyncAPIClient for better clarity ([dba36f7](https://github.com/digitalocean/gradient-python/commit/dba36f7bae0b3d28a0013f5d23c482b7be5e238a))

## 3.0.0-beta.6 (2025-09-17)

Full Changelog: [v3.0.0-beta.5...v3.0.0-beta.6](https://github.com/digitalocean/gradient-python/compare/v3.0.0-beta.5...v3.0.0-beta.6)

### Features

* **api:** enable typescript ([c17086a](https://github.com/digitalocean/gradient-python/commit/c17086aaed18fbb8ba85f050556a193cdc4a233f))
* improve future compat with pydantic v3 ([300eac0](https://github.com/digitalocean/gradient-python/commit/300eac0417f8f17a65bb871b15de1254f4677558))
* normalize user agent with other do clients ([85bc8eb](https://github.com/digitalocean/gradient-python/commit/85bc8eb26afdfd7deb28ce2198eb3ef02181b95f))
* **types:** replace List[str] with SequenceNotStr in params ([5a6aa92](https://github.com/digitalocean/gradient-python/commit/5a6aa9241b5e7c2f4319caa14d62f41c0c824f9e))


### Chores

* clean up LICENSING after legal review ([#49](https://github.com/digitalocean/gradient-python/issues/49)) ([7212f62](https://github.com/digitalocean/gradient-python/commit/7212f62b6d3a5bbc7c8422a7fd8f336d22792049))
* **internal:** move mypy configurations to `pyproject.toml` file ([25c0448](https://github.com/digitalocean/gradient-python/commit/25c044818b636e3307af2fefd2add15a6e650e8d))
* **internal:** update pydantic dependency ([55255fb](https://github.com/digitalocean/gradient-python/commit/55255fb5d51bca4204f5e741024f4184da465d78))
* **tests:** simplify `get_platform` test ([b839e4b](https://github.com/digitalocean/gradient-python/commit/b839e4b31c1262157544bd69536051a10d6b098d))

## 3.0.0-beta.5 (2025-09-08)

Full Changelog: [v3.0.0-beta.4...v3.0.0-beta.5](https://github.com/digitalocean/gradient-python/compare/v3.0.0-beta.4...v3.0.0-beta.5)

### Features

* **api:** manual updates ([044a233](https://github.com/digitalocean/gradient-python/commit/044a2339f9ae89facbed403d8240d1e4cf3e9c1f))
* **api:** manual updates ([0e8fd1b](https://github.com/digitalocean/gradient-python/commit/0e8fd1b364751ec933cadf02be693afa63a67029))


### Bug Fixes

* avoid newer type syntax ([3d5c35c](https://github.com/digitalocean/gradient-python/commit/3d5c35ca11b4c7344308f7fbd7cd98ec44dd65a0))


### Chores

* **internal:** add Sequence related utils ([2997cfc](https://github.com/digitalocean/gradient-python/commit/2997cfc25bf46b4cc9faf9f0f22cb4680cadca8b))
* **internal:** change ci workflow machines ([5f41b3d](https://github.com/digitalocean/gradient-python/commit/5f41b3d956bf1ae25f90b862d5057c16b06e78a3))
* **internal:** update pyright exclude list ([2a0d1a2](https://github.com/digitalocean/gradient-python/commit/2a0d1a2b174990d6b081ff764b13949b4dfa107f))
* update github action ([369c5d9](https://github.com/digitalocean/gradient-python/commit/369c5d982cfadfaaaeda9481b2c9249e3f87423d))

## 3.0.0-beta.4 (2025-08-12)

Full Changelog: [v3.0.0-beta.3...v3.0.0-beta.4](https://github.com/digitalocean/gradient-python/compare/v3.0.0-beta.3...v3.0.0-beta.4)

### Chores

* **internal:** codegen related update ([4757cc5](https://github.com/digitalocean/gradient-python/commit/4757cc594565cf8500b4087205e6eb5fd8c5d5c5))
* **internal:** update comment in script ([c324412](https://github.com/digitalocean/gradient-python/commit/c32441201c3156cc4fe5b400a4f396eaf19ecaad))
* update @stainless-api/prism-cli to v5.15.0 ([835aa7c](https://github.com/digitalocean/gradient-python/commit/835aa7c204f5def64cdcd8b863581fd6a1ea37b6))

## 3.0.0-beta.3 (2025-08-08)

Full Changelog: [v3.0.0-beta.2...v3.0.0-beta.3](https://github.com/digitalocean/gradient-python/compare/v3.0.0-beta.2...v3.0.0-beta.3)

### Features

* **api:** make kwargs match the env vars ([b74952e](https://github.com/digitalocean/gradient-python/commit/b74952e665a92a50937f475ef68331d85d96e018))
* **api:** rename environment variables ([ed70ab7](https://github.com/digitalocean/gradient-python/commit/ed70ab72ce3faecd7fb5070f429275518b7aa6f2))


### Bug Fixes

* actually read env vars ([68daceb](https://github.com/digitalocean/gradient-python/commit/68daceb4cf89b76fbf04e5111cea7541a989afed))
* **config:** align environment variables with other DO tools and console ([#40](https://github.com/digitalocean/gradient-python/issues/40)) ([#41](https://github.com/digitalocean/gradient-python/issues/41)) ([6853d05](https://github.com/digitalocean/gradient-python/commit/6853d0542055a29a70685cab67414e5612890c7d))
* use of cached variable in internals ([4bd6ace](https://github.com/digitalocean/gradient-python/commit/4bd6ace92d2dbfe1364c5f5aa8e0bf5899e8fc16))


### Chores

* **internal:** fix ruff target version ([b370349](https://github.com/digitalocean/gradient-python/commit/b370349a68d24b00854e3f54df50c86f2c29651b))

## 3.0.0-beta.2 (2025-08-04)

Full Changelog: [v3.0.0-beta.1...v3.0.0-beta.2](https://github.com/digitalocean/gradient-python/compare/v3.0.0-beta.1...v3.0.0-beta.2)

### Features

* **api:** collected updates 8/4 ([90ff9f2](https://github.com/digitalocean/gradient-python/commit/90ff9f227aa00805deb270e8e1de0ea9b56e3b4e))

## 3.0.0-beta.1 (2025-07-31)

Full Changelog: [v0.1.0-beta.4...v3.0.0-beta.1](https://github.com/digitalocean/gradient-python/compare/v0.1.0-beta.4...v3.0.0-beta.1)

### Features

* **api:** remove GRADIENTAI env vars ([43d5c5a](https://github.com/digitalocean/gradient-python/commit/43d5c5a6f22e108e1727e6abae9199c1ba2481da))
* **api:** update to package gradient ([9dcd1d6](https://github.com/digitalocean/gradient-python/commit/9dcd1d6c53d31e7da58a7828a0864fc7f633b22c))
* **api:** update to package gradient ([3099c15](https://github.com/digitalocean/gradient-python/commit/3099c154ab5fc3fd104349ce9069cdd18485104d))
* **client:** support file upload requests ([90a77c9](https://github.com/digitalocean/gradient-python/commit/90a77c93c1a0b4a565fbb78f37e69ed6709df223))


### Chores

* update SDK settings ([b7d59f7](https://github.com/digitalocean/gradient-python/commit/b7d59f71d0d511e2ec9bdbf5e548d5e5bf946832))
* update SDK settings ([3b18c48](https://github.com/digitalocean/gradient-python/commit/3b18c48f0c5dbb3f70e73b9a2654d820c8f6a882))
* update SDK settings ([df18f3a](https://github.com/digitalocean/gradient-python/commit/df18f3a44bdc859e78130aa229e7fd0bfc0af906))
* update SDK settings ([33893b0](https://github.com/digitalocean/gradient-python/commit/33893b0a60acc7746e7a60b5066e332547210c38))
* whitespace cleanup ([dd13d32](https://github.com/digitalocean/gradient-python/commit/dd13d321f46cf779fcb841c12068216875f551e0))

## 0.1.0-beta.4 (2025-07-29)

Full Changelog: [v0.1.0-beta.3...v0.1.0-beta.4](https://github.com/digitalocean/gradientai-python/compare/v0.1.0-beta.3...v0.1.0-beta.4)

### Features

* **api:** update via SDK Studio ([3018b4c](https://github.com/digitalocean/gradientai-python/commit/3018b4cc758839eda46617170a24f181d9a0b70b))
* **api:** update via SDK Studio ([4292abf](https://github.com/digitalocean/gradientai-python/commit/4292abf5ba2e89dedf7f7660f6e274e42a163ae0))
* **api:** update via SDK Studio ([2252d77](https://github.com/digitalocean/gradientai-python/commit/2252d77e753a1407a1b851e01f4dcdbf1d4e0697))
* **api:** update via SDK Studio ([7d7d879](https://github.com/digitalocean/gradientai-python/commit/7d7d879480a1d85ac8329cb98fa8da8afd8fee12))

## 0.1.0-beta.3 (2025-07-25)

Full Changelog: [v0.1.0-beta.2...v0.1.0-beta.3](https://github.com/digitalocean/gradient-python/compare/v0.1.0-beta.2...v0.1.0-beta.3)

### Bug Fixes

* **parsing:** parse extra field types ([93bea71](https://github.com/digitalocean/gradient-python/commit/93bea71735195fa3f32de6b64bbc0aaac60a6d6c))


### Chores

* **project:** add settings file for vscode ([3b597aa](https://github.com/digitalocean/gradient-python/commit/3b597aa96e1f588506de47d782444992383f5522))
* update README with new gradient name ([03157fb](https://github.com/digitalocean/gradient-python/commit/03157fb38616c68568024ab7e426b45d414bf432))

## 0.1.0-beta.2 (2025-07-22)

Full Changelog: [v0.1.0-beta.1...v0.1.0-beta.2](https://github.com/digitalocean/gradient-python/compare/v0.1.0-beta.1...v0.1.0-beta.2)

### Bug Fixes

* **parsing:** ignore empty metadata ([cee9728](https://github.com/digitalocean/gradient-python/commit/cee9728fd727cd600d2ac47ead9206ca937f7757))


### Chores

* **internal:** version bump ([e13ccb0](https://github.com/digitalocean/gradient-python/commit/e13ccb069743fc6ebc56e0bb0463ff11864ad944))
* **internal:** version bump ([00ee94d](https://github.com/digitalocean/gradient-python/commit/00ee94d848ae5c5fc4604160c822e4757c4e6de8))
* **types:** rebuild Pydantic models after all types are defined ([db7d61c](https://github.com/digitalocean/gradient-python/commit/db7d61c02df9f86af9170d38539257e9cbf3eff9))

## 0.1.0-beta.1 (2025-07-21)

Full Changelog: [v0.1.0-alpha.19...v0.1.0-beta.1](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.19...v0.1.0-beta.1)

### Features

* **api:** manual updates ([fda6270](https://github.com/digitalocean/gradient-python/commit/fda62708a8f4d4fd66187edd54b39336b88a7e1c))
* **api:** manual updates ([7548648](https://github.com/digitalocean/gradient-python/commit/75486489df49297376fe0bcff70f1e527764b64d))


### Chores

* **internal:** version bump ([be22c3d](https://github.com/digitalocean/gradient-python/commit/be22c3d8c9835b45643d5e91db093108cb03f893))
* **internal:** version bump ([2774d54](https://github.com/digitalocean/gradient-python/commit/2774d540184f8ca7d401c77eaa69a52f62e8514b))
* **internal:** version bump ([44abb37](https://github.com/digitalocean/gradient-python/commit/44abb37d897dc77c1fda511b195cc9297fd324ac))
* **internal:** version bump ([981ba17](https://github.com/digitalocean/gradient-python/commit/981ba17925e46a9f87a141a481645711fbb6bb6e))

## 0.1.0-alpha.19 (2025-07-19)

Full Changelog: [v0.1.0-alpha.18...v0.1.0-alpha.19](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.18...v0.1.0-alpha.19)

### Features

* **api:** manual updates ([2c36a8b](https://github.com/digitalocean/gradient-python/commit/2c36a8be83bb24025adf921c24acba3d666bf25d))


### Chores

* **internal:** version bump ([2864090](https://github.com/digitalocean/gradient-python/commit/2864090c0af4858e4bee35aef2113e6983cfdca4))

## 0.1.0-alpha.18 (2025-07-19)

Full Changelog: [v0.1.0-alpha.17...v0.1.0-alpha.18](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.17...v0.1.0-alpha.18)

### Features

* **api:** manual updates ([92d54ed](https://github.com/digitalocean/gradient-python/commit/92d54edfff94931f10fb8dac822764edf6fca6bd))
* **api:** manual updates ([688982c](https://github.com/digitalocean/gradient-python/commit/688982c143e0ebca62f6ac39c1e074a2fd4083fc))


### Chores

* **internal:** version bump ([ecb4bae](https://github.com/digitalocean/gradient-python/commit/ecb4baedce933efc4ae99e0ef47100a02a68c9cd))
* **internal:** version bump ([feb32ce](https://github.com/digitalocean/gradient-python/commit/feb32ce78b107e9414be87e8c34d8c3274105cb4))
* update pypi package name ([656dfe0](https://github.com/digitalocean/gradient-python/commit/656dfe01d8e301dd1f93b3fa447434e6a5b41270))

## 0.1.0-alpha.17 (2025-07-19)

Full Changelog: [v0.1.0-alpha.16...v0.1.0-alpha.17](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.16...v0.1.0-alpha.17)

### Chores

* **internal:** version bump ([bc0b77b](https://github.com/digitalocean/gradient-python/commit/bc0b77b663dc5837a2e341b70b1cda31224a6d9d))
* **internal:** version bump ([503666f](https://github.com/digitalocean/gradient-python/commit/503666fa61c23e584a22273371850f520100984a))
* **internal:** version bump ([394991e](https://github.com/digitalocean/gradient-python/commit/394991e1f436ac2fa3581a3e1bab02e8a95f94b9))
* **internal:** version bump ([7ae18a1](https://github.com/digitalocean/gradient-python/commit/7ae18a15cc889c8b0ffe5879824745e964cdd637))

## 0.1.0-alpha.16 (2025-07-18)

Full Changelog: [v0.1.0-alpha.15...v0.1.0-alpha.16](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.15...v0.1.0-alpha.16)

### Chores

* **internal:** version bump ([02f1f68](https://github.com/digitalocean/gradient-python/commit/02f1f686505028155ee2a4cf670794117ce7981a))

## 0.1.0-alpha.15 (2025-07-18)

Full Changelog: [v0.1.0-alpha.14...v0.1.0-alpha.15](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.14...v0.1.0-alpha.15)

### Features

* **api:** add gpu droplets ([b207e9a](https://github.com/digitalocean/gradient-python/commit/b207e9a69ddf821522f5d9e9f10502850220585f))
* **api:** add gpu droplets ([b9e317b](https://github.com/digitalocean/gradient-python/commit/b9e317bac2c541a7eafcfb59a4b19c81e1145075))


### Chores

* format ([d940e66](https://github.com/digitalocean/gradient-python/commit/d940e66107e00f351853c0bc667ca6ed3cf98605))
* **internal:** version bump ([1a66126](https://github.com/digitalocean/gradient-python/commit/1a661264f68580dff74c3f7d4891ab2661fde190))
* **internal:** version bump ([9c546a1](https://github.com/digitalocean/gradient-python/commit/9c546a1f97241bb448430e1e43f4e20589e243c1))
* **internal:** version bump ([8814098](https://github.com/digitalocean/gradient-python/commit/881409847161671b798baf2c89f37ae29e195f29))
* **internal:** version bump ([bb3ad60](https://github.com/digitalocean/gradient-python/commit/bb3ad60d02fe01b937eaced64682fd66d95a9aec))
* **internal:** version bump ([2022024](https://github.com/digitalocean/gradient-python/commit/20220246634accf95c4a53df200db5ace7107c55))
* **internal:** version bump ([52e2c23](https://github.com/digitalocean/gradient-python/commit/52e2c23c23d4dc27c176ebf4783c8fbd86a4c07b))
* **internal:** version bump ([8ac0f2a](https://github.com/digitalocean/gradient-python/commit/8ac0f2a6d4862907243ba78b132373289e2c3543))
* **internal:** version bump ([d83fe97](https://github.com/digitalocean/gradient-python/commit/d83fe97aa2f77c84c3c7f4bf40b9fb94c5c28aca))
* **internal:** version bump ([9d20399](https://github.com/digitalocean/gradient-python/commit/9d2039919e1d9c9e6d153edfb03bccff18b56686))
* **internal:** version bump ([44a045a](https://github.com/digitalocean/gradient-python/commit/44a045a9c0ce0f0769cce66bc7421a9d81cbc645))
* **internal:** version bump ([95d1dd2](https://github.com/digitalocean/gradient-python/commit/95d1dd24d290d7d5f23328e4c45c439dca5df748))
* **internal:** version bump ([7416147](https://github.com/digitalocean/gradient-python/commit/74161477f98e3a76b7227b07d942e1f26a4612b3))
* **internal:** version bump ([06d7f19](https://github.com/digitalocean/gradient-python/commit/06d7f19cd42a6bc578b39709fe6efed8741a24bc))

## 0.1.0-alpha.14 (2025-07-17)

Full Changelog: [v0.1.0-alpha.13...v0.1.0-alpha.14](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.13...v0.1.0-alpha.14)

### Features

* **api:** update via SDK Studio ([6cdcc6a](https://github.com/digitalocean/gradient-python/commit/6cdcc6a36b9dde2117295ee7bcb9a3bc15571779))
* **api:** update via SDK Studio ([5475a94](https://github.com/digitalocean/gradient-python/commit/5475a9460676d1c48e99e0d1e75e50de7caecf3a))
* dynamically build domain for agents.chat.completions.create() ([dee4ef0](https://github.com/digitalocean/gradient-python/commit/dee4ef07ebb3367abc7f05c15271d43ab57e2081))
* dynamically build domain for agents.chat.completions.create() ([3dbd194](https://github.com/digitalocean/gradient-python/commit/3dbd194643e31907a78ab7e222e95e7508378ada))


### Bug Fixes

* add /api prefix for agent routes ([00c62b3](https://github.com/digitalocean/gradient-python/commit/00c62b35f3a29ea8b6e7c96b2e755e6b5199ae55))
* add /api prefix for agent routes ([72a59db](https://github.com/digitalocean/gradient-python/commit/72a59db98ebeccdf0c4498f6cce37ffe1cb198dd))
* fix validation for inference_key and agent_key auth ([d27046d](https://github.com/digitalocean/gradient-python/commit/d27046d0c1e8214dd09ab5508e4fcb11fa549dfe))


### Chores

* **internal:** version bump ([f3629f1](https://github.com/digitalocean/gradient-python/commit/f3629f169267f240aeb2c4d400606761a649dff7))

## 0.1.0-alpha.13 (2025-07-15)

Full Changelog: [v0.1.0-alpha.12...v0.1.0-alpha.13](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.12...v0.1.0-alpha.13)

### Features

* **api:** manual updates ([bd6fecc](https://github.com/digitalocean/gradient-python/commit/bd6feccf97fa5877085783419f11dad04c57d700))
* **api:** manual updates ([c2b96ce](https://github.com/digitalocean/gradient-python/commit/c2b96ce3d95cc9b74bffd8d6a499927eefd23b14))
* **api:** share chat completion chunk model between chat and agent.chat ([d67371f](https://github.com/digitalocean/gradient-python/commit/d67371f9f4d0761ea03097820bc3e77654b4d2bf))
* clean up environment call outs ([64ee5b4](https://github.com/digitalocean/gradient-python/commit/64ee5b449c0195288d0a1dc55d2725e8cdd6afcf))


### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([507a342](https://github.com/digitalocean/gradient-python/commit/507a342fbcc7c801ba36708e56ea2d2a28a1a392))
* **parsing:** correctly handle nested discriminated unions ([569e473](https://github.com/digitalocean/gradient-python/commit/569e473d422928597ccf762133d5e52ac9a8665a))


### Chores

* **internal:** bump pinned h11 dep ([6f4e960](https://github.com/digitalocean/gradient-python/commit/6f4e960b6cb838cbf5e50301375fcb4b60a2cfb3))
* **internal:** codegen related update ([1df657d](https://github.com/digitalocean/gradient-python/commit/1df657d9b384cb85d27fe839c0dab212a7773f8f))
* **package:** mark python 3.13 as supported ([1a899b6](https://github.com/digitalocean/gradient-python/commit/1a899b66a484986672a380e405f09b1ae94b6310))
* **readme:** fix version rendering on pypi ([6fbe83b](https://github.com/digitalocean/gradient-python/commit/6fbe83b11a9e3dbb40cf7f9f627abbbd086ee24a))

## 0.1.0-alpha.12 (2025-07-02)

Full Changelog: [v0.1.0-alpha.11...v0.1.0-alpha.12](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.11...v0.1.0-alpha.12)

### Bug Fixes

* **ci:** correct conditional ([646b4c6](https://github.com/digitalocean/gradient-python/commit/646b4c62044c9bb5211c50e008ef30c777715acb))


### Chores

* **ci:** change upload type ([7449413](https://github.com/digitalocean/gradient-python/commit/7449413efc16c58bc484f5f5793aa9cd36c3f405))
* **internal:** codegen related update ([434929c](https://github.com/digitalocean/gradient-python/commit/434929ce29b314182dec1542a3093c98ca0bb24a))

## 0.1.0-alpha.11 (2025-06-28)

Full Changelog: [v0.1.0-alpha.10...v0.1.0-alpha.11](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.10...v0.1.0-alpha.11)

### Features

* **api:** manual updates ([8d918dc](https://github.com/digitalocean/gradient-python/commit/8d918dcc45f03d799b3aed4e94276086e2d7ea9b))


### Chores

* **ci:** only run for pushes and fork pull requests ([adfb5b5](https://github.com/digitalocean/gradient-python/commit/adfb5b51149f667bf9a0b4b4c4c6418e91f843d8))
* Move model providers ([8d918dc](https://github.com/digitalocean/gradient-python/commit/8d918dcc45f03d799b3aed4e94276086e2d7ea9b))

## 0.1.0-alpha.10 (2025-06-28)

Full Changelog: [v0.1.0-alpha.9...v0.1.0-alpha.10](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.9...v0.1.0-alpha.10)

### Features

* **api:** manual updates ([0e5effc](https://github.com/digitalocean/gradient-python/commit/0e5effc727cebe88ea38f0ec4c3fcb45ffeb4924))
* **api:** manual updates ([d510ae0](https://github.com/digitalocean/gradient-python/commit/d510ae03f13669af7f47093af06a00609e9b7c07))
* **api:** manual updates ([c5bc3ca](https://github.com/digitalocean/gradient-python/commit/c5bc3caa477945dc19bbf90661ffeea86370189d))

## 0.1.0-alpha.9 (2025-06-28)

Full Changelog: [v0.1.0-alpha.8...v0.1.0-alpha.9](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.8...v0.1.0-alpha.9)

### Features

* **api:** manual updates ([e0c210a](https://github.com/digitalocean/gradient-python/commit/e0c210a0ffde24bd2c5877689f8ab222288cc597))

## 0.1.0-alpha.8 (2025-06-27)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* **client:** setup streaming ([3fd6e57](https://github.com/digitalocean/gradient-python/commit/3fd6e575f6f5952860e42d8c1fa22ccb0b10c623))

## 0.1.0-alpha.7 (2025-06-27)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** manual updates ([63b9ec0](https://github.com/digitalocean/gradient-python/commit/63b9ec02a646dad258afbd048db8db1af8d4401b))
* **api:** manual updates ([5247aee](https://github.com/digitalocean/gradient-python/commit/5247aee6d6052f6380fbe892d7c2bd9a8d0a32c0))
* **api:** manual updates ([aa9e2c7](https://github.com/digitalocean/gradient-python/commit/aa9e2c78956162f6195fdbaa1c95754ee4af207e))
* **client:** add agent_domain option ([b4b6260](https://github.com/digitalocean/gradient-python/commit/b4b62609a12a1dfa0b505e9ec54334b776fb0515))

## 0.1.0-alpha.6 (2025-06-27)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** manual updates ([04eb1be](https://github.com/digitalocean/gradient-python/commit/04eb1be35de7db04e1f0d4e1da8719b54a353bb5))

## 0.1.0-alpha.5 (2025-06-27)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** define api links and meta as shared models ([8d87001](https://github.com/digitalocean/gradient-python/commit/8d87001b51de17dd1a36419c0e926cef119f20b8))
* **api:** update OpenAI spec and add endpoint/smodels ([e92c54b](https://github.com/digitalocean/gradient-python/commit/e92c54b05f1025b6173945524724143fdafc7728))
* **api:** update via SDK Studio ([1ae76f7](https://github.com/digitalocean/gradient-python/commit/1ae76f78ce9e74f8fd555e3497299127e9aa6889))
* **api:** update via SDK Studio ([98424f4](https://github.com/digitalocean/gradient-python/commit/98424f4a2c7e00138fb5eecf94ca72e2ffcc1212))
* **api:** update via SDK Studio ([299fd1b](https://github.com/digitalocean/gradient-python/commit/299fd1b29b42f6f2581150e52dcf65fc73270862))
* **api:** update via SDK Studio ([9a45427](https://github.com/digitalocean/gradient-python/commit/9a45427678644c34afe9792a2561f394718e64ff))
* **api:** update via SDK Studio ([abe573f](https://github.com/digitalocean/gradient-python/commit/abe573fcc2233c7d71f0a925eea8fa9dd4d0fb91))
* **api:** update via SDK Studio ([e5ce590](https://github.com/digitalocean/gradient-python/commit/e5ce59057792968892317215078ac2c11e811812))
* **api:** update via SDK Studio ([1daa3f5](https://github.com/digitalocean/gradient-python/commit/1daa3f55a49b5411d1b378fce30aea3ccbccb6d7))
* **api:** update via SDK Studio ([1c702b3](https://github.com/digitalocean/gradient-python/commit/1c702b340e4fd723393c0f02df2a87d03ca8c9bb))
* **api:** update via SDK Studio ([891d6b3](https://github.com/digitalocean/gradient-python/commit/891d6b32e5bdb07d23abf898cec17a60ee64f99d))
* **api:** update via SDK Studio ([dcbe442](https://github.com/digitalocean/gradient-python/commit/dcbe442efc67554e60b3b28360a4d9f7dcbb313a))
* use inference key for chat.completions.create() ([5d38e2e](https://github.com/digitalocean/gradient-python/commit/5d38e2eb8604a0a4065d146ba71aa4a5a0e93d85))


### Bug Fixes

* **ci:** release-doctor — report correct token name ([4d2b3dc](https://github.com/digitalocean/gradient-python/commit/4d2b3dcefdefc3830d631c5ac27b58778a299983))


### Chores

* clean up pyproject ([78637e9](https://github.com/digitalocean/gradient-python/commit/78637e99816d459c27b4f2fd2f6d79c8d32ecfbe))
* **internal:** codegen related update ([58d7319](https://github.com/digitalocean/gradient-python/commit/58d7319ce68c639c2151a3e96a5d522ec06ff96f))

## 0.1.0-alpha.4 (2025-06-25)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/digitalocean/gradient-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** update via SDK Studio ([d1ea884](https://github.com/digitalocean/gradient-python/commit/d1ea884c9be72b3f8804c5ba91bf4f77a3284a6c))
* **api:** update via SDK Studio ([584f9f1](https://github.com/digitalocean/gradient-python/commit/584f9f1304b3612eb25f1438041d287592463438))
* **api:** update via SDK Studio ([7aee6e5](https://github.com/digitalocean/gradient-python/commit/7aee6e55a0574fc1b6ab73a1777c92e4f3a940ea))
* **api:** update via SDK Studio ([4212f62](https://github.com/digitalocean/gradient-python/commit/4212f62b19c44bcb12c02fe396e8c51dd89d3868))
* **api:** update via SDK Studio ([b16cceb](https://github.com/digitalocean/gradient-python/commit/b16cceb63edb4253084036b693834bde5da10943))
* **api:** update via SDK Studio ([34382c0](https://github.com/digitalocean/gradient-python/commit/34382c06c5d61ac97572cb4977d020e1ede9d4ff))
* **api:** update via SDK Studio ([c33920a](https://github.com/digitalocean/gradient-python/commit/c33920aba0dc1f3b8f4f890ce706c86fd452dd6b))
* **api:** update via SDK Studio ([359c8d8](https://github.com/digitalocean/gradient-python/commit/359c8d88cec1d60f0beb810b5a0139443d0a3348))
* **api:** update via SDK Studio ([f27643e](https://github.com/digitalocean/gradient-python/commit/f27643e1e00f606029be919a7117801facc6e5b7))
* **api:** update via SDK Studio ([e59144c](https://github.com/digitalocean/gradient-python/commit/e59144c2d474a4003fd28b8eded08814ffa8d2f3))
* **api:** update via SDK Studio ([97e1768](https://github.com/digitalocean/gradient-python/commit/97e17687a348b8ef218c23a06729b6edb1ac5ea9))
* **api:** update via SDK Studio ([eac41f1](https://github.com/digitalocean/gradient-python/commit/eac41f12912b8d32ffa23d225f4ca56fa5c72505))
* **api:** update via SDK Studio ([1fa7ebb](https://github.com/digitalocean/gradient-python/commit/1fa7ebb0080db9087b82d29e7197e44dfbb1ebed))
* **api:** update via SDK Studio ([aa2610a](https://github.com/digitalocean/gradient-python/commit/aa2610afe7da79429e05bff64b4796de7f525681))
* **api:** update via SDK Studio ([e5c8d76](https://github.com/digitalocean/gradient-python/commit/e5c8d768388b16c06fcc2abee71a53dcc8b3e8c5))
* **api:** update via SDK Studio ([5f700dc](https://github.com/digitalocean/gradient-python/commit/5f700dc7a4e757015d3bd6f2e82a311114b82d77))
* **api:** update via SDK Studio ([c042496](https://github.com/digitalocean/gradient-python/commit/c04249614917198b1eb2324438605d99b719a1cf))
* **api:** update via SDK Studio ([5ebec81](https://github.com/digitalocean/gradient-python/commit/5ebec81604a206eba5e75a7e8990bd7711ba8f47))
* **api:** update via SDK Studio ([cac54a8](https://github.com/digitalocean/gradient-python/commit/cac54a81a3f22d34b2de0ebfac3c68a982178cad))
* **api:** update via SDK Studio ([6d62ab0](https://github.com/digitalocean/gradient-python/commit/6d62ab00594d70df0458a0a401f866af15a9298e))
* **api:** update via SDK Studio ([0ccc62c](https://github.com/digitalocean/gradient-python/commit/0ccc62cb8ef387e0aaf6784db25d5f99a587e5da))
* **api:** update via SDK Studio ([e75adfb](https://github.com/digitalocean/gradient-python/commit/e75adfbd2d035e57ae110a1d78ea40fb116975e5))
* **api:** update via SDK Studio ([8bd264b](https://github.com/digitalocean/gradient-python/commit/8bd264b4b4686ca078bf4eb4b5462f058406df3e))
* **api:** update via SDK Studio ([6254ccf](https://github.com/digitalocean/gradient-python/commit/6254ccf45cbe50ca8191c7149824964f5d00d82f))
* **api:** update via SDK Studio ([8f5761b](https://github.com/digitalocean/gradient-python/commit/8f5761b1d18fb48ad7488e6f0ad771c077eb7961))
* **api:** update via SDK Studio ([f853616](https://github.com/digitalocean/gradient-python/commit/f8536166320d1d5bacf1d10a5edb2f71691dde8b))
* **client:** add support for aiohttp ([494afde](https://github.com/digitalocean/gradient-python/commit/494afde754f735d1ba95011fc83d23d2410fcfdd))


### Bug Fixes

* **client:** correctly parse binary response | stream ([abba5be](https://github.com/digitalocean/gradient-python/commit/abba5be958d03a7e5ce7d1cbf8069c0bcf52ee20))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([e649dcb](https://github.com/digitalocean/gradient-python/commit/e649dcb0f9416e9bf568cc9f3480d7e222052391))


### Chores

* **ci:** enable for pull requests ([b6b3f9e](https://github.com/digitalocean/gradient-python/commit/b6b3f9ea85918cfc6fc7304b2d21c340d82a0083))
* **internal:** codegen related update ([4126872](https://github.com/digitalocean/gradient-python/commit/41268721eafd33fcca5688ca5dff7401f25bdeb2))
* **internal:** codegen related update ([10b79fb](https://github.com/digitalocean/gradient-python/commit/10b79fb1d51bcff6ed0d18e5ccd18fd1cd75af9f))
* **internal:** update conftest.py ([12e2103](https://github.com/digitalocean/gradient-python/commit/12e210389204ff74f504e1ec3aa5ba99f1b4971c))
* **readme:** update badges ([6e40dc3](https://github.com/digitalocean/gradient-python/commit/6e40dc3fa4e33082be7b0bbf65d07e9ae9ac6370))
* **tests:** add tests for httpx client instantiation & proxies ([7ecf66c](https://github.com/digitalocean/gradient-python/commit/7ecf66c58a124c153a32055967beacbd1a3bbcf3))
* **tests:** run tests in parallel ([861dd6b](https://github.com/digitalocean/gradient-python/commit/861dd6b75956f2c12814ad32b05624d8d8537d52))
* **tests:** skip some failing tests on the latest python versions ([75b4539](https://github.com/digitalocean/gradient-python/commit/75b45398c18e75be3389be20479f54521c2e474a))
* update SDK settings ([ed595b0](https://github.com/digitalocean/gradient-python/commit/ed595b0a23df125ffba733d7339e771997c3f149))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([5d452d7](https://github.com/digitalocean/gradient-python/commit/5d452d7245af6c80f47f8395f1c03493dfb53a52))

## 0.1.0-alpha.3 (2025-06-12)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/digitalocean/genai-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Chores

* update SDK settings ([502bb34](https://github.com/digitalocean/genai-python/commit/502bb34e1693603cd572c756e8ce6aeba63d1283))

## 0.1.0-alpha.2 (2025-06-12)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/digitalocean/genai-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Chores

* update SDK settings ([5b3b94b](https://github.com/digitalocean/genai-python/commit/5b3b94b57a4ba7837093617aafc2ce2d21ac87f1))

## 0.1.0-alpha.1 (2025-06-12)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/digitalocean/genai-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([1e202d0](https://github.com/digitalocean/genai-python/commit/1e202d01e3582ef5284380417d9f7e195bbc8a39))
* **api:** update via SDK Studio ([e6103ad](https://github.com/digitalocean/genai-python/commit/e6103ad8134752e632cf1dae9cb09edf10fd7739))
* **api:** update via SDK Studio ([bf61629](https://github.com/digitalocean/genai-python/commit/bf61629f25376f1cc32b910fbaea9feccfef9884))
* **api:** update via SDK Studio ([c680ef3](https://github.com/digitalocean/genai-python/commit/c680ef3bac9874ef595edde2bd8f0ce5948ac6c4))
* **api:** update via SDK Studio ([a4bb08b](https://github.com/digitalocean/genai-python/commit/a4bb08ba4829b5780511b78538e5cbbc276f1965))
* **api:** update via SDK Studio ([691923d](https://github.com/digitalocean/genai-python/commit/691923d9f60b5ebe5dc34c8227273d06448945e8))
* **client:** add follow_redirects request option ([5a6d480](https://github.com/digitalocean/genai-python/commit/5a6d480aef6d4c5084f484d1b69e6f49568a8caf))


### Chores

* **docs:** remove reference to rye shell ([29febe9](https://github.com/digitalocean/genai-python/commit/29febe9affcb0ae41ec69f8aea3ae6ef53967537))
* **docs:** remove unnecessary param examples ([35ec489](https://github.com/digitalocean/genai-python/commit/35ec48915a8bd750060634208e91bd98c905b53c))
* update SDK settings ([a095281](https://github.com/digitalocean/genai-python/commit/a095281b52c7ac5f096147e67b7b2e5bf342f95e))
* update SDK settings ([d2c39ec](https://github.com/digitalocean/genai-python/commit/d2c39eceea1aaeaf0e6c2707af10c3998d222bda))
* update SDK settings ([f032621](https://github.com/digitalocean/genai-python/commit/f03262136aa46e9325ac2fae785bf48a56f0127b))
* update SDK settings ([b2cf700](https://github.com/digitalocean/genai-python/commit/b2cf700a0419f7d6e3f23ee02747fe7766a05f98))
