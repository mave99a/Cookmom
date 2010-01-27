from ragendja.settings_post import settings

settings.add_uncombined_app_media('photostoryeditor')
#
settings.add_app_media('combined-%(LANGUAGE_DIR)s.css',
    'photostoryeditor/css/screen.css'
)

settings.add_app_media('combined-%(LANGUAGE_CODE)s.js',
    'photostoryeditor/js/editor.js',
)

