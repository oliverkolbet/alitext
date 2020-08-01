```bash
ali [FILE]
```
default alipack command
```bash
ali [FILE] -s [SEGMENT]
```
instead of running the section ``<main>``, runs the segment given. (i.e,``<user:ar1``, ``<stuff>``,``<secret:ar1:ar2>``)
```bash
ali raw [FILE]
```
installs a raw alias file to ~/.bash_aliases
```bash
ali [FILE] -sa [SEGMENT] [ARGUMENTS (separated by ':')]
```
runs a segment with arguments.
```bash
ali [FILE] -a [ARGUMENTS]
```
runs ``<main>`` with arguments.
