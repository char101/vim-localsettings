import os
import vim
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

cache = {}

def load_settings(file):
    file_dir = os.path.dirname(file)

    for dir, settings in cache.items():
        if file_dir.startswith(dir):
            return settings

    dir = file_dir
    for i in range(0, 100):
        settings_file = os.path.join(dir, '.localsettings')
        if os.path.isfile(settings_file):
            cp = ConfigParser()
            cp.read([settings_file])
            settings = {s: dict(cp.items(s)) for s in cp.sections()}
            cache[dir + os.sep] = settings
            return settings
        parent_dir = os.path.dirname(dir)
        if parent_dir == dir:
            break
        dir = parent_dir

def apply_settings():
    buf = vim.current.buffer
    localsettings = load_settings(buf.name)
    if localsettings:
        settings = localsettings.get('global', {})
        settings.update(localsettings.get(buf.options['filetype'], {}))
        for k, v in settings.items():
            if v == '':
                vim.command('setlocal {}'.format(k))
            else:
                vim.command('setlocal {}={}'.format(k, v))
