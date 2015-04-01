# vim-localsettings

Find `.localsettings` in project directory and load it.
The plugin caches the localsettings so the localsettings file will be loaded only once for all files in the same project directory.

## Example `.localsettings`
```conf
[global]
ts = 4
sw = 4

[javascript]
ts = 2
sw = 2
```

## Requirements

`vim` compiled with `python` support.
