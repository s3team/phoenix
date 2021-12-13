# A2C

A2C translates the assembly code output from Uroboros to an analyzable and compilable C code.

## Requirements

Before using our framework, please make sure that you can build and run [Uroboros](../uroboros) properly.

## Usage

Our tool takes the asm file generated from [Uroboros](../uroboros) as the input. After you get that, you can use our tool as follows:

    python3 a2c.py asm_file_from_urobros [-o/--output <file>]

Then you can find the generated C file at current dicrectory. If you do not specify the name yourself, the default output will be **output.c**. Otherwise, the filename will be **\<file\>.c**. x

## Directory Structure

``` python
├── src	
│   ├── a2c.py	
│   ├── builder.py
│   ├── definition.py
│   ├── inst_template.py
│   ├── loader.py
│   ├── program_info.py
│   ├── register.py
│   ├── runtime_info.py
│   ├── translator.py
│   └── util.py
└── template 
    ├── code_template.c
    └── template_file
```

