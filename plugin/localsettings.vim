if exists('g:loaded_localsettings')
	finish
endif
let g:loaded_localsettings = 1

au FileType * py import localsettings; localsettings.apply_settings()
