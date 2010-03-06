from ragendja.settings_post import settings

settings.add_app_media('combined-%(LANGUAGE_DIR)s.css',
    'article/css/article.css',
    'article/css/editor.css',
)

settings.add_app_media('combined-%(LANGUAGE_CODE)s.js',
    'article/js/article.js',
    'article/js/editor.js',
    'article/js/uploadhandler.js',
)