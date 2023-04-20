A simple tool to convert strings taken from cat-aws-tdl into blocks that can be added into an ECS task definition.

Call the tool with a file as an argument like:

`./convert.py examplefile.txt`

You may need to make the py file an executable by running:

`chmod 755 convert.py`

This tool makes it easier to change the format between key : value pairs like this:

```
key1 : value1
key2 : value2
key3 : value3
```

Into this:

```
                {
                    "name": "key1",
                    "value": "value1"
                },
                {
                    "name": "key2",
                    "value": "value2"
                },
                {
                    "name": "key3",
                    "value": "value3"
                },
```
