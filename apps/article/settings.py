from ragendja.settings_post import settings

settings.add_app_media('combined-%(LANGUAGE_DIR)s.css',
    'article/css/screen.css'
)

settings.add_app_media('combined-%(LANGUAGE_CODE)s.js',
    'article/js/article.js',
)