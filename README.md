
# sqlite_random

## Synopsis

In Kalliope, this neuron read a random statement from a sqlite database and say it.

## Installation
```bash
kalliope install --git-url https://github.com/BernardOOO/sqlite_random.git
```

## Options

(usage of a [table generator](http://www.tablesgenerator.com/markdown_tables) is recommended)

| parameter        | required | default                       | values                           | comments                     |
|------------------|----------|-------------------------------|-----------------------------------|------------------------------|
| base | yes      |                               |The absolute path to the database |  |
| table | yes       |                               | The table name |  |
| column | yes      |  |     The column name                              |  |


## Return Values

Only necessary when the neuron use a template to say something

| name      | description                        | type       | sample                    |
|-----------|------------------------------------|------------|---------------------------|
| value_key | dictionary containing all the data | dictionary | {"name":"me", "email": 2} |
| value_key | list of value                      | list       | ["val1", "val2", "val3"]  |
| value_key | string value                       | string     | "2"                       |


## Synapses example

Description of what the synapse will do
```yml
 - name: "type here your name"
   signals:
     - order: "this is what I have to say to run this synapse"
   neurons:      
     - neuron_name:
        parameter: "value"
        parameter: "value"
        file_template: template_name.j2
    
```

## Templates example 

Description of the template
```
This is a var {{ var }} 
{% for item in items %}
 This is the  {{ item }}  
{% endfor %}
```

## Notes

> **Note:** This is an important note concerning the neuron

## Licence

Here define or link the licence you want to use.
