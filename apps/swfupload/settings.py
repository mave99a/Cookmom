from ragendja.settings_post import settings

settings.add_uncombined_app_media('swfupload')

settings.add_app_media('combined-%(LANGUAGE_DIR)s.css',
    'swfupload/css/swfupload.css'
)

settings.add_app_media('combined-%(LANGUAGE_CODE)s.js',
    'swfupload/js/swfupload.js',
)