# vexmason template repository (simplified version)

Simply click "Use this Template" to get started with
[vexmason](https://github.com/zabackary/vexmason), the VEX V5 Python bundler
that Just Works(r).

vexmason is a bundler that allows you to write modern, OOP, abstract Python code
and yet still use the VEXCode V5 build/upload tools maintained by VEX.

This repo contains a simplified version of the code available at
[`zabackary/vexmason-template`](https://github.com/zabackary/vexmason-template).

## Setup

- `.vscode/vexmason-config.json`  
  This contains the program name, description and defines.
- `.vscode/vexmason-local-config.json`  
  This file is gitignored, but you should use
  [`vexmason-local-config.example.json`](./.vscode/vexmason-local-config.example.json)
  as an example to get started. It contains the computer name (which you can use
  as a placeholder in the description like this: `{{ computer-name }}`) and the
  local defines overrides.
- `src/`  
  This is where your code lives! I have some things there already, but please
  modify it to suit your setup.

## Support

If you run into any problems while compiling (i.e., an error popup saying VEX
Error in the bottom right of your screen), make sure to check
[`build/vexmason.log`](./build/vexmason.log) to see if there's any useful logs.

If you can't figure it out, leave a
[GitHub issue](https://github.com/zabackary/vexmason-template/issues/new) and
I'll get back to you soon. I'll also be at our team's table or somewhere near it
during VEX VRC Over Under Worlds 2024.

## Small personal note

<sup>(feel free to ignore this)</sup><br> Maybe you've heard the story of Jesus
or have heard the name, but there are still _so_ many people who haven't heard
the "Good News", or the gospel of Christianity. Whether you're Christian or not,
I urge you to find out that God's love for you, even through all your mistakes
and failures both with robotics and with life, was large enough that He died for
you to bring you back into a loving relationship with Him.
