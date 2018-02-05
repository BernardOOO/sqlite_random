
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
    - order: "speak to me"
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

> **Note:** The FortunesDB.db i provide is an exemple, made from Debian packages "Fortune" and "Fortune-fr".

## Licence

Here define or link the licence you want to use.
