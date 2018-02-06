
# sqlite_random

## Synopsis

In Kalliope, this neuron read a random statement from a sqlite database and say it.

## Installation
```bash
kalliope install --git-url https://github.com/BernardOOO/sqlite_random.git
```

## Options


| parameter        | required | default                       | values                           |
|------------------|----------|-------------------------------|-----------------------------------|
| base | yes      |                               |The absolute path to the database |
| table | yes       |                               | The table name |
| column | yes      |  |     The column name                              |


## Return Values

| name      | description                        | type       |
|-----------|------------------------------------|------------|
| text | The sentence in the statement | text |


## Synapses example
    
```
- name: "say-me-something"
  signals:
    - order: "say me something"
    - order: "dis-moi quelque chose"
    - order: "speak to me"
    - order: "parle-moi"
  neurons:
    - sqlite_random:
        base: /home/pi/kalliope_fr/resources/db/FortunesDB.db
        table: "sentences"
        column : "TEXTE"
        say_template: "{{ text }}"
        tts:
          pico2wave:
            cache: False

```

## Notes

> **Note:** The FortunesDB.db i provide is an example, made from Debian packages "Fortune" and "Fortune-fr".

## Licence

Copyright (c) 2018. All rights reserved.

Kalliope is covered by the MIT license, a permissive free software license that lets you do anything you want with the source code, as long as you provide back attribution and "don't hold you liable". For the full license text see the LICENSE.md file.
